import tkinter as tk
import customtkinter as CTk
import from_two
import from_eight
import from_ten
import from_sixteen

import get_result


class ConversionApp(CTk.CTk):
    def __init__(self):
        super().__init__()

        # --- Window Settings --- #
        self.geometry("500x250")
        self.title("Number Conversion")


class App(ConversionApp):
    def __init__(self):
        super().__init__()

        # --- RadioButtons Frame (From) --- #
        self.from_frame = CTk.CTkFrame(master=self)
        self.from_frame.grid(row=0, column=0, padx=10, pady=10)

        self.from_label = CTk.CTkLabel(master=self.from_frame, text="From:", font=("consolas", 12))
        self.from_label.grid(row=0, column=0, padx=5, pady=5)

        self.from_var = tk.StringVar()
        self.from_var.set("10")  # Default selection

        systems = ["2", "8", "10", "16"]
        self.from_radios = []

        for i, system in enumerate(systems):
            radio = CTk.CTkRadioButton(master=self.from_frame, text=system, font=("consolas", 12),
                                       variable=self.from_var, value=system)
            radio.grid(row=0, column=i + 1, padx=5, pady=5)
            self.from_radios.append(radio)

        # --- RadioButtons Frame (To) --- #
        self.to_frame = CTk.CTkFrame(master=self)
        self.to_frame.grid(row=1, column=0, padx=10, pady=10)

        self.to_label = CTk.CTkLabel(master=self.to_frame, text="To:", font=("consolas", 12))
        self.to_label.grid(row=0, column=0, padx=5, pady=5)

        self.to_var = tk.StringVar()
        self.to_var.set("10")  # Default selection

        self.to_radios = []

        for i, system in enumerate(systems):
            radio = CTk.CTkRadioButton(master=self.to_frame, text=system, font=("consolas", 12),
                                       variable=self.to_var, value=system)
            radio.grid(row=0, column=i + 1, padx=5, pady=5)
            self.to_radios.append(radio)

        # --- Result Frame --- #
        self.result_frame = CTk.CTkFrame(master=self)
        self.result_frame.grid(row=2, column=0, padx=10, pady=10)

        # - User Number - #
        self.user_number_label = CTk.CTkLabel(master=self.result_frame, text="Enter a number:", font=("consolas", 12))
        self.user_number_label.grid(row=0, column=0, padx=5, pady=5)

        self.user_number_entry = CTk.CTkEntry(master=self.result_frame, font=("consolas", 12))
        self.user_number_entry.grid(row=0, column=1, padx=5, pady=5)

        # - Convert Button - #
        self.convert_button = CTk.CTkButton(master=self.result_frame, text="Convert", font=("consolas", 12),
                                            command=self.convert)
        self.convert_button.grid(row=0, column=2, padx=5, pady=5)

        # - Output - #
        self.output_label = CTk.CTkLabel(master=self.result_frame, text="Result:", font=("consolas", 12))
        self.output_label.grid(row=1, column=0, padx=5, pady=5)

        self.result_var = tk.StringVar()
        self.result_entry = CTk.CTkEntry(master=self.result_frame, textvariable=self.result_var, font=("consolas", 12))
        self.result_entry.grid(row=1, column=1, padx=5, pady=5)

    def convert(self):
        result = [get_result.get_res(value_from=self.from_var.get(), value_to=self.to_var.get(),
                                     number=self.user_number_entry.get())]

        print(result)


if __name__ == '__main__':
    app = App()
    app.mainloop()
