from math import sqrt
from tkinter import *
window = Tk()
window.title("Calculator")
window.config(bg="#bae8e8")
# Entry Top
ent1 = Entry(window,width=60,borderwidth=5,bg="#e3f6f5")
ent1.grid(row=0,column=0,columnspan=5,padx=10,pady=10)

def addButton(num):
    return Button(window,padx=16,bd=6,text=num,bg="#e3f6f5",fg="#272343",width=4,command= lambda:clickButton(str(num)))

def createButton():
    # Number
    bttn0 = addButton(0)
    bttn1 = addButton(1)
    bttn2 = addButton(2)
    bttn3 = addButton(3)
    bttn4 = addButton(4)
    bttn5 = addButton(5)
    bttn6 = addButton(6)
    bttn7 = addButton(7)
    bttn8 = addButton(8)
    bttn9 = addButton(9)
    # Operators
    bttn_add=addButton('+')
    bttn_sub = addButton('-')
    bttn_mult = addButton('*')
    bttn_div = addButton('/')
    bttn_clear = addButton('C')
    bttn_equal = addButton('=')
    bttn_mod = addButton('%')
    bttn_verg = addButton('.')
    bttn_sqr= addButton('^')
    bttn_jadrM = addButton('sqrt')
    # Organiser Butts
    row1 = [bttn7,bttn8,bttn9,bttn_add,bttn_jadrM]
    row2 = [bttn4, bttn5, bttn6,bttn_sub,bttn_sqr]
    row3 = [bttn1, bttn2, bttn3,bttn_mult,bttn_mod]
    row4 = [bttn_clear, bttn0,bttn_verg,bttn_div,bttn_equal]
    r = 1
    for row in [row1,row2,row3,row4]:
        c=0
        for bttn in row:
            bttn.grid(row = r,column = c , columnspan = 1)
            c += 1
        r += 1
def clickButton(value):
    current_equal=str(ent1.get())
    if value == 'C':
        ent1.delete(-1,END)
    elif value == '=':
        answer = str(eval(current_equal))
        ent1.delete(-1,END)
        ent1.insert(0,answer)
    elif value == "^":
        x = "**"
        ent1.insert(END, x)
    elif value == "sqrt":
        x = sqrt(int(current_equal))
        ent1.delete(-1, END)
        ent1.insert(END, x)
    else:
        ent1.delete(0,END)
        ent1.insert(0,current_equal+value)
# Main
createButton()
window.mainloop()