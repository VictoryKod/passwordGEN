import tkinter
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
import customtkinter as ctk
from PIL import Image
import password  # Импорт файла с функцией генерации пароля


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry('460x700')
        self.title('Password generator')
        self.resizable(False, False)
 
        self.grid_rowconfigure(2, weight=1)  # Рамка с настройками будет растягиваться
        self.grid_columnconfigure(0, weight=1)

        # Лого
        self.logo = ctk.CTkImage(dark_image=Image.open('logo_gen.png'), size=(460, 400))
        self.logo_label = ctk.CTkLabel(master=self, text="", image=self.logo)
        self.logo_label.grid(row=0, column=0)

        # Фрейм с полем для пароля
        self.password_frame = ctk.CTkFrame(master=self, fg_color='transparent')
        self.password_frame.grid(row=1, column=0, padx=(20, 20), pady=10, sticky="nsew")

        self.entry_password = ctk.CTkEntry(master=self.password_frame, width=300, height=35)
        self.entry_password.grid(row=0, column=0, padx=(0, 20))

        self.btn_generate = ctk.CTkButton(master=self.password_frame, text='Generate', width=100, height=35,
                                          command=self.set_password)
        self.btn_generate.grid(row=0, column=1)

        # Фрейм для настроек пароля
        self.settings_frame = ctk.CTkFrame(master=self)
        self.settings_frame.grid(row=2, column=0, padx=(20, 20), pady=(20, 20), sticky='nsew')

        # Конфигурация сетки для фрейма с настройками
        self.settings_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)  # Равномерное распределение колонок

        # Слайдер длины пароля
        self.password_lenght_slider = ctk.CTkSlider(master=self.settings_frame, from_=1, to=100,
                                                    number_of_steps=100, command=self.slider_event)
        self.password_lenght_slider.grid(row=0, column=0, columnspan=3, padx=(10, 10), pady=(10, 0), sticky='ew')

        # Поле для отображения длины пароля (+возможность ввода с клавиатуры)
        self.password_lenght_entry = ctk.CTkEntry(master=self.settings_frame, width=50, height=35)
        self.password_lenght_entry.grid(row=0, column=3, padx=(10, 10), pady=(10, 0), sticky='we')

        # Привязка события на изменение в поле ввода длины пароля
        self.password_lenght_entry.bind("<KeyRelease>", self.entry_event)

        # Поле для чек-боксов (настройки символов)
        self.cb_digits_var = tkinter.StringVar()
        self.cb_digits = ctk.CTkCheckBox(master=self.settings_frame, text='0-9', variable=self.cb_digits_var,
                                         onvalue=digits, offvalue='')
        self.cb_digits.grid(row=1, column=0, padx=10, pady=10)

        self.cb_lower_var = tkinter.StringVar()
        self.cb_lower = ctk.CTkCheckBox(master=self.settings_frame, text='a-z', variable=self.cb_lower_var,
                                        onvalue=ascii_lowercase, offvalue='')
        self.cb_lower.grid(row=1, column=1, padx=10, pady=10)

        self.cb_upper_var = tkinter.StringVar()
        self.cb_upper = ctk.CTkCheckBox(master=self.settings_frame, text='A-Z', variable=self.cb_upper_var,
                                        onvalue=ascii_uppercase, offvalue='')
        self.cb_upper.grid(row=1, column=2, padx=10, pady=10)

        self.cb_symbol_var = tkinter.StringVar()
        self.cb_symbol = ctk.CTkCheckBox(master=self.settings_frame, text='@#$%', variable=self.cb_symbol_var,
                                         onvalue=punctuation, offvalue='')
        self.cb_symbol.grid(row=1, column=3, padx=10, pady=10)

        # Опции внешнего вида
        self.appearance_mode_option_menu = ctk.CTkOptionMenu(self.settings_frame,
                                                             values=["Light", "Dark", "System"],
                                                             command=self.change_appearance_mode_event)
        self.appearance_mode_option_menu.grid(row=2, column=0, columnspan=4, pady=(40, 10))

        self.appearance_mode_option_menu.set("System")  # Тема синхронизируется с системой при запуске

        # Установка длины пароля по умолчанию (8 символов)
        self.password_lenght_slider.set(8)
        self.password_lenght_entry.insert(0, "8")

    def slider_event(self, value):
        # Вывод длины пароля в entry при изменении слайдера
        self.password_lenght_entry.delete(0, "end")
        self.password_lenght_entry.insert(0, str(int(value)))

    def entry_event(self, event):
        # Обработка изменения длины пароля с клавиатуры
        try:
            value = int(self.password_lenght_entry.get())
            if 1 <= value <= 100:  # Ограничение значений (1-100)
                self.password_lenght_slider.set(value)
        except ValueError:
            pass  # Игнорируем некорректные значения

    def change_appearance_mode_event(self, new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode)

    def get_characters(self):
        chars = "".join(self.cb_digits_var.get() + self.cb_lower_var.get()
                        + self.cb_upper_var.get() + self.cb_symbol_var.get())
        return chars

    def set_password(self):
        # Генерация пароля
        self.entry_password.delete(0, 'end')
        self.entry_password.insert(0, password.create_new(length=int(self.password_lenght_slider.get()),
                                                          characters=self.get_characters()))


if __name__ == '__main__':
    app = App()
    app.mainloop()


