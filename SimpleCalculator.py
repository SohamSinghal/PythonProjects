from tkinter import *
window = Tk() #inititalize object named window
window.title("Simple Calculator")
window.resizable(0,0) #makes the Calculator window non-resizable
e = Entry(window)
e.grid(row = 0,columnspan = 4)

def button_click(number):
  current = e.get() #keeps whats in the entry bar
  e.delete(0,END) #deletes what's in the entry bar
  e.insert(0,str(current)+str(number)) #adds the new number 
def clear():
  e.delete(0,END) #deletes ecerything from the start to finish
def add():
  global fnum,action
  action = "add"
  fnum = float(e.get())
  e.delete(0,END) 
def subtract():
  global fnum,action
  action = "subtract"
  fnum = float(e.get())
  e.delete(0,END) 
def multiply():
  global fnum,action
  action = "multiply"
  fnum = float(e.get())
  e.delete(0,END) 
def divide():
  global fnum,action
  action = "divide"
  fnum = float(e.get())
  e.delete(0,END) 
def equals():
  snum =float(e.get())
  e.delete(0,END)
  if action == "add":
    e.insert(0,fnum+snum)
  elif action == "subtract":
    e.insert(0,fnum-snum)
  elif action == "multiply":
    e.insert(0,fnum*snum)
  else:
    e.insert(0,fnum/snum)

button_1 = Button(window,padx =40, pady = 20,text = "1",command = lambda:button_click(1))
button_2 = Button(window,padx =40,pady = 20, text = "2",command = lambda:button_click(2))
button_3 = Button(window,padx =40,pady = 20, text = "3",command = lambda:button_click(3))
button_4 = Button(window,padx =40,pady = 20, text = "4",command = lambda:button_click(4))
button_5 = Button(window,padx =40,pady = 20, text = "5",command = lambda:button_click(5))
button_6 = Button(window,padx =40,pady = 20, text = "6",command = lambda:button_click(6))
button_7 = Button(window,padx =40,pady = 20, text = "7",command = lambda:button_click(7))
button_8 = Button(window,padx =40,pady = 20, text = "8",command = lambda:button_click(8))
button_9 = Button(window,padx =40,pady = 20, text = "9",command = lambda:button_click(9))
button_0 = Button(window,padx =40,pady = 20, text = "0",command = lambda:button_click(0))
button_plus = Button(window,padx =40,pady = 20, text = "+",command = add)
button_subtract = Button(window,text = "-",padx = 40,pady = 20,command = subtract)
button_divide = Button(window,text = chr(247),padx = 40,pady = 20,command = divide)
button_multiply = Button(window,text = "x",padx = 40,pady = 20,command = multiply)
button_clear = Button(window,padx = 22,pady = 20,text = "CLEAR",command = clear)
button_equal = Button(window,text = "=",padx = 40,pady = 20,command = equals)
#7 8 9 /
button_7.grid(row = 1,column = 0)
button_8.grid(row = 1,column = 1)
button_9.grid(row = 1,column = 2)
button_divide.grid(row = 1,column = 3)
#4 5 6 x
button_4.grid(row = 2,column = 0)
button_5.grid(row = 2,column = 1)
button_6.grid(row = 2,column = 2)
button_multiply.grid(row = 2,column = 3)
#1 2 3 -
button_1.grid(row = 3,column = 0)
button_2.grid(row = 3,column = 1)
button_3.grid(row = 3,column = 2)
button_plus.grid(row = 3,column = 3)
#clear 0 = -
button_clear.grid(row = 4,column = 0)
button_0.grid(row = 4,column = 1)
button_equal.grid(row = 4,column = 2)
button_subtract.grid(row = 4,column = 3)





window.mainloop()
