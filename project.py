from tkinter import *
root = Tk()
root.geometry("500x300")

def getVals():
    print("Accepted")

# Heading
Label(root, text="Python Registration Form", font="arial 15 bold").grid(row=0, column=3)

# Declaring the labels
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency")
paymentmood = Label(root, text="Payment Mood")

# Displaying Labels on the form
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentmood.grid(row=5, column=2)

nameValue = StringVar
phoneValue = StringVar
genderValue = StringVar
emergencyValue = StringVar
paymentmoodValue = StringVar
checkValue = IntVar

nameEntry = Entry(root, textvariable=nameValue)
phoneEntry = Entry(root, textvariable=phoneValue)
genderEntry = Entry(root, textvariable=genderValue)
paymentmoodEntry = Entry(root, textvariable=paymentmoodValue)
emergencyEntry = Entry(root, textvariable=emergencyValue)

nameEntry.grid(row=1,column=3)
phoneEntry.grid(row=2,column=3)
genderEntry.grid(row=3,column=3)
emergencyEntry.grid(row=4,column=3)
paymentmoodEntry.grid(row=5,column=3)

# Creating Checkbox
checkBtn = Checkbutton(text="remember me?", variable=checkValue)
checkBtn.grid(row=6, column=3)

# Submit button
Button(text="Submit", command=getVals).grid(row=7, column=3)

root.mainloop()