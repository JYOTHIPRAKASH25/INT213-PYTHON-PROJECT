from tkinter import *
root = Tk()
root.geometry("200x200")
root.title("Student")
def Register():
    print("Successfully Registered")
    open()
Button(text="Login", command=Register).grid(row=1, column=5)
Button(text="New User", command=Register).grid(row=2, column=5)
Button(text="Request for Supervisor", command=Register).grid(row=3, column=5)
root.mainloop()
