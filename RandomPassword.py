import random
import string
import tkinter as tk
from tkinter import messagebox
from tkinter import *

window = Tk()
window.geometry('300x120')
window["bg"] = "#FFE5B4"
window.title('Random Password Generator')
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=0)
window.columnconfigure(2, weight=1)

def password():
    all_chars = string.ascii_letters + string.digits + string.punctuation
    all_chars = list(all_chars)
    
    weights = [4 if char in string.ascii_letters else 2 if char in string.digits else 1 for char in all_chars]
    
    password_list = random.choices(all_chars, weights = weights, k = 13)
    
    password_final = ""
    for char in password_list:
        password_final = password_final + char

    label = Label(master = window, text = password_final, bg = "white")
    label.grid(row=1, column=1, padx = 20, pady = 20)

btn = Button(master = window, text = "Generate Password?", fg = "white", bg = "blue", command = password)
btn.grid(row=0, column=1, padx = 20, pady = 10)

window.mainloop()