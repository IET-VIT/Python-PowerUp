import tkinter as tk
from tkinter import filedialog, Text, messagebox

def Encrypt():
    fname = filedialog.askopenfilename()
    if fname:
        f = open(fname, "r")
        content = f.read()
        f.close()

        key = int(key_var.get())

        encrypt = ""

        for ch in content:
            if ch.islower():
                encrypt += chr(ord('a')+((ord(ch)+key-ord('a'))%26))
            elif ch.isupper():
                encrypt += chr(ord('A')+((ord(ch)+key-ord('A'))%26))
            elif ch.isdigit():
                encrypt += str((int(ch)+key)%10)
            else:
                encrypt += ch

        with open(fname, "w") as f:
            f.write(encrypt)

        messagebox.showinfo("Success!", "Your file hase been successfully encrypted now.") 

def Decrypt():
    fname = filedialog.askopenfilename() 
    if fname:   
        f = open(fname, "r")
        content = f.read()

        key = int(key_var.get())

        decrypt = ""

        for ch in content:
            if ch.islower():
                decrypt += chr(ord('a')+((ord(ch)-key-ord('a'))%26))
            elif ch.isupper():
                decrypt += chr(ord('A')+((ord(ch)-key-ord('A'))%26))
            elif ch.isdigit():
                decrypt += str((10+int(ch)-key)%10)
            else:
                decrypt += ch

        with open(fname, "w") as f:
            f.write(decrypt)
        
        messagebox.showinfo("Success!", "Your file hase been successfully decrypted now.") 


root = tk.Tk()
root.title("Encryptor & Decryptor")
root.geometry("600x400")

key_var=tk.StringVar()
key_label = tk.Label(root, text="Enter the key : ")
key_entry = tk.Entry(root,textvariable = key_var)
enc_btn = tk.Button(root, text="Encrypt", command=Encrypt)
dec_btn = tk.Button(root, text="Decrypt", command=Decrypt)

key_label.grid(row=0, column=0)
key_entry.grid(row=0, column=1)
enc_btn.grid(row=1, column=0)
dec_btn.grid(row=1, column=1)

root.mainloop()