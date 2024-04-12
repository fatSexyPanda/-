import tkinter as tk

def myClick():
    label.config(text="Нажата кнопка!")

#главное окно
root = tk.Tk()

# кнопка
button = tk.Button(root, text="Нажми меня!", command=myClick, bg="white", fg="blue")

button.pack()

# надпись
label = tk.Label(root, text="")
label.pack()

# цикл обработки
root.mainloop()
