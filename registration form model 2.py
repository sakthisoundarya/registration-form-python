from tkinter import*

    


root=Tk()
root.geometry("270x300")


# creating heading

label=Label(root,text="Registration form",font="times,8,bold").grid(row=1,column=3)
#creating field name(label)
firstname=Label(root,text="Firstname",fg="violet")
lastname=Label(root,text="Lastname",fg="indigo")
birth=Label(root,text="Birth",fg="blue")
email=Label(root,text="email",fg="green")
phone=Label(root,text="phone",fg="magenta")
zipcode=Label(root,text="zipcode",fg="olive")

#packing the field name
firstname.grid(row=2,column=2)
lastname.grid(row=4,column=2)
birth.grid(row=7,column=2)
email.grid(row=8,column=2)
phone.grid(row=9,column=2)
zipcode.grid(row=10,column=2)

#creating database to storedata

firstnamevalue=StringVar()
lastnamevalue=StringVar()
birthvalue=StringVar()
emailvalue=StringVar()
phonevalue=StringVar()
zipcodevalue=StringVar()


#creating entry field

e1=Entry(root,textvariable=firstnamevalue)
e2=Entry(root,textvariable=lastnamevalue)
e3=Entry(root,textvariable=birthvalue)
e4=Entry(root,textvariable=emailvalue)
e5=Entry(root,textvariable=phonevalue)
e6=Entry(root,textvariable=zipcodevalue)


#packing the entry field

e1.grid(row=2,column=3)
e2.grid(row=4,column=3)
e3.grid(row=7,column=3)
e4.grid(row=8,column=3)
e5.grid(row=9,column=3)
e6.grid(row=10,column=3)


#creating radiobutton


gender=IntVar()
male=Radiobutton(root,text="male",variable=gender,value=1)
female=Radiobutton(root,text="female",variable=gender,value=2)
no=Radiobutton(root,variable=gender,value=3)

#packing radiobutton
male.grid(row=3,column=3)
female.place(x=51,y=50)
#creating submit button


B1=Button(root,text="submit",command="save to file",bg="orange",fg="blue")
B1.place(x=60,y=190,width=150)
B2=Button(root, text='Quit',bg='orange',fg='black' ,command=root.quit)
B2.place(x=60,y=220,width=150)



root.mainloop()

               
                 
                 
                 
