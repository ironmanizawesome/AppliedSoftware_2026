import tkinter as tk
from tkinter import simpledialog, messagebox

root = tk.Tk()

root.withdraw()

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
#재귀호출 구조를 이용한 팩토리얼 계산
num = simpledialog.askinteger(title='팩토리얼계산기', 
                                    prompt= "숫자를 넣어주세요:")
messagebox.showinfo("결과", f"Factorial of {num} is {factorial(num)}")