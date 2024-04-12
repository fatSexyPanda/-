import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def button_add():
    global f_num
    global math
    math = "addition"
    f_num = float(entry.get())
    entry.delete(0, tk.END)

def button_subtract():
    global f_num
    global math
    math = "subtraction"
    f_num = float(entry.get())
    entry.delete(0, tk.END)

def button_multiply():
    global f_num
    global math
    math = "multiplication"
    f_num = float(entry.get())
    entry.delete(0, tk.END)

def button_divide():
    global f_num
    global math
    math = "division"
    f_num = float(entry.get())
    entry.delete(0, tk.END)

def button_equal():
    second_num = float(entry.get())
    entry.delete(0, tk.END)
    if math == "addition":
        result = f_num + second_num
    elif math == "subtraction":
        result = f_num - second_num
    elif math == "multiplication":
        result = f_num * second_num
    elif math == "division":
        result = f_num / second_num
    entry.insert(0, result)

def button_clear():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Калькулятор")

entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ("1", 1, 0), ("2", 1, 1), ("3", 1, 2),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2),
    ("7", 3, 0), ("8", 3, 1), ("9", 3, 2),
    ("0", 4, 1)
]

for button_text, row, column in buttons:
    button = tk.Button(root, text=button_text, padx=40, pady=20, command=lambda button_text=button_text: button_click(button_text))
    button.grid(row=row, column=column)

operations = [
    ("+", button_add, 1, 3), ("-", button_subtract, 2, 3),
    ("*", button_multiply, 3, 3), ("/", button_divide, 4, 3),
    ("=", button_equal, 4, 2), ("C", button_clear, 4, 0)
]

for operation_text, operation_func, row, column in operations:
    button = tk.Button(root, text=operation_text, padx=35, pady=20, command=operation_func)
    button.grid(row=row, column=column)

root.mainloop()
