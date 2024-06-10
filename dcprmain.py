import csv
from tkinter import *
from tkinter import messagebox as mg
import hos1
def login():
    usn=e1.get()
    pas=e2.get()
    if(usn=="Aditya" and pas=="3011"):
        hos1.hospital()
    else:
         mg.showinfo('user&password',' user or psasword wrong')
def clear():
    e1.delete(0,"end")
    e2.delete(0,"end")
wn=Tk()
wn.title("Employee ateendence")
wn.state('zoomed')
wn.configure(bg="#babdcc",bd=10, relief=RIDGE)
#frame 1
f1=Frame(wn,bg="#babdcc",height="100",width="1513",bd=10, relief=RIDGE)
f1.place(y=1,x=1)
#Label 1 for Employee Ateendence Sheet
L0=Label(f1,text="Mom Health Care Globle Hospital",font=("Calibri",50),fg="white" ,bg="#babdcc")
L0.place(y=0,x=275)
 #frame 2
f2=Frame(wn,bg="#babdcc",height="670",width="1113",bd=10, relief=RIDGE)
f2.place(y=102,x=1)
img001=PhotoImage(file="C:\\Users\\adity\\Desktop\\doctor project\\doct2.png")
img1=Label(f2,image=img001)
img1.place(height="650",width="1094",x=0,y=0)

f3=Frame(wn,bg="#babdcc",height="670",width="400",bd=10, relief=RIDGE)
f3.place(y=102,x=1115)
L1=Label(f3,text="Username:",font=("Calibri",15),bg="#babdcc",fg="white")
L1.place(y=45,x=30)
e1=Entry(f3,font=("Calibri",15),fg="#babdcc")
e1.place(y=45,x=150)
L2=Label(f3,text="Password:",font=("Calibri",15),bg="#babdcc",fg="white")
L2.place(y=120,x=30)
e2=Entry(f3,font=("Calibri",15),fg="#babdcc",show="*")
e2.place(y=120,x=150)
bt1=Button(f3,font=("Elephant",13),fg="white",bg="#babdcc", text="Submit" ,command=login)
bt1.place(y=190,x=180)
bt2=Button(f3,font=("Elephant",13),fg="white",bg="#babdcc", text="Clear" ,command=clear)
bt2.place(y=190,x=90)
L3=Label(f3,text="Notice:-",font=("Calibri",18,'bold'),bg="#babdcc",fg="white")
L3.place(y=260,x=30)
L4=Label(f3,text="i)-Specialty Hospitals.",font=("Calibri",15),bg="#babdcc",fg="white")
L4.place(y=300,x=100)
L5=Label(f3,text="ii)-General Medical & Surgical\nHospitals.",font=("Calibri",15),bg="#babdcc",fg="white")
L5.place(y=340,x=100)
L6=Label(f3,text="iii)-Teaching Hospitals.",font=("Calibri",15),bg="#babdcc",fg="white")
L6.place(y=400,x=100)
L7=Label(f3,text="iv)-Hospices & Palliative Care \nCenters.",font=("Calibri",15),bg="#babdcc",fg="white") 
L7.place(y=440,x=100)
L8=Label(f3,text="v)-Clinics for Family Planning \nand Abortion.",font=("Calibri",15),bg="#babdcc",fg="white") 
L8.place(y=500,x=100)
L8=Label(f3,text="thanks for read.....",font=("Calibri",15,"bold"),bg="#babdcc",fg="white") 
L8.place(y=560,x=200)
wn.mainloop()