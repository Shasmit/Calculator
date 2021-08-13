from tkinter import *
from tkinter import messagebox

""" A Python project to create a simple calculator GUI using tkinter"""

#creating a window
root = Tk()
root.title("My Calculator")
root.iconbitmap('cal.ico')
#added an image in the background
pho=PhotoImage(file="cool.png")
lab=Label(root,image=pho)
lab.pack()

#set the max and min size of window with min max method
root.maxsize(width=263,height=245)
root.minsize(width=263,height=245)

#creating a entry widget
equation = StringVar()
e=Entry(root,width=29,borderwidth=8,font=("Comic Sans MS",10,'bold'),bg="light gray",fg="red",textvariable=equation)
e.place(x=5,y=5)


def info():
    messagebox.showinfo("Operators info",
                        """
    Addition(+) : Adds the numbers
    Substraction(-) : Substracts the numbers
    Multiplication(*) : Multiplies the numbers
    Division(/) : Divides the numbers
    Clear(C) : Clears the screen
    Equals(=) : Shows the result of the performed operation """)


def about():
    messagebox.showinfo("About My Calculator",
                        "This is a simple calculator GUI developed using Tkinter\n BY : Shasmit Basnet")

#creating menu bar
mine_menu = Menu(root)
root.config(menu=mine_menu)

# Info menu with operators info option
menu11 = Menu(mine_menu,bg="light gray",tearoff=0)
mine_menu.add_cascade(label="INFO",menu=menu11)
menu11.add_command(label="Operators info",font=("Comic Sans MS",8,'bold'), command=info)

#about menu with about my calculator option
menu2 = Menu(mine_menu,bg="light gray", tearoff=0)
mine_menu.add_cascade(label="ABOUT",menu=menu2)
menu2.add_command(label="About my calculator",font=("Comic Sans MS",8,'bold'), command=about)


#defining operator functions
def button_click(number):
    num = e.get()
    e.delete(0, END)
    e.insert(0, str(num) + str(number))


def button_clear():
    e.delete(0, END)



def button_equal():
    try:
        x = e.get()
        tot = eval(x)
        e.delete(0, END)
        e.insert(0, tot)

    except:
        e.delete(0, END)
        e.insert(0, "Error")
        messagebox.showerror("Error", "Please perform valid calculations")

# creating buttons
b7=Button(root,text="7",width=6,height=2,borderwidth=4,font=("Comic Sans MS",8,'bold'),bg="khaki",fg="black",command=lambda : button_click(7))
b8=Button(root,text="8",width=6,height=2,borderwidth=4,font=("Comic Sans MS",8,'bold'),bg="khaki",fg="black",command=lambda : button_click(8))
b9=Button(root,text="9",width=6,height=2,borderwidth=4,font=("Comic Sans MS",8,'bold'),bg="khaki",fg="black",command=lambda : button_click(9))
div=Button(root,text="/",width=6,height=2,borderwidth=4,font=("Comic Sans MS",8,'bold'),bg="khaki",fg="deep pink",command=lambda : button_click("/"))

b6=Button(root,text="6",width=6,height=2,borderwidth=4,font=("Comic Sans MS",8,'bold'),bg="khaki",fg="black",command=lambda : button_click(6))
b5=Button(root,text="5",width=6,height=2,borderwidth=4,font=("Comic Sans MS",8,'bold'),bg="khaki",fg="black",command=lambda : button_click(5))
b4=Button(root,text="4",width=6,height=2,borderwidth=4,font=("Comic Sans MS",8,'bold'),bg="khaki",fg="black",command=lambda : button_click(4))
mul=Button(root,text="*",width=6,height=2,borderwidth=4,font=("Comic Sans MS",8,'bold'),bg="khaki",fg="navy",command=lambda : button_click("*"))

b1=Button(root,text="1",width=6,height=2,borderwidth=4,font=("Comic Sans MS",8,'bold'),bg="khaki",fg="black",command=lambda : button_click(1))
b2=Button(root,text="2",width=6,height=2,borderwidth=4,font=("Comic Sans MS",8,'bold'),bg="khaki",fg="black",command=lambda : button_click(2))
b3=Button(root,text="3",width=6,height=2,borderwidth=4,font=("Comic Sans MS",8,'bold'),bg="khaki",fg="black",command=lambda : button_click(3))
button_clear=Button(root,text="C",width=6,height=2,borderwidth=4,font=("Comic Sans MS",8,'bold'),bg="khaki",fg="red2",command=button_clear)

add=Button(root,text="+",width=6,height=2,borderwidth=4,font=("Comic Sans MS",8,'bold'),bg="khaki",fg="purple",command=lambda : button_click("+"))
b0=Button(root,text="0",width=6,height=2,borderwidth=4,font=("Comic Sans MS",8,'bold'),bg="khaki",fg="black",command=lambda : button_click(0))
sub=Button(root,text="-",width=6,height=2,borderwidth=4,font=("Comic Sans MS",8,'bold'),bg="khaki",fg="deep sky blue",command=lambda : button_click("-"))
button_equal=Button(root,text="=",width=6,height=2,borderwidth=4,font=("Comic Sans MS",8,'bold'),bg="khaki",fg="red",command=button_equal)


b7.place(x=20,y=45)
b8.place(x=75,y=45)
b9.place(x=130,y=45)
div.place(x=185,y=45)


b6.place(x=20,y=90)
b5.place(x=75,y=90)
b4.place(x=130,y=90)
mul.place(x=185,y=90)

b1.place(x=20,y=135)
b2.place(x=75,y=135)
b3.place(x=130,y=135)
button_clear.place(x=185,y=135)

add.place(x=20,y=180)
b0.place(x=75,y=180)
sub.place(x=130,y=180)
button_equal.place(x=185,y=180)

root.mainloop()


