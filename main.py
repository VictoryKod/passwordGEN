import customtkinter as ctk
from PIL import Image

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry('460x700')
        self.title('Password generator')
        self.resizable(False, False)

        # Конфигурация сетки для растяжения
        self.grid_rowconfigure(2, weight=1)  # Рамка с настройками будет растягиваться
        self.grid_columnconfigure(0, weight=1)

        # Логотип
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
        self.settings_frame.grid_rowconfigure(1, weight=1)
        self.settings_frame.grid_columnconfigure(0, weight=3)  # Колонка для слайдера
        self.settings_frame.grid_columnconfigure(1, weight=1)  # Колонка для поля длины

        # Слайдер длины пароля
        self.password_lenght_slider = ctk.CTkSlider(master=self.settings_frame, from_=0, to=100,
                                                    number_of_steps=100, command=self.slider_event)
        self.password_lenght_slider.grid(row=1, column=0, pady=(0, 150), padx=(10, 10), sticky='ew')  # Слайдер занимает 3/4 пространства

        # Поле для отображения длины пароля
        self.password_lenght_entry = ctk.CTkEntry(master=self.settings_frame, width=50, height=35)
        self.password_lenght_entry.grid(row=1, column=1, padx=(10, 10), pady=(0, 150), sticky='we')  # Поле занимает оставшееся место

    def slider_event(self, value):
        # Вывод длины пароля в entry
        self.password_lenght_entry.delete(0, "end")
        self.password_lenght_entry.insert(0, str(int(value)))

    def set_password(self):
        # Генерация пароля
        pass


if __name__ == '__main__':
    app = App()
    app.mainloop()
