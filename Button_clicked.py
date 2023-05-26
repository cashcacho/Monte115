#importing tkinter as tk
import tkinter as tk

#define function and print the words "Button Clicked" 
def button_click ():
    print("Button clicked")


#create root window and widjet object
root = tk.Tk()
root.title("Button Example")

#Create a button that pops out with the words "Click Me!"
button = tk.Button(root,text="Click Me!", command=button_click)
button.pack()

#Create loop to keep window open
root.mainloop()