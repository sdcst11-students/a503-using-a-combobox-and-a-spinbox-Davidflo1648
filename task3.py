#!python3

"""
##### Task 3 tKinter Compound Interest 
Create an application to calculate the final value of a compount interest value problem.  Recall that the final value can be calculated with:

A = P(1+r/n)^(n*t) where:
P = Principal (amount of the initial investment)
r = Interest rate as a decimal (4% has r = 0.04)
n = Number of compounding periods in a year (monthly n = 12, daily n=365)
t = number of years

You should decide which values should have regular entry widgets, comboboxes or spinboxes.  You will need a label or entry box to show your result.
"""
# Import tkinter module
import tkinter as tk

# Create a root window
root = tk.Tk()
root.title("Compound Interest Calculator")

# Create labels for the input values
tk.Label(root, text="P = Principal").grid(row=0, column=0, padx=10, pady=10)
tk.Label(root, text="r = Interest rate").grid(row=1, column=0, padx=10, pady=10)
tk.Label(root, text="n = Compounding periods").grid(row=2, column=0, padx=10, pady=10)
tk.Label(root, text="t = Years").grid(row=3, column=0, padx=10, pady=10)

A = tk.Label(root, text="A = Final value")
A.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

P = tk.Entry(root)
P.grid(row=0, column=1, padx=10, pady=10)
r = tk.Entry(root)
r.grid(row=1, column=1, padx=10, pady=10)
n = tk.Entry(root)
n.grid(row=2, column=1, padx=10, pady=10)
t = tk.Entry(root)
t.grid(row=3, column=1, padx=10, pady=10)

def calculate():
    global P, r, n, t
    p = float(P.get())
    r = float(r.get())
    n = float(n.get())
    t = float(t.get())

    a = p * (1 + r / n) ** (n * t)

    A.config(text=f"A = {a:.2f}")

button = tk.Button(root, text="Calculate", command=calculate)
button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
