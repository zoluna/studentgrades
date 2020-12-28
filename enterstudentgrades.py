import sqlite3
from tkinter import *

def add_entry():
    newName = namebox.get()
    newGrade = gradebox.get()
    cursor.execute("""INSERT INTO studentgrades(name,grade)
        VALUES(?,?)""",(newName,newGrade))
    db.commit()
    db.close()

def clear_entry():
    namebox.delete(0, END)
    gradebox.delete(0, END)
    namebox.focus()
    gradebox.focus()

window = Tk()
window.title("Test scores")
window.geometry("600x250")

with sqlite3.connect("studentgrades.db") as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS studentgrades(
    name text PRIMARY KEY,
    grade text);""")

label1 = Label(text = "Enter student's name: ")
label1.place(x = 30, y = 20, width = 150, height = 25)
label2 = Label(text = "Enter student's grade: ")
label2.place(x = 30, y = 80, width = 150, height = 25)
addbutton = Button(text = "Add", command = add_entry)
addbutton.place(x = 40, y = 120, width = 40)
clearbutton = Button(text = "Clear", command = clear_entry)
clearbutton.place(x = 100, y = 120, width = 40)
namebox = Entry(text = "")
namebox.place(x = 180, y = 25, width = 100, height = 20)
gradebox = Entry(text = "")
gradebox.place(x = 180, y = 85, width = 100, height = 20)

window.mainloop()




