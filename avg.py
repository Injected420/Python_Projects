from select import select
import tkinter as tk
# This is a good template for any Calcuation GUI, change the calcuation that is done and the text
# This example will output the results IN the same window/widget


class AverageGUI:
    def __init__(self):
        self.main_window = tk.Tk()

        # Need 3 frames, one for input, one for buttons, one for output
        self.test1_frame = tk.Frame(self.main_window)
        self.test2_frame = tk.Frame(self.main_window)
        self.test3_frame = tk.Frame(self.main_window)
        self.avg_frame = tk.Frame(self.main_window)
        self.button_frame = tk.Frame(self.main_window)
        # Widgets for Top Frame
        self.test1_label = tk.Label(
            self.test1_frame, text='Enter the score for test 1: ')
        self.test1_entry = tk.Entry(self.test1_frame, width=15)
        self.test1_label.pack(side='left')
        self.test1_entry.pack(side='left')
        # Repeat for the 3 tests and the average frame
        self.test2_label = tk.Label(
            self.test2_frame, text='Enter the score for test 2: ')
        self.test2_entry = tk.Entry(self.test2_frame, width=15)
        self.test2_label.pack(side='left')
        self.test2_entry.pack(side='left')
        self.test3_label = tk.Label(
            self.test3_frame, text='Enter the score for test 3: ')
        self.test3_entry = tk.Entry(self.test3_frame, width=15)
        self.test3_label.pack(side='left')
        self.test3_entry.pack(side='left')
        self.result_label = tk.Label(self.avg_frame, text='Average: ')
        self.avg = tk.StringVar()
        self.avg_label = tk.Label(self.avg_frame, textvariable=self.avg)
        self.result_label.pack(side='left')
        self.avg_label.pack(side='left')
        self.calc_button = tk.Button(
            self.button_frame, text='Average', command=self.calc_avg)
        self.quit_button = tk.Button(
            self.button_frame, text='Quit', command=self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')
        # Pack
        self.test1_frame.pack()
        self.test2_frame.pack()
        self.test3_frame.pack()
        self.avg_frame.pack()
        self.button_frame.pack()

        # Mainloop
        tk.mainloop()

    def calc_avg(self):
        self.test1 = float(self.test1_entry.get())
        self.test2 = float(self.test2_entry.get())
        self.test3 = float(self.test3_entry.get())
        self.average = (self.test1 + self.test2 + self.test3) / 3.0
        self.avg.set(self.average)


show_avg = AverageGUI()
