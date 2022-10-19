import tkinter as tk

class calculate:
  def __init__(self):
    self.main_calculate = tk.Tk()

    self.calc_frame = tk.Frame()
    self.button_frame = tk.Frame()
    self.output_frame = tk.Frame()

    self.calc_label = tk.Label(self.calc_frame, text='This is main calculator')