from tkinter import *
root = Tk()
root.geometry("500x300")

def Register():
    print("Successfully Registered")
Label(root, text="New User Student Registration", font="times 15 bold").grid(row=2,column=3)
Name = Label(root, text="Name")
Name.grid(row=4, column=2,pady=10)
RegistrationNumber = Label(root, text="RegistrationNumber")
RegistrationNumber.grid(row=5, column=2,pady=10)
Specialization = Label(root, text="Specialization")
Specialization.grid(row=6, column=2,pady=10)
MobileNo = Label(root, text="MobileNo")
MobileNo.grid(row=7, column=2,pady=10)
Emailid = Label(root, text="Emailid")
Emailid.grid(row=8, column=2,pady=10)

Name = StringVar
RegistrationNumber = StringVar
specialization = StringVar
MobileNo = StringVar
Emailid = StringVar
checkBox = IntVar

Name = Entry(root, text="Name")
Name.grid(row=4, column=3)
RegistrationNumber = Entry(root, text="RegistrationNumber")
RegistrationNumber.grid(row=5, column=3)
Specialization = Entry(root, text="Specialization")
Specialization.grid(row=6, column=3)
MobileNo = Entry(root, text="MobileNo")
MobileNo.grid(row=7, column=3)
Emailid = Entry(root, text="Emailid")
Emailid.grid(row=8, column=3)

checkBox = Checkbutton(text="Agree to Terms & Conditions", variable="checkBox")
checkBox.grid(row=9, column=3)

Button(text="Register", command=Register).grid(row=12, column=3)
root.mainloop()
