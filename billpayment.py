import tkinter
from tkinter import *
from tkinter import ttk, messagebox

username = ("Tom")
password = ("")
usernameguess1 = ("")
passwordguess1 = ("")


#ignore the file writing part,I'll sort this out later.

file = open("userlogondata.txt", "w")
file.write("User Data:\n")

file = open("userlogondata.txt", "r")

def trylogin():
   print ("Trying to login...")
   if usernameguess == username:
       print ("Complete sucsessfull!")
       messagebox.showinfo("-- COMPLETE --", "You Have Now Logged In.",icon="info")
   else:
       print ("Error: (Incorrect value entered)")
       messagebox.showinfo("-- ERROR --", "Please enter valid infomation!", icon="warning")



#Gui Things
window = tkinter.Tk()
window.resizable(width=FALSE, height=FALSE)
window.title("Log-In")
window.geometry("200x150")
window.wm_iconbitmap("applicationlogo.ico")


#Creating the username & password entry boxes
usernametext = tkinter.Label(window, text="Username:")
usernameguess = tkinter.Entry(window)
passwordtext = tkinter.Label(window, text="Password:")
passwordguess = tkinter.Entry(window, show="*")

usernameguess1 = usernameguess




#attempt to login button
attemptlogin = tkinter.Button(text="Login", command=trylogin)



usernametext.pack()
usernameguess.pack()
passwordtext.pack()
passwordguess.pack()
attemptlogin.pack()
#Main Starter
window.mainloop()