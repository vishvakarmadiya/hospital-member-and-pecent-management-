from tkinter import *
from tkinter import ttk
import csv
import re
def patient():
    def login():
            list=[]
            a1=e1.get()
            if len(a1)>0:
                if a1.isdigit():
                    EmployeeRecList=[]
                    with open('member.csv','r') as f:
                        data=csv.reader(f)
                        for i in data:
                            EmployeeRecList.append(i)
                    srNo=len(EmployeeRecList)
                    list.append(a1)
                    a2=e2.get().capitalize()
                    list.append(a2)
                    a3=e3.get()
                    list.append(a3)
                    a4=e4.get()
                    list.append(a4)
                    a5=e5.get()
                    list.append(a5)
                    a6=e6.get()
                    list.append(a6)
                    a7=e7.get()
                    list.append(a7)
                    a8=e8.get()
                    list.append(a8)
                    a9=e9.get()
                    list.append(a9)
                    a10=e10.get()
                    list.append(a10)
                    a11=e11.get()
                    list.append(a11)
                    a12=e12.get()
                    list.append(a12)
                    tv.insert("",END,values=tuple(list))
                    with open('hospitalpecent.csv','a',newline='') as ref:
                        employData=csv.writer(ref)
                        employData.writerow(list)
    def clear():
        e1.delete(0,"end")
        e2.delete(0,"end")
        e3.delete(0,"end")
        e4.delete(0,"end")
        e5.delete(0,"end")
        e6.delete(0,"end")
        e7.delete(0,"end")
        e8.delete(0,"end")
        e9.delete(0,"end")
        e10.delete(0,"end")
        e11.delete(0,"end")
        e12.delete(0,"end")
    wn=Toplevel()
    wn.title("Employee ateendence")
    wn.state('zoomed')
    wn.configure(bg="#babdcc",bd=10, relief=RIDGE)
     #frame 1
    f1=Frame(wn,bg="#babdcc",height="100",width="1513",bd=10, relief=RIDGE)
    f1.place(y=1,x=1)
    #Label 1 for Employee Ateendence Sheet
    L0=Label(f1,text="Patient full details",font=("Calibri",50),fg="white" ,bg="#babdcc")
    L0.place(y=0,x=500)
    f3=Frame(wn,bg="#babdcc",height="670",width="400",bd=10, relief=RIDGE)
    f3.place(y=102,x=1)
    L1=Label(f3,text="SrN. ",font=("Calibri",15),fg="white" ,bg="#babdcc")
    L1.place(y=5,x=10)
    e1=Entry(f3,font=("Calibri",15),fg="#babdcc")
    e1.place(y=10,x=153)
    L2=Label(f3,text="Patient Name: ",font=("Calibri",15),fg="white" ,bg="#babdcc")
    L2.place(y=55,x=10)
    e2=Entry(f3,font=("Calibri",15),fg="#babdcc")
    e2.place(y=60,x=153)
    L3=Label(f3,text="Father Name: ",font=("Calibri",15),fg="white" ,bg="#babdcc")
    L3.place(y=105,x=10)
    e3=Entry(f3,font=("Calibri",15),fg="#babdcc")
    e3.place(y=110,x=153)
    L4=Label(f3,text="Mother Name: ",font=("Calibri",15),fg="white" ,bg="#babdcc")
    L4.place(y=155,x=10)
    e4=Entry(f3,font=("Calibri",15),fg="#babdcc")
    e4.place(y=160,x=153)
    L5=Label(f3,text="Age/Sex :",font=("Calibri",15),fg="white" ,bg="#babdcc")
    L5.place(y=205,x=10)
    e5=Entry(f3,font=("Calibri",15),fg="#babdcc")
    e5.place(y=210,x=153)
    L6=Label(f3,text="Diagnosis: ",font=("Calibri",15),fg="white" ,bg="#babdcc")
    L6.place(y=255,x=10)
    e6=Entry(f3,font=("Calibri",15),fg="#babdcc")
    e6.place(y=260,x=153)
    L7=Label(f3,text="Word Number: ",font=("Calibri",15),fg="white" ,bg="#babdcc")
    L7.place(y=305,x=10)
    e7=Entry(f3,font=("Calibri",15),fg="#babdcc")
    e7.place(y=310,x=153)
    L8=Label(f3,text="Bed Number: ",font=("Calibri",15),fg="white" ,bg="#babdcc")
    L8.place(y=355,x=10)
    e8=Entry(f3,font=("Calibri",15),fg="#babdcc")
    e8.place(y=360,x=153)
    L9=Label(f3,text="Education: ",font=("Calibri",15),fg="white" ,bg="#babdcc")
    L9.place(y=405,x=10)
    e9=Entry(f3,font=("Calibri",15),fg="#babdcc")
    e9.place(y=410,x=153)
    L10=Label(f3,text="Occupation: ",font=("Calibri",15),fg="white" ,bg="#babdcc")
    L10.place(y=455,x=10)
    e10=Entry(f3,font=("Calibri",15),fg="#babdcc")
    e10.place(y=460,x=153)#
    L11=Label(f3,text="Mobile Number: ",font=("Calibri",15),fg="white" ,bg="#babdcc")
    L11.place(y=505,x=10)
    e11=Entry(f3,font=("Calibri",15),fg="#babdcc")
    e11.place(y=510,x=153)
    L12=Label(f3,text="Address: ",font=("Calibri",15),fg="white" ,bg="#babdcc")
    L12.place(y=555,x=10)
    e12=Entry(f3,font=("Calibri",15),fg="#babdcc")
    e12.place(y=560,x=153)
    bt1=Button(f3,font=("Elephant",12),fg="white",bg="#babdcc", text="Submit" ,command=login)
    bt1.place(y=605,x=180)
    bt2=Button(f3,font=("Elephant",12),fg="white",bg="#babdcc", text="Clear" ,command=clear)
    bt2.place(y=605,x=90)
    
   
    f2=Frame(wn,bg="#babdcc",height="670",width="1113",bd=10, relief=RIDGE)
    f2.place(y=102,x=401)   
    t=("sr","fn","ln","An","as","a","uf",'bn',"ed","oc","mn","ad")
    tv=ttk.Treeview(f2,height="32",show="headings",columns=t)
    tv.heading("sr",text="SrN.")
    tv.heading("fn",text="Patient Name")
    tv.heading("ln",text="Father Name")
    tv.heading("An",text="Mother Name")
    tv.heading("as",text="Age/Sex")
    tv.heading("a",text="Diagnosis")
    tv.heading("uf",text="Word No.")
    tv.heading("bn",text="Bed No.")
    tv.heading("ed",text="Education")
    tv.heading("oc",text="Occupatino")
    tv.heading("mn",text="Mo.No.")
    tv.heading("ad",text="Address")
    tv.column("#1",anchor=CENTER,width="50" )
    tv.column("#2",anchor=CENTER,width="120")
    tv.column("#3",anchor=CENTER,width="120")
    tv.column("#4",anchor=CENTER,width="120")
    tv.column("#5",anchor=CENTER,width="80")
    tv.column("#6",anchor=CENTER,width="80")
    tv.column("#7",anchor=CENTER,width="80")
    tv.column("#8",anchor=CENTER,width="80")
    tv.column("#9",anchor=CENTER,width="80")
    tv.column("#10",anchor=CENTER,width="80")
    tv.column("#11",anchor=CENTER,width="100")
    tv.column("#12",anchor=CENTER,width="100")
   
    tv.pack(side=TOP)
    with open('Employee.csv','a',newline='') as ref:
        pass
    employeeList=[]
    with open('Employee.csv','r') as ref:
        employeeData=csv.reader(ref)
        for i in employeeData:
            employeeList.append(i)
    for i in employeeList:
        tv.insert('',END,values=tuple(i))
    tv.pack(side=TOP)


    
    
    wn.mainloop()
# patient()