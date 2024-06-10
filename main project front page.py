from tkinter import *
from tkinter import messagebox as mg
import test
def login():
    usn=e1.get()
    pas=e2.get()
    if(usn=="1" and pas=="1" ):
        test.login()
        
    else:
        mg.showinfo("username or password wrong","invalid username or password")
def clear():
    e1.delete(0,"end")
    e2.delete(0,"end")
    
    
wn=Tk()
wn.title("Employee ateendence")
wn.geometry("1530x791")
wn.configure(bg="lightskyblue",bd=10, relief=RIDGE)
#frame 1
f1=Frame(wn,bg="lightskyblue",height="100",width="1513",bd=10, relief=RIDGE)
f1.place(y=1,x=1)
#Label 1 for Employee Ateendence Sheet
L1=Label(f1,text="Employee Attendance Sheet",font=("Calibri",50),fg="royalblue" ,bg="lightskyblue")
L1.place(y=0,x=375)
#frame 2
f2=Frame(wn,bg="lightskyblue",height="670",width="566.5",bd=10, relief=RIDGE)
f2.place(y=102,x=1)
#1img use karna onty png
img001=PhotoImage(file="D:\\python all programs\\python gui\\F22.png")
img1=Label(f2,image=img001)
img1.place(height="650",width="547",x=0,y=0)

#frame3
f3=Frame(wn,bg="lightskyblue",height="150",width="398",bd=10, relief=RIDGE)
f3.place(y=102,x=568.5)
#1img use karna onty png
img0001=PhotoImage(file="D:\\python all programs\\python gui\\face2.png")
img02=Label(f3,image=img0001)
img02.place(height="130",width="378",x=-1,y=0)
f4=Frame(wn,bg="lightskyblue",height="289.5",width="398",bd=10, relief=RIDGE)
f4.place(y=253,x=569)
L1=Label(f4,text="Username:",font=("Calibri",15),bg="lightskyblue",fg="black")
L1.place(y=45,x=30)
e1=Entry(f4,font=("Calibri",15),fg="black",)
e1.place(y=45,x=150)
L2=Label(f4,text="Password:",font=("Calibri",15),bg="lightskyblue",fg="black")
L2.place(y=120,x=30)
e2=Entry(f4,font=("Calibri",15),fg="black",show="*")
e2.place(y=120,x=150)
bt1=Button(f4,font=("Elephant",13),fg="black",bg="lightskyblue", text="login" ,command=login)
bt1.place(y=190,x=240)
bt2=Button(f4,font=("Elephant",13),fg="black",bg="lightskyblue", text="clear" ,command=clear)
bt2.place(y=190,x=105)
#frame 5
f5=Frame(wn,bg="lightskyblue",height="228",width="398",bd=10, relief=RIDGE)
f5.place(y=544,x=568)
#1img use karna onty png
imga01=PhotoImage(file="D:\\python all programs\\python gui\\pt1.png")
imga1=Label(f5,image=imga01)
imga1.place(height="207.5",width="377.5",x=0,y=0)
#frame 6
f6=Frame(wn,bg="lightskyblue",height="670",width="547",bd=10, relief=RIDGE)
f6.place(y=102,x=966.5)
#1img use karna onty png
img01=PhotoImage(file="D:\\python all programs\\python gui\\F033.png")
img2=Label(f6,image=img01)
img2.place(height="650",width="527",x=0,y=0)
wn.mainloop()
