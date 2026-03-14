import tkinter as tk
from tkinter import simpledialog, messagebox

root = tk.Tk()

root.withdraw()

def f2c(temp_f):
    return (temp_f - 32) * 5/9

temp_f = simpledialog.askfloat(title='온도변환기', 
                                    prompt= "숫자를 넣어주세요:")
messagebox.showinfo("결과", f"Temperature in Celsius: {f2c(temp_f):.2f}")