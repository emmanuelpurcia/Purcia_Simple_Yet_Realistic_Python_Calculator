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
root.geometry("570x630+200+300")
root.resizable(False,False)
root.configure(bg = "#17161b")

# Function that shows the label of the button the user is clicking
label_result = Label(root, width = 25, height = 2, text = "", font = ("Comic Sans MS", 30))
label_result.pack() 

# Displays the Buttons on the 1st Row of the Program
Button(root,text="C", width = 5, height = 1, font = ("Comic Sans MS", 30, "bold"), bd = 1, fg = "#fff", bg = "#fe9037").place(x = 10, y = 120)
Button(root,text="/", width = 5, height = 1, font = ("Comic Sans MS", 30, "bold"), bd = 1, fg = "#fff", bg = "#2a2d36").place(x = 150, y = 120)
Button(root,text="%", width = 5, height = 1, font = ("Comic Sans MS", 30, "bold"), bd = 1, fg = "#fff", bg = "#2a2d36").place(x = 290, y = 120)
Button(root,text="*", width = 5, height = 1, font = ("Comic Sans MS", 30, "bold"), bd = 1, fg = "#fff", bg = "#2a2d36").place(x = 430, y = 120)

# Displays the Buttons on the 2nd Row of the Program
Button(root,text="7", width = 5, height = 1, font = ("Comic Sans MS", 30, "bold"), bd = 1, fg = "#fff", bg = "#2a2d36").place(x = 10, y = 220)
Button(root,text="8", width = 5, height = 1, font = ("Comic Sans MS", 30, "bold"), bd = 1, fg = "#fff", bg = "#2a2d36").place(x = 150, y = 220)
Button(root,text="9", width = 5, height = 1, font = ("Comic Sans MS", 30, "bold"), bd = 1, fg = "#fff", bg = "#2a2d36").place(x = 290, y = 220)
Button(root,text="-", width = 5, height = 1, font = ("Comic Sans MS", 30, "bold"), bd = 1, fg = "#fff", bg = "#2a2d36").place(x = 430, y = 220)

# Displays the Buttons on the 3rd Row of the Program
Button(root,text="4", width = 5, height = 1, font = ("Comic Sans MS", 30, "bold"), bd = 1, fg = "#fff", bg = "#2a2d36").place(x = 10, y = 320)
Button(root,text="5", width = 5, height = 1, font = ("Comic Sans MS", 30, "bold"), bd = 1, fg = "#fff", bg = "#2a2d36").place(x = 150, y = 320)
Button(root,text="6", width = 5, height = 1, font = ("Comic Sans MS", 30, "bold"), bd = 1, fg = "#fff", bg = "#2a2d36").place(x = 290, y = 320)
Button(root,text="+", width = 5, height = 1, font = ("Comic Sans MS", 30, "bold"), bd = 1, fg = "#fff", bg = "#2a2d36").place(x = 430, y = 320)

# Displays the Buttons on the 4th and 5th Row of the Program
Button(root,text="1", width = 5, height = 1, font = ("Comic Sans MS", 30, "bold"), bd = 1, fg = "#fff", bg = "#2a2d36").place(x = 10, y = 420)
Button(root,text="2", width = 5, height = 1, font = ("Comic Sans MS", 30, "bold"), bd = 1, fg = "#fff", bg = "#2a2d36").place(x = 150, y = 420)
Button(root,text="3", width = 5, height = 1, font = ("Comic Sans MS", 30, "bold"), bd = 1, fg = "#fff", bg = "#2a2d36").place(x = 290, y = 420) 
Button(root,text="0", width = 11, height = 1, font = ("Comic Sans MS", 30, "bold"), bd = 1, fg = "#fff", bg = "#2a2d36").place(x = 10, y = 520)
Button(root,text=".", width = 5, height = 1, font = ("Comic Sans MS", 30, "bold"), bd = 1, fg = "#fff", bg = "#2a2d36").place(x = 290, y = 520)
Button(root,text="=", width = 5, height = 3, font = ("Comic Sans MS", 30, "bold"), bd = 1, fg = "#fff", bg = "#3697f5").place(x = 430, y = 420)

# Function to run the Program
root.mainloop()
