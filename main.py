import tkinter
import customtkinter as CTk


class AppSettings(CTk.CTk):
    def __init__(self):
        super().__init__()

        # --- Window Settings --- #
        self.geometry("700x700")
        self.title("Calculation System Calculator")
        self.resizable(False, False)


class AppWidgets(AppSettings):
    def __init__(self):
        super().__init__()
        pass


if __name__ == '__main__':
    app = AppWidgets()
    app.mainloop()