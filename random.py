import tkinter as tk
from tkinter import ttk
import random


class App:

    def __init__(self, master):
        self.master = master
        self.master.title("Random Number Generator")
        self.master.resizable(True, True)

        self.font = ("arial", 11)

        self.create_gui()

    def create_gui(self):
        self.main_frame = tk.Frame(self.master)
        self.main_frame.grid(row=0, column=0)

        self.min_label = tk.Label(self.main_frame, text="min: ", font=self.font)
        self.min_label.grid(row=0, column=0)

        self.min_entry = ttk.Entry(self.main_frame)
        self.min_entry.grid(row=0, column=1, padx=5, pady=2)

        self.max_label = tk.Label(self.main_frame, text="max: ", font=self.font)
        self.max_label.grid(row=1, column=0)

        self.max_entry = ttk.Entry(self.main_frame)
        self.max_entry.grid(row=1, column=1, padx=5, pady=2)

        self.stepsize_label = tk.Label(self.main_frame,
                                       text="stepsize: ", font=self.font)
        self.stepsize_label.grid(row=2, column=0)

        self.stepsize_entry = ttk.Entry(self.main_frame, text="1")
        self.stepsize_entry.grid(row=2, column=1, padx=5, pady=2)

        self.generate_button = ttk.Button(self.main_frame, text="generate",
                                          command=lambda: self.generate_number())
        self.generate_button.grid(row=3, column=0)

        self.result_label = tk.Label(self.main_frame, text="result: ", font=self.font)
        self.result_label.grid(row=3, column=1)

    def generate_number(self):
        try:
            min_threshold = float(self.min_entry.get())
            max_threshold = float(self.max_entry.get())
            stepsize = float(self.stepsize_entry.get())
            random_number = random.randrange(min_threshold, max_threshold, stepsize)
            self.result_label.config(text="result: {}".format(random_number))
        except Exception as e:
            print(e)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
