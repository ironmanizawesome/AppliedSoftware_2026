import tkinter as tk
from tkinter import simpledialog ,messagebox

root = tk.Tk()

root.withdraw()

import tkinter as tk
from tkinter import simpledialog
root = tk.Tk()

root.withdraw()

UserInput= simpledialog.askinteger(title='숫자넣기', 
                                    prompt= "숫자를 넣어주세요:")

messagebox.showinfo("결과", UserInput)