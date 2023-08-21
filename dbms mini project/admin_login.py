import tkinter
from tkinter import*
from tkinter import messagebox
import admin
import os
from PIL import Image, ImageTk


window = tkinter.Tk()
window.title("Admin Login form")
window.geometry('1530x730+0+0')
window.configure(bg='#333333')
bbg=Image.open("C:\\Users\\FARHAN KHAN\\OneDrive\\Desktop\\dbms mini project\\pictures\\adminlogin.jpg")
bck_end=ImageTk.PhotoImage(bbg)
my_label=Label(window,image=bck_end)
my_label.place(x=0,y=0,relwidth=1,relheight=1)

my_canvas=Canvas(window,width=1570,height=730)
my_canvas.pack(fill="both",expand=True)

#set image in canvas
my_canvas.create_image(0,0,image=bck_end,anchor='nw')

my_canvas.create_text(780,205,text="ADMIN LOGIN", font=("Arial Black",30))

my_canvas.create_text(650,350,text="USERNAME",font=('Arial Black', 14),fill='blue')
my_canvas.create_text(650,390,text="PASSWORD",font=('Arial Black', 14),fill='blue')


def login():
    username = "AdminCIT"
    password = "1234@"
    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title="Login Success", message="You successfully logged in.")
        window.destroy()
        os.system('admin.py')
        
    else:
        messagebox.showerror(title="Error", message="Invalid login.")

#button
button1=Button(window,text="login",command=login)

button1_window=my_canvas.create_window(755,480,window=button1)


'''frame = tkinter.Frame()

# Creating widgets
login_label = tkinter.Label(
    frame, text="Admin Login", font=("Arial", 30))
username_label = tkinter.Label(
    frame, text="Username", font=("Arial", 16))'''
username_entry = tkinter.Entry(window, font=("Arial", 16))
password_entry = tkinter.Entry(window, show="*", font=("Arial", 16))

username_window=my_canvas.create_window(835,350,window=username_entry)
password_window=my_canvas.create_window(835,390,window=password_entry,)


#password_label = tkinter.Label(
#    window, text="Password", font=("Arial", 16))
'''login_button = tkinter.Button(
    window, text="Login", font=("Arial", 16), command=login)'''

# Placing widgets on the screen
'''login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)

frame.pack()'''

window.mainloop()