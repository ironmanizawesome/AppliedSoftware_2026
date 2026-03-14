import tkinter as tk
from tkinter import simpledialog, messagebox

root = tk.Tk()

root.withdraw()

def check_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

num = simpledialog.askinteger(title='소수판별기', 
                                    prompt= "숫자를 넣어주세요:")
if check_prime(num):
    messagebox.showinfo("결과", f"{num} is a prime number")
else:
    messagebox.showinfo("결과", f"{num} is not a prime number")
