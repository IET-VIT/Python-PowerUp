import tkinter as tk
from tkinter import filedialog, Text

def open_file():
    filename = filedialog.askopenfilename()
    if filename:
        with open(filename, 'r') as f:
            content = f.read()
            root.text_widget.delete('1.0', "end")
            root.text_widget.insert('1.0', content)

def save_file():
    filename = filedialog.asksaveasfilename()
    if filename:
        with open(filename, 'w') as f:
            f.write(root.text_widget.get('1.0', 'end'))

def new_file():
    root.text_widget.delete('1.0', "end")

root = tk.Tk()

root.title("Notepad")
root.geometry("600x400")

menubar = tk.Menu()
file_menu = tk.Menu(menubar)

file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Exit", command=root.quit)

root.config(menu=file_menu)

root.text_widget = Text(root)
root.text_widget.pack(expand=True, fill='both')

root.mainloop()