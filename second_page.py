from tkinter import *
import pecent
import  Member
def hospital():

    def penter():
        pecent.patient()

    def hmember():
         Member.Member()

    
    wn=Toplevel()
    wn.title("Employee ateendence")
    wn.state('zoomed')
    wn.configure(bg="#babdcc",bd=10, relief=RIDGE)
    #frame 1
    f1=Frame(wn,bg="#babdcc",height="100",width="1513",bd=10, relief=RIDGE)
    f1.place(y=1,x=1)
    #Label 1 for Employee Ateendence Sheet
    L0=Label(f1,text="Mom Health Care Globle Hospital Management system",font=("Calibri",45),fg="white" ,bg="#babdcc")
    L0.place(y=0,x=75)
    f3=Frame(wn,bg="#babdcc",height="265",width="400",bd=10, relief=RIDGE)
    f3.place(y=102,x=1)
    img002=PhotoImage(file="C:\\Users\\adity\\Desktop\\doctor project\\docmemb.png")
    img2=Label(f3,image=img002)
    img2.place(height="245",width="380",x=0,y=0)
    f03=Frame(wn,bg="#babdcc",height="70",width="400",bd=10, relief=RIDGE)
    f03.place(y=367,x=1)
    L1=Label(f03,text="Hospital member ditail:",font=("Calibri",15),bg="#babdcc",fg="white")
    L1.place(y=5,x=5)
    f4=Frame(wn,bg="#babdcc",height="265",width="400",bd=10, relief=RIDGE)
    f4.place(y=437,x=1)
    img003=PhotoImage(file="C:\\Users\\adity\\Desktop\\doctor project\\pce3.png")
    img3=Label(f4,image=img003)
    img3.place(height="245",width="380",x=0,y=0)
    f04=Frame(wn,bg="#babdcc",height="70",width="400",bd=10, relief=RIDGE)
    f04.place(y=702,x=1)
    L2=Label(f04,text="Patient all  ditail:",font=("Calibri",15),bg="#babdcc",fg="white")
    L2.place(y=5,x=5)
    bt2=Button(f04,font=("Elephant",12),fg="white",bg="#babdcc", text="Enter" ,command=penter)
    bt2.place(y=5,x=250)
    bt3=Button(f03,font=("Elephant",12),fg="white",bg="#babdcc", text="Enter" ,command=hmember)
    bt3.place(y=5,x=250)
    f2=Frame(wn,bg="#babdcc",height="670",width="1113",bd=10, relief=RIDGE)
    f2.place(y=102,x=401)
    
    img001=PhotoImage(file="C:\\Users\\adity\\Desktop\\doctor project\\hospitl7.png")
    img1=Label(f2,image=img001)
    img1.place(height="650",width="1094",x=0,y=0)
    wn.mainloop()
# hospital()