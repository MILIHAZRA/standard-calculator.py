import tkinter as tk
import math

# --- Logic Functions ---
def add_to_display(value):
    entry.insert(tk.END, value)

def clear_display():
    entry.delete(0, tk.END)

def calculate_result():
    try:
        # We replace the display symbols with Python math symbols before evaluating
        # 'mod' becomes '%' and '√' is handled by math.sqrt
        expression = entry.get().replace('×', '*').replace('÷', '/').replace('mod', '%')
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def calculate_root():
    try:
        val = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(math.sqrt(val)))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def calculate_percent():
    try:
        val = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(val / 100))
    except:
        entry.delete(0, tk.END)

# --- GUI Setup ---
root = tk.Tk()
root.title("Mili's Calculator")
root.configure(bg="black")
root.resizable(False, False)

# The Display Screen
entry = tk.Entry(root, font=("Arial", 30), bg="black", fg="white", 
                 borderwidth=0, justify="right", insertbackground="white")
entry.grid(row=0, column=0, columnspan=4, pady=30, padx=20)

# --- Button Definitions ---
# Structure: (Text, Row, Column, Color, Command)
# Orange: #FF9500 | Dark Grey: #333333 | Light Grey: #A5A5A5
buttons = [
    ('C', 1, 0, "#A5A5A5", clear_display), 
    ('√', 1, 1, "#A5A5A5", calculate_root),
    ('mod', 1, 2, "#A5A5A5", lambda: add_to_display('mod')), 
    ('÷', 1, 3, "#FF9500", lambda: add_to_display('÷')),
    
    ('7', 2, 0, "#333333", lambda: add_to_display('7')), 
    ('8', 2, 1, "#333333", lambda: add_to_display('8')),
    ('9', 2, 2, "#333333", lambda: add_to_display('9')), 
    ('×', 2, 3, "#FF9500", lambda: add_to_display('×')),
    
    ('4', 3, 0, "#333333", lambda: add_to_display('4')), 
    ('5', 3, 1, "#333333", lambda: add_to_display('5')),
    ('6', 3, 2, "#333333", lambda: add_to_display('6')), 
    ('-', 3, 3, "#FF9500", lambda: add_to_display('-')),
    
    ('1', 4, 0, "#333333", lambda: add_to_display('1')), 
    ('2', 4, 1, "#333333", lambda: add_to_display('2')),
    ('3', 4, 2, "#333333", lambda: add_to_display('3')), 
    ('+', 4, 3, "#FF9500", lambda: add_to_display('+')),
    
    ('0', 5, 0, "#333333", lambda: add_to_display('0')), 
    ('.', 5, 1, "#333333", lambda: add_to_display('.')),
    ('%', 5, 2, "#333333", calculate_percent), 
    ('=', 5, 3, "#FF9500", calculate_result),
]

# Create buttons using a loop to apply style
for (text, r, c, color, cmd) in buttons:
    tk.Button(root, text=text, width=5, height=2, 
              bg=color, fg="white", font=("Arial", 16, "bold"),
              bd=0, highlightthickness=0, command=cmd).grid(row=r, column=c, padx=5, pady=5)

import operator
def standard_calculator():
    op=input("enter the operation you wanna doing:+,-,*,/,root,percentage,mod")
    num1=float(input("enter the first number:"))
    num2=float(input("enter the second number:"))
    if op=='+':
        result=operator.add(num1,num2)
    elif op=='-':
        if num1<num2 :
           result=operator.sub(num2,num1)
        elif num2<num1:
            result=operator.sub(num1,num2)
    elif op=='*':
        result=operator.mul(num1,num2)
    elif op=='/':
        if num2 == 0:
            print("Error: Cannot divide by zero.")
            return
        result=operator.truediv(num1,num2)
    elif op=="root":
        if num2 == 0:
                 print("Error: Cannot divide by zero.")
                 return
        result=math.sqrt(num1)
    elif op=='percentage':
        if num2 == 0:
                 print("Error: Cannot divide by zero.")
                 return
        result=num1/num2*100
    elif op =='mod':
        if num2 == 0:
                 print("Error: Cannot divide by zero.")
                 return
        result=num1%num2
    else:
        print("invalid number")
        print("thank you, please try again later")
 def check_num(float_or_int):
    try:
        numbers=float(float_or_int)
        return True
    except :
        return False
if __name__ == "__main__":
    standard_calculator()   
root.mainloop()








