import tkinter as tk
from tkinter import simpledialog, messagebox

root = tk.Tk()

root.withdraw()
def check_even(n): 
    if num % 2 == 0:
        return True
    return False

num = simpledialog.askinteger(title='홀짝판별기', 
                                    prompt= "숫자를 넣어주세요:")

if check_even(num):
    messagebox.showinfo("결과", f"{num} is Even")
else:
    messagebox.showinfo("결과", f"{num} is Odd")
