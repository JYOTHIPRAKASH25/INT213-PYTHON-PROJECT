from tkinter import *
root = Tk()
root.geometry("300x200")
root.title("Student")
def Register():
    print("Successfully Registered")
    open()
Button(text="Login", command=Register).grid(row=1, column=6,pady=10)
Button(text="New User", command=Register).grid(row=2, column=6,pady=10)
Button(text="Open Hours", command=Register).grid(row=3, column=6,pady=10)
Button(text="Select Students", command=Register).grid(row=4, column=6,pady=10)
root.mainloop()