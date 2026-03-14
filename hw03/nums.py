import tkinter as tk
from tkinter import simpledialog, messagebox

root = tk.Tk()

root.withdraw()

nums = [x for x in range(1, 101)
    if x % 2 == 0]
messagebox.showinfo("결과", sum(nums))
#1부터 100까지 n의 배수 합 계산