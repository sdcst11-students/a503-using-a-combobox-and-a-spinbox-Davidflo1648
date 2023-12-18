"""
##### Task 1 Select birthdate.
Create an application that allows the user to select the month, day and year of their birthdate. You will need 3 separate entries: month,day, year.

You are responsible for designing your GUI.  You may use the pack, grid or place methods for doing so, but your GUI layout should be organized and visually appealing.

Display the results of their selection in an entry box in the widget.

Extra: Can you create some of the lists of values dynamically instead of explicitly listing them all?
"""
import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('User Application')
win.geometry('150x150')

res = tk.StringVar
res.set('Result')

def results():
    day = s1.get()
    month = c2.get()
    year = e3.get()
    res.set(f'{day}, {month}, {year}')

l0 = tk.Label(win,text='Enter your Birthdate')
l1 = tk.Label(win,text='Day')
s1 = ttk.Spinbox(win,values=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31',])
s1.set('Day')
l2 = tk.Label(win,text='Month')
c2 = ttk.Combobox(win,values=['January','February','March','April','May','June','July','August','September','October','November','December'])
c2.set('Month')
l3 = tk.Label(win,text='Year')
e3 = tk.Entry(win)
b1 = tk.Button(win,text='Resume',command=results)
result_l = tk.Label(win,text='All information')
result_e = tk.Entry(win, width=20, textvariable=res)

l0.grid(row=1,column=2)
l1.grid(row=3,column=1)
s1.grid(row=4,column=1)
l2.grid(row=3,column=2)
c2.grid(row=4,column=2)
l3.grid(row=3,column=3)
e3.grid(row=4,column=3)
b1.grid(row=6,column=2)
result_l(row=7,column=1)
result_e(row=7,column=2)

win.mainloop()