#!python3

"""
##### Task 2 Calculator
Create a simple app that allows you to do a calculation with an arithmetic operation.  You will need a spinbox between 2 entry boxes.  The entryboxes are where you should be entering your numbers, and the spinbox should be the operator.  You will need a button to do the calculation.  You can modify your assignment from A500 for this.
"""
import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Simple Calculator")

num1 = tk.Entry(win)
num1.grid(row=0, column=0)
num2 = tk.Entry(win)
num2.grid(row=0, column=2)

operator = ttk.Spinbox(win, values=["+", "-", "×", "÷"])
operator.grid(row=0, column=1)

result = tk.Label(win, text="Result: ")
result.grid(row=1, column=0, columnspan=3)

def calculate():
    n1 = float(num1.get())
    n2 = float(num2.get())
    op = operator.get()

    if op == "+":
        res = n1 + n2
    elif op == "-":
        res = n1 - n2
    elif op == "*":
        res = n1 * n2
    elif op == "/":
        res = n1 / n2

    result.config(text=f"Result: {res}")

button = tk.Button(win, text="Calculate", command=calculate)
button.grid(row=2, column=0, columnspan=3)

win.mainloop()
