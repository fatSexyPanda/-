import tkinter as tk

def showInput():
    input_text = entry.get()
    popup = tk.Toplevel()
    popup_label = tk.Label(popup, text=f"Привет {input_text}!")
    popup_label.pack()

root = tk.Tk()

entry = tk.Entry(root, width=50, bg="blue", fg="white", borderwidth=5)
entry.insert(0, "Введите ваше имя")
entry.pack()
button = tk.Button(root, text="Показать", command=showInput, bg="white", fg="blue")
button.pack()

root.mainloop()
