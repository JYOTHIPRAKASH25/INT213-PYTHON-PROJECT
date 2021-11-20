from tkinter import *
root = Tk()
root.geometry("450x300")

def Login():
    print("Successfully logged in")
Label(root, text="Login Page", font="times 15 bold").grid(row=3,column=3)
UserName = Label(root, text="UserName")
UserName.grid(row=4, column=8,pady=10)
Password = Label(root, text="Password")
Password.grid(row=5, column=8,pady=10)


UserName = StringVar
Password = StringVar


UserName = Entry(root, text="Name")
UserName.grid(row=4, column=9)
Password = Entry(root, text="Password")
Password.grid(row=5, column=9)

checkBox = Checkbutton(text="Keep Me Logged In", variable="checkBox")
checkBox.grid(row=9, column=9)

Button(text="Login", command=Login).grid(row=12, column=9, pady=10)
Button(text="NewUser", command=Login).grid(row=13, column=9, pady=10)
root.mainloop()