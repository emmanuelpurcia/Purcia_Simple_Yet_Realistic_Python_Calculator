# Hello! I call this program my "Simple Yet Fancy Python Calculator" 
# I chose to do this as my final project in our Programming Logic and Design Subject because I want to know
# How most programmers make a calculator using a software.
# This existing simple calculator project was made by a youtuber named "Parvat Computer Technology"

# pseudocode

# Import Tkinter
import tkinter
from tkinter import *
 
 # Displays the Layout of the Program
root = Tk()
root.title("My Simple Yet Fancy Python Calculator")
root.geometry("570x600+100+200")
root.resizable(False,False)
root.configure(bg="#17161b")

# Function that shows the button you click
label_result = Label(root,width = 25, height = 2, text = "", font = ("Comic Sans MS", 30))
label_result.pack() 

# Displays the Buttons on the 1st Row
Button(root,text="C", width = 5, height = 1, font = ("Comic Sans MS", 30, "bold"), bd = 1, fg = "#fff", bg = "#3697f5").place(x = 10, y = 100)
Button(root,text="/", width = 5, height = 1, font = ("Comic Sans MS", 30, "bold"), bd = 1, fg = "#fff", bg = "#2a2d36").place(x = 150, y = 100)
Button(root,text="%", width = 5, height = 1, font = ("Comic Sans MS", 30, "bold"), bd = 1, fg = "#fff", bg = "#2a2d36").place(x = 290, y = 100)
Button(root,text="*", width = 5, height = 1, font = ("Comic Sans MS", 30, "bold"), bd = 1, fg = "#fff", bg = "#2a2d36").place(x = 430, y = 100)

# Function to run the Program
root.mainloop()
