from tkinter import*
from tkinter import messagebox 
import mysql.connector 
root=Tk()
root.geometry("500x300")

def getvals():
  Name=e1.get()
  Phone=e2.get()
  Gender=e3.get()
  Emergency=e4.get()
  Paymentmode=e5.get()

  if(Name=="" or Phone=="" or Gender=="" or Emergency=="" or Paymentmode==""):
    messagebox.showinfo("ERROR","Empty Text are not Acceptable!!!")
  else:
      comm=mysql.connector.connect(host="localhost",user="root",password="",database="registered")
      cur1=comm.cursor()
      sql1="insert into shinchan(Name,Phone,Gender,Emergency,Paymentmode)values (%s,%s,%s,%s,%s)"
      val1=(Name,Phone,Gender,Emergency,Paymentmode)
      cur1.execute(sql1,val1)
      comm.commit()
      messagebox.showinfo("SUCCESS","YOUR ACCCOUNT HAS BEEN LOGINED")

#heading
Label(root,text="Caps Registration Form",font="times,12,bold").grid(row=0,column=3)
#field name
name=Label(root,text="Name")
phone=Label(root,text="Phone")
gender=Label(root,text="Gender")
emergency=Label(root,text="Emergency")
paymentmode=Label(root,text="PaymentMode")


#packing fields
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
paymentmode.grid(row=5,column=2)
#variable for storing data
namevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
emergencyvalue=StringVar()
paymentmodevalue=StringVar()



#creating entry fields
e1=Entry(root,textvariable=namevalue)
e2=Entry(root,textvariable=phonevalue)
e3=Entry(root,textvariable=gendervalue)
e4=Entry(root,textvariable=emergencyvalue)
e5=Entry(root,textvariable=paymentmodevalue)

#packing entry fields
e1.grid(row=1,column=3)
e2.grid(row=2,column=3)
e3.grid(row=3,column=3)
e4.grid(row=4,column=3)
e5.grid(row=5,column=3)

#submitfield

Button(text="submit",command=getvals).grid(row=8,column=3)





root.mainloop()
