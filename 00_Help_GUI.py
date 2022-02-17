from tkinter import *
from functools import partial    # To prevent unwanted windows

import random

class Converter: 
    def __init__(self, parent):
        print("hello world")

        # Formatting variables...
        background_color = "red"

        # Converter Main Screen GUI...
        self.converter_frame = Frame(width=600, height=600, bg=background_color,
                                     pady=10)
        self.converter_frame.grid()

        # Temperature Conversion Heading (rov 0)
        self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter",
                                          font=("Georgia", "18", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        # Help Button (row 1)
        self.help_button = Button (self.converter_frame, text="help", 
                                   font= ("Arial", "14"),
                                   padx=10, pady=10, command=self.help)
        self.help_button.grid(row=1)
        
    def help(self):
        print("you asked for help")
        get_help = Help(self)
        get_help.help_text.configure(text="Help text goes here")

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()
