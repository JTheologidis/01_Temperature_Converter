from tkinter import *
import random



class Converter: 
    def __init__(self, parent):
        
        # Formatting variables
        background_color = "#d19fe8"    # light purple

        # Converter Frame
        self.converter_frame = Frame(width=240, bg=background_color,
                                     pady=10)
        self.converter_frame.grid()

        # Temperature Converter Heading (row 0)
        self.temp_heading_label = Label(self.converter_frame,
                                        text="Temperature Converter",
                                          font="Georgia 18 bold",
                                          bg=background_color,
                                          padx=10, pady=10)

        # User Instructions (row 1)
        self.temp_instructions_label = Label(self.converter_frame,
                                             text="Type in the amount to be "
                                                  "converted and then push "
                                                  "one of the buttons below...",
                                          font="Arial 10 italic", wrap=250,
                                          justify=LEFT, bg=background_color,
                                          padx=10, pady=10)
        self.temp_instructions_label.grid(row=1)

        # Temperature entry box (row 2)
        self.to_convert_entry = Entry(self.converter_frame, width=18,
                                      font="Arial 14 bold")
        self.to_convert_entry.grid(row=2)

        # Conversion buttons frame (row 3), indianred1 | springgreen2
        self.conversion_buttons_frame = Frame(self.converter_frame)
        self.conversion_buttons_frame.grid(row=3, pady=10)

        self.to_c_button = Button(self.conversion_buttons_frame,
                                  text="To Centrigrade", font="Arial 10 bold",
                                  bg="Indianred1", padx=10, pady=10)
        self.to_c_button.grid(row=0, column=0)

        self.to_f_button = Button(self.conversion_buttons_frame,
                                  text="To Fahrenheit", font="Arial 10 bold",
                                  bg="springgreen2", padx=10, pady=10)
        self.to_f_button.grid(row=0, column=1)
        
        # Answer label (row 4)

        # History / Help button frame (row 5)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()
