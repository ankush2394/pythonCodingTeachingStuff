from tkinter import *
from tkinter import messagebox

master = Tk()
master.title("Tic Tac Toe")
##master.geometry("500x500")
click = True
def checker(buttons):
    global click
    if buttons["text"] == "" and click == True:
        buttons["text"]="X"
        click = False
        
    elif buttons["text"] == "" and click == False:
        buttons["text"]="O"
        click = True
        
    elif (button1["text"]=="X" and button2["text"]=="X" and button3["text"]=="X" or
         button4["text"]=="X" and button5["text"]=="X" and button6["text"]=="X" or
         button7["text"]=="X" and button8["text"]=="X" and button9["text"]=="X" or
         button3["text"]=="X" and button5["text"]=="X" and button7["text"]=="X" or
         button3["text"]=="X" and button6["text"]=="X" and button9["text"]=="X" or
         button2["text"]=="X" and button5["text"]=="X" and button8["text"]=="X" or
         button1["text"]=="X" and button5["text"]=="X" and button9["text"]=="X" or
         button1["text"]=="X" and button4["text"]=="X" and button7["text"]=="X"):
        messagebox.showinfo("Winner X","You have won the game")

    elif (button1["text"]=="O" and button2["text"]=="O" and button3["text"]=="O" or
         button4["text"]=="O" and button5["text"]=="O" and button6["text"]=="O" or
         button7["text"]=="O" and button8["text"]=="O" and button9["text"]=="O" or
         button3["text"]=="O" and button5["text"]=="O" and button7["text"]=="O" or
         button3["text"]=="O" and button6["text"]=="O" and button9["text"]=="O" or
         button2["text"]=="O" and button5["text"]=="O" and button8["text"]=="O" or
         button1["text"]=="O" and button5["text"]=="O" and button9["text"]=="O" or
         button1["text"]=="O" and button4["text"]=="O" and button7["text"]=="O"):
        messagebox.showinfo("Winner O","You have won the game")

 
         
        

buttons = StringVar()

button1 = Button(master,text="",command =
                 lambda:checker(button1))
button1.grid(row=0,column=0, sticky = N+S+E+W)

button2 = Button(master,text="",command =
                 lambda:checker(button2))
button2.grid(row=0,column=1, sticky = N+S+E+W)

button3 = Button(master,text="",command =
                 lambda:checker(button3))
button3.grid(row=0,column=2, sticky = N+S+E+W)

button4 = Button(master,text="",command =
                 lambda:checker(button4))
button4.grid(row=1,column=0, sticky = N+S+E+W)

button5 = Button(master,text="",command =
                 lambda:checker(button5))
button5.grid(row=1,column=1, sticky = N+S+E+W)

button6 = Button(master,text="",command =
                 lambda:checker(button6))
button6.grid(row=1,column=2, sticky = N+S+E+W)

button7 = Button(master,text="",command =
                 lambda:checker(button7))
button7.grid(row=2,column=0, sticky = N+S+E+W)

button8 = Button(master,text="",command =
                 lambda:checker(button8))
button8.grid(row=2,column=1, sticky = N+S+E+W)

button9 = Button(master,text="",command =
                 lambda:checker(button9))
button9.grid(row=2,column=2, sticky = N+S+E+W)



mainloop()
