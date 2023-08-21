import admin
import student
import tkinter
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

window = tkinter.Tk()
window.title("TRANSPORTION PORTAL")
window.geometry('1530x730')
window.configure(bg='azure')
bbg=Image.open("C:\\Users\\FARHAN KHAN\\OneDrive\\Desktop\\dbms mini project\\pictures\\mainjpg.jpg")
bck_end=ImageTk.PhotoImage(bbg)
my_label=Label(window,image=bck_end)
my_label.place(x=0,y=0,relwidth=1,relheight=1)

my_canvas=Canvas(window,width=1570,height=730)
my_canvas.pack(fill="both",expand=True)

#set image in canvas
my_canvas.create_image(0,0,image=bck_end,anchor='nw')

my_canvas.create_text(780,50,text="CITNC TRANSPORTATION MANAGEMENT SYSTEM",font=('Arial Black', 34),fill="navy")
my_canvas.create_text(780,530,text="SELECT YOUR POST/POSITION IN THE COLLEGE",font=('Arial Black', 24),fill='white')


def stu():
    os.system('student.py')

def ad():
    os.system('admin_login.py')

#frame = tkinter.Frame(bg="antiqueWhite2")
#button
button1=Button(window,text="STUDENT/FACULTY",command=stu)
button2=Button(window,text="ADMIN",command=ad)

button1_window=my_canvas.create_window(720,640,window=button1)
button2_window=my_canvas.create_window(810,640,window=button2)



'''#widgets
label = tkinter.Label(frame, text="TRANPORTATION MANAGEMENT SYSTEM",bg="antiqueWhite2", font=("Arial", 30))
msg= tkinter.Label(frame,text='select your post/position in the college',bg="antiqueWhite2",font=("arial",20))

student_button = tkinter.Button(frame, text="STUDENT/FACULTY", font=("Arial", 16), command=stu)
admin_button = tkinter.Button(frame, text="ADMIN", font=("Arial", 16), command=ad)

#widget placing
label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
msg.grid(row=2, column=0, columnspan=2, sticky="news", pady=40)
student_button.grid(row=0, column=0,sticky=E, pady=30)
admin_button.grid(row=0, column=1,sticky=W, pady=30)


frame.pack()'''

window.mainloop()