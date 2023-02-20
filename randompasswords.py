import random
import tkinter as tk
from tkinter import TclError, ttk

def generatePassword():
    lenghtOfPassw = password_lenght.get()
    password_input.delete(0, tk.END)
    symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    list_symbols = list(symbols)
    try:          
        for i in range(int(lenghtOfPassw)):
            password = random.choice(list_symbols)
            password_input.insert(0, password)
            old_password_input.insert(tk.END, password)
    except:
        old_password_input.insert(tk.END, "Only numbers!")
    old_password_input.insert(tk.END, "\n")
    pass

def exitApp():
    window.destroy()
    pass

def clearTextArea():
    old_password_input.delete("1.0", tk.END)
    pass

window = tk.Tk()
window.title("Random passwords by Darkzellos")
frameGeneral = tk.Frame(width=500, height=100, master=window)
frame = tk.Frame()
frameButton = ttk.Frame(padding=[0, 30])
frameExit = ttk.Frame(padding=[0, 20])
frameDown = tk.Frame()

#labelTop = tk.Label(text="Random password: ", font=("Montserrat", 15), master=frame)
labelLenghtPassw = tk.Label(text="Enter length of password", font=("Montserrat", 15), master=frameDown) #length of password
labelOldPass = tk.Label(text="Genereted passwords", font=("Montserrat", 15), master=frameGeneral)
password_lenght = tk.Entry(font=("Montserrat"), master=frameDown) #entry for length of password
password_input = tk.Entry(font=("Montserrat"), master=frame)
old_password_input = tk.Text(font=("Montserrat", 15), width=30, height=10, wrap="none", master=frameGeneral)
button_submit = tk.Button(text="Generate", font=("Montserrat"), height=2, width=10, bg="orange", command=generatePassword, master=frameButton)
button_clear = tk.Button(text="Clear", font=("Montserrat"), height=2, width=10, bg="Green", command=clearTextArea, master=frameExit)
button_exit = tk.Button(text="Exit", font=("Montserrat"), height=2, width=5, bg="Red", command=exitApp)

frame.pack()
frameDown.pack()
frameButton.pack()
frameGeneral.pack()
frameExit.pack()
#password_input.pack(side=tk.RIGHT)
#labelTop.pack(side=tk.RIGHT)
labelOldPass.pack()
old_password_input.pack()
labelLenghtPassw.pack()
password_lenght.pack()
button_submit.pack()
button_clear.pack()
button_exit.pack(side=tk.RIGHT)

window.mainloop()