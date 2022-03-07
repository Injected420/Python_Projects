import tkinter as tk
# This is a good template for any Calcuation GUI, change the calcuation that is done and the text
# This example will output the results IN the same window/widget
class KiloconvertGUI:
    def __init__(self):
        self.main_window = tk.Tk()

        #Need 3 frames, one for input, one for buttons, one for output
        self.top_frame = tk.Frame()
        self.mid_frame = tk.Frame()
        self.bottom_frame = tk.Frame()

        #Widgets for Top Frame
        self.prompt_label = tk.Label(self.top_frame, text="Enter the distance in Kilometers")
        self.kilo_entry = tk.Entry(self.top_frame, width=10)

        #Pack top frame widgets
        self.prompt_label.pack(side='left')
        self.kilo_entry.pack(side='left')

        #Middle frame widgets
        self.des_label = tk.Label(self.mid_frame, text='Converted to Miles')

        #We need to use the StringVar() object to assoicate with the output, create a blank
        self.value = tk.StringVar()

        #Create a label and assoicate it with the StringVar, any object stored in StringVar will auto be displayed in the label
        self.miles_label = tk.Label(self.mid_frame, textvariable=self.value)

        #Pack the Middle Widgets
        self.des_label.pack(side='left')
        self.miles_label.pack(side='left')

        #Create button for widgets in bottom frame
        self.calc_button = tk.Button(self.bottom_frame, text='Convert', command=self.convert)
        self.quit_button = tk.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        #Pack the buttons
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        #Pack the Frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        #Mainloop
        tk.mainloop()

    #Define the convert function

    def convert(self):
        kilo = float(self.kilo_entry.get())
        miles = kilo * 0.6214
        self.value.set(format(miles, '.3f'))

conv_kilo = KiloconvertGUI()