import tkinter as tk

root = tk.Tk()

label1 = tk.Label(root, text="Hello World!")
label2 = tk.Label(root, text="Меня зовут Имя Фамилия")

label1.grid(row=0, column=0)
label2.grid(row=1, column=0)

root.mainloop()
