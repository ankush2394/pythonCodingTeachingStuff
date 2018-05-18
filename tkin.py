from tkinter import *
from tkinter import messagebox
 
master = Tk()
global ans
master.configure(background='green')
def addition():
    
    #showerror()
    #showwarning()
    #showinfo()
    #messagebox.showinfo("Title", "Thank you for clicking +. Have a nice day!!")
    string1 = g.get()
    string2 = h.get()
    if len(string1) and len(string2):
        messagebox.showinfo("Addition", "Answer is "+ str(float(string1)+float(string2)))
        ans = float(string1)+float(string2)
        print("Addition is: ",float(string1)+float(string2))
    else:
        messagebox.showerror("Error","Check your inputs")

def subtraction():
    
    string1 = g.get()
    string2 = h.get()
    if len(string1) and len(string2):
        messagebox.showinfo("Subtraction", "Answer is "+str(float(string1)-float(string2)))
        ans = float(string1)-float(string2)
        print("Subtraction is: ",float(string1)-float(string2))
    else:
        messagebox.showerror("Error","Check your inputs")
    

def multiplication():
    
    string1 = g.get()
    string2 = h.get()
    if len(string1) and len(string2):
        messagebox.showinfo("Multiplication", "Answer is "+ str(float(string1)*float(string2)))
        ans = float(string1)*float(string2)
        print("Multiplication is: ",float(string1)*float(string2))
    else:
        messagebox.showerror("Error","Check your inputs")
    

def divide():
    
    string1 = g.get()
    string2 = h.get()
    if len(string1) and len(string2):
        messagebox.showinfo("Division", "Answer is "+ str( float(string1)/float(string2)))
        ans = float(string1)/float(string2) #// floor division
        print("Divison is: ",float(string1)/float(string2))
    else:
        messagebox.showerror("Error","Check your inputs")



master.title("Calculator")
master.geometry("500x500") #You want the size of the app to be 500x500
master.resizable(0, 0) #Don't allow resizing in the x or y direction

def clear():
    g.delete(0, END)
    h.delete(0, END)


# NOTE --- either we canuse all pack or all grid on one frame
    

g = Entry(master)
g.pack()
g.focus_set()
h = Entry(master)
h.pack()
h.focus_set()
b = Button(master, text="+", command=addition)
b.configure(background='yellow')
#.grid(row=1,column=2) is also a method used for placing thebtton at the desired position
b.pack()
c = Button(master, text="-", command=subtraction)
c.pack()
d = Button(master, text="*", command=multiplication)
d.pack()
e = Button(master, text="/", command=divide)
e.pack()
f = Button(master, text="AC", command=clear)
f.pack()



mainloop()
