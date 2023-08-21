from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox

class Student:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x730+0+0")
        self.root.config(bg="light yellow") 
        self.root.title('Transportation Management System')

        # variables
        self.var_pos=StringVar()
        self.var_name=StringVar()
        self.var_phno=StringVar()
        self.var_id=StringVar()
        self.var_gdr=StringVar()
        self.var_pk=StringVar()
        self.var_dp=StringVar()
        self.var_pr=StringVar()
        self.var_dr=StringVar()


        lbl_title=Label(self.root,text="CITNC STUDENT/FACULTY TRANSPORTATION PORTAL",font=('Times new roman',30,'bold'),fg='darkblue',bg='white')
        lbl_title.place(x=0,y=0,width=1530,height=50)


        # making a image frame box
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=50,width=1530,height=160)

        # 1st 
        img1=Image.open('pictures/IMG_20230116_125007 (1).jpg')
        img1=img1.resize((382,160),Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(img1)

        self.img_1=Label(img_frame,image=self.photo1)
        self.img_1.place(x=0,y=0,width=382,height=160)

        # 2nd
        img2=Image.open('pictures/IMG_20230116_124925.jpg')
        img2=img2.resize((382,160),Image.ANTIALIAS)
        self.photo2=ImageTk.PhotoImage(img2)

        self.img_2=Label(img_frame,image=self.photo2)
        self.img_2.place(x=382,y=0,width=382,height=160)

        #3rd
        img3=Image.open('pictures/IMG_20230116_1625001.jpg')
        img3=img3.resize((383,160),Image.ANTIALIAS)
        self.photo3=ImageTk.PhotoImage(img3)

        self.img_3=Label(img_frame,image=self.photo3)
        self.img_3.place(x=764,y=0,width=383,height=160)

        #4th
        img4=Image.open('pictures/IMG_20230116_124906.jpg')
        img4=img4.resize((483,160),Image.ANTIALIAS)
        self.photo4=ImageTk.PhotoImage(img4)

        self.img_4=Label(img_frame,image=self.photo4)
        self.img_4.place(x=1147,y=0,width=383,height=160)


        #making second frame
        main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='DarkSeaGreen1')
        main_frame.place(x=10,y=220,width=1500,height=560)

        # upper frame
        upper_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,bg='white',text='Student/Faculty Information',font=('Times new roman',11,'bold'),fg='red')
        upper_frame.place(x=10,y=10,width=1480,height=270)

        # Labels and Entry files

        # position entry
        lbl_pos=Label(upper_frame,text='Position',font=('arial',11,'bold'),bg='white')
        lbl_pos.grid(row=0,column=0,padx=2,sticky=W)

        combo_pos=ttk.Combobox(upper_frame,textvariable=self.var_pos,font=('arial',12,'bold'),width=17,state='readonly')
        combo_pos['value']=(' ','Student','College Faculty')
        combo_pos.current(0)
        combo_pos.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # name entry
        lbl_name=Label(upper_frame,text='  Name:',font=('arial',12,'bold'),bg='white')
        lbl_name.grid(row=0,column=3,padx=2,sticky=W,pady=7)

        txt_name=ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font=('arial',11,"bold"))
        txt_name.grid(row=0,column=4,padx=2,pady=7,sticky=W) 

        # pickup point entry
        lbl_pk=Label(upper_frame,text='Pickup Point:',font=('arial',12,'bold'),bg='white')
        lbl_pk.grid(row=1,column=0,padx=2,sticky=W,pady=7)

        txt_pk=ttk.Entry(upper_frame,textvariable=self.var_pk,width=22,font=('arial',11,"bold"))
        txt_pk.grid(row=1,column=1,padx=2,pady=7,sticky=W)

        # drop point entry
        lbl_dp=Label(upper_frame,text='  Drop Point:',font=('arial',12,'bold'),bg='white')
        lbl_dp.grid(row=1,column=3,padx=2,sticky=W,pady=7)

        txt_dp=ttk.Entry(upper_frame,textvariable=self.var_dp,width=22,font=('arial',11,"bold"))
        txt_dp.grid(row=1,column=4,padx=2,pady=7,sticky=W)

        # Phone no entry
        lbl_phno=Label(upper_frame,text='Phone No:',font=('arial',12,'bold'),bg='white')
        lbl_phno.grid(row=2,column=0,padx=2,sticky=W,pady=7)

        txt_phno=ttk.Entry(upper_frame,textvariable=self.var_phno,width=22,font=('arial',11,"bold"))
        txt_phno.grid(row=2,column=1,padx=2,pady=7,sticky=W)

        # ID no entry
        lbl_idno=Label(upper_frame,text='  ID / USN No:',font=('arial',12,'bold'),bg='white')
        lbl_idno.grid(row=2,column=3,padx=2,sticky=W,pady=7)

        txt_idno=ttk.Entry(upper_frame,textvariable=self.var_id,width=22,font=('arial',11,"bold"))
        txt_idno.grid(row=2,column=4,padx=2,pady=7,sticky=W)

        # gender entry
        lbl_gd=Label(upper_frame,text='  Gender:',font=('arial',11,'bold'),bg='white')
        lbl_gd.grid(row=0,column=5,padx=2,sticky=W,pady=7)

        combo_gd=ttk.Combobox(upper_frame,textvariable=self.var_gdr,font=('arial',12,'bold'),width=17,state='readonly')
        combo_gd['value']=(' ','Male','Female','Other')
        combo_gd.current(0)
        combo_gd.grid(row=0,column=6,padx=2,pady=7,sticky=W)

        # pickup route no entry
        lbl_pr=Label(upper_frame,text='Pickup Route No:',font=('arial',11,'bold'),bg='white')
        lbl_pr.grid(row=3,column=0,padx=2,sticky=W,pady=7)

        combo_pr=ttk.Combobox(upper_frame,textvariable=self.var_pr,font=('arial',12,'bold'),width=17,state='readonly')
        combo_pr['value']=(' ','1','2','3','4','5','6','7','8','9','10')
        combo_pr.current(0)
        combo_pr.grid(row=3,column=1,padx=2,pady=7,sticky=W)

        # drop route no entry
        lbl_dr=Label(upper_frame,text='  Drop Route No:',font=('arial',11,'bold'),bg='white')
        lbl_dr.grid(row=3,column=3,padx=2,sticky=W,pady=7)

        combo_dr=ttk.Combobox(upper_frame,textvariable=self.var_dr,font=('arial',12,'bold'),width=17,state='readonly')
        combo_dr['value']=(' ','1','2','3','4','5','6','7','8','9','10')
        combo_dr.current(0)
        combo_dr.grid(row=3,column=4,padx=2,pady=7,sticky=W)

        

        #img inside upper frame
        citnc=Image.open('pictures/1657093680868-dc6d1c0a-81ce-4511-ab0c-93a4111d2bc5 (1).jpg')
        citnc.resize((540,160),Image.ANTIALIAS)
        self.photocitnc=ImageTk.PhotoImage(citnc)

        self.img_citnc=Label(upper_frame,image=self.photocitnc)
        self.img_citnc.place(x=750,y=38,width=540,height=150)

        #button frame
        button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=1300,y=60,width=170,height=110)

        btn_add=Button(button_frame,text="Save",command=self.add_data,font=('arial',14,'bold'),width=13,bg='lawn green',fg='black')
        btn_add.grid(row=0,column=0,padx=1,pady=5)

        btn_clr=Button(button_frame,text="Clear",command=self.reset_data,font=('arial',14,'bold'),width=13,bg='lawn green',fg='black')
        btn_clr.grid(row=3,column=0,padx=1,pady=5)

        

               
        #down frame
        down_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,bg='white',text='Student/Faculty Information Table',font=('Times new roman',11,'bold'),fg='red')
        down_frame.place(x=10,y=280,width=1480,height=270)

        #search frame
        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,bg='white',text='Search Information',font=('Times new roman',11,'bold'),fg='dark slate gray')
        search_frame.place(x=5,y=0,width=1470,height=60)

        search_by=Label(search_frame,text='Search By:',font=('arial',11,'bold'),fg='white',bg='red')
        search_by.grid(row=0,column=0,padx=5,sticky=W)

        #search
        self.var_com_search=StringVar()
        com_txt_search=ttk.Combobox(search_frame,textvariable=self.var_com_search,font=('arial',12,'bold'),width=18,state='readonly')
        com_txt_search['value']=(' ','Id','Phone')
        com_txt_search.current(0)
        com_txt_search.grid(row=0,column=1,padx=5,sticky=W)


        self.var_search=StringVar()
        txt_search=ttk.Entry(search_frame,textvariable=self.var_search,width=22,font=('arial',11,'bold'))
        txt_search.grid(row=0,column=2,padx=5)

        btn_search=Button(search_frame,command=self.search_data,text="Search",font=('arial',11,'bold'),width=14,bg='lawn green',fg='black')
        btn_search.grid(row=0,column=3,padx=5)
        
        btn_ShowAll=Button(search_frame,text="Show All",command=self.fetch_data,font=('arial',11,'bold'),width=14,bg='lawn green',fg='black')
        btn_ShowAll.grid(row=0,column=4,padx=5)

        # ==================================Student table=====================================
        #table frame
        table_frame=Frame(down_frame,bd=3,relief=RIDGE)
        table_frame.place(x=5,y=60,width=1470,height=170)

        # scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        # table under scrollbar
        self.student_table=ttk.Treeview(table_frame,columns=('pos','name','phno','id','gdr','pk','dp','pr','dr',),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading('pos',text='Position')
        self.student_table.heading('name',text='Name')
        self.student_table.heading('phno',text='Phone No')
        self.student_table.heading('id',text='ID/USN No')
        self.student_table.heading('gdr',text='Gender')
        self.student_table.heading('pk',text='Pickup Point')
        self.student_table.heading('dp',text='Drop Point')
        self.student_table.heading('pr',text='Pickup Route No')
        self.student_table.heading('dr',text='Drop Route No')

        self.student_table['show']='headings'

        self.student_table.column('pos',width=120)
        self.student_table.column('name',width=140)
        self.student_table.column('phno',width=140)
        self.student_table.column('id',width=140)
        self.student_table.column('gdr',width=120)
        self.student_table.column('pk',width=120)
        self.student_table.column('dp',width=120)
        self.student_table.column('pr',width=120)
        self.student_table.column('dr',width=120)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()

    # *******************fuction declarations**************
    
    def add_data(self):
        if self.var_pos.get()=="" or self.var_id.get()=="":
            messagebox.showerror('error','All fields are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost', user='root',password='system123@',database='mydata')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into transport values(%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                                                                  self.var_pos.get(),
                                                                                                  self.var_name.get(),
                                                                                                  self.var_phno.get(),
                                                                                                  self.var_id.get(),
                                                                                                  self.var_gdr.get(),
                                                                                                  self.var_pk.get(),
                                                                                                  self.var_dp.get(),
                                                                                                  self.var_pr.get(),
                                                                                                  self.var_dr.get()
                                                                                              ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('success', ' student/faculty has been added',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due to:{str(es)}',parent=self.root)


    # fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost', user='root',password='system123@',database='mydata')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from transport')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit
        conn.close()

    # get cursor
    def get_cursor(self,event=''):
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        data=content['values']

        self.var_pos.set(data[0])
        self.var_name.set(data[1])
        self.var_phno.set(data[2])
        self.var_id.set(data[3])
        self.var_gdr.set(data[4])
        self.var_pk.set(data[5])
        self.var_dp.set(data[6])
        self.var_pr.set(data[7])
        self.var_dr.set(data[8])

    # get update
    def update_data(self):
        
        messagebox.showinfo('Notice','contact the ADMIN to make any changes to the data.',parent=self.root)



    #get reset
    def reset_data(self):
        self.var_pos.set(" ")
        self.var_name.set("")
        self.var_phno.set("")
        self.var_id.set("")
        self.var_gdr.set(" ")
        self.var_pk.set("")
        self.var_dp.set("")
        self.var_pr.set(" ")
        self.var_dr.set(" ")


    # second frame 
    # search
    def search_data(self):
        if self.var_com_search.get()==' ' or self.var_search.get()=='':
            messagebox.showerror('Error','Please select option')
        else:
            try:
                conn=mysql.connector.connect(host='localhost', user='root',password='system123@',database='mydata')
                my_cursor=conn.cursor()
                my_cursor.execute('select * from transport where ' + str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("",END,values=i)
                conn.commit
                conn.close()
            except Exception as es:
                messagebox.showerror('Error',f'Due to:{str(es)}',parent=self.root)









if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()