import random as r 
import tkinter as t
from tkinter import StringVar, messagebox
from tkinter import Tk, filedialog

address=""  # This Global Variable is used to store the path where we want to store the Text file

def select():
   root = Tk() 
   root.withdraw() 
   root.attributes('-topmost', True) 
   open_file = filedialog.askdirectory()
   print(open_file)
   global address 
   global myvar
   myvar.set(open_file)
   address = open_file  

def info():
   messagebox.showinfo("INSTRUCTIONS","1.Use 2 digits less in third entry\n    (Total No. of digits - Starting Digits) \n 2.Entry other than name should be only integer\n ")

def phnno():
   try:
      global address 
      location=address+"/"+"phndir.txt" 
      n1=int(e1.get()) # Fetching input data from Input Widget
      n2=int(e2.get())
      n3=int(e3.get())
      #n4=str(e4.get())
      file=open(location,"a")
      v=''
      for i in range(n2):
         for j  in range(n3):
               z=str(r.randint(0,9))
               v=v+z
         w=str(n1)+v
         file2=open(location,"r")
         q=file2.readlines()
         if w in q:
               print("already")
         else:
               
               file.write(w+"\n")
               v=''
      messagebox.showinfo("Numbers Genrated","Numbers are Genrated Successfuly ")
      file.close()
   except:
      messagebox.showwarning("Exception Occured","There are some fields empty")

#________Main________   

top=t.Tk()
top.title("Phone Number Generator")
top.geometry("550x290")
top.resizable(0,0)
top.config(bg="blue")
h1=t.Label(top,text=" Phone Number Genrator ",font=("calibri",30),fg="red",relief="raised").place(x=60,y=8)

l1=t.Label(top,text="Enter Starting Digits",font=("Arial",10)).place(x=60,y=95)
e1=t.Entry(top,width=10)
e1.place(x=200,y=98)

l2=t.Label(top,text="Enter how many Numbers to be Genrated",font=("arial",10)).place(x=60,y=125)
e2=t.Entry(top,width=10)
e2.place(x=318,y=128)

l3=t.Label(top,text="Enter the the no. of digits",font=("arial",10)).place(x=60,y=155)
e3=t.Entry(top,width=10)
e3.place(x=225,y=158)

myvar=StringVar()
myvar.set("Browse ")
l5=t.Label(top,text="File Location ").place(x=60,y=185)
bt=t.Button(top,textvariable=myvar,command=select).place(x=165,y=185)

b=t.Button(top,text="Submit",command=phnno)
b.config(font='arial')
b.place(x=430,y=245)

b2=t.Button(top,text="i",bg='blue',command=info)
b2.config(bg="black",fg="white",width=2,font='arial')
b2.place(x=510,y=20)

top.mainloop()