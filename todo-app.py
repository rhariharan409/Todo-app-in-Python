# importing tkinter
from tkinter import *

# creating a obj root for class Tk
root = Tk()
root.geometry("400x400")


# getting user input for string type
inputvar = StringVar()

# creating a insert function
def insert():
    task = inputvar.get()
    if task:
        lb.insert(END, task) # inserting at the end
        inputvar.set("")  # Clear input after adding

# creating a delete function to delete the elements
def delete():
    # ANCHOR method play the given role in the selected element
    lb.delete(ANCHOR)

# creating a Label
Label(root,text="TO DO LIST",width=50).pack()

# creating a listbox
lb = Listbox(root,width=50,height=10)

Entry(root, textvariable=inputvar).pack()
# creating button for insert and delete
ib = Button(root,text="insert",command=insert)
db = Button(root,text="delete",command=delete)

# packing process
lb.pack()
ib.pack()
db.pack()


root.mainloop()
