from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector as con
from datetime import datetime
from tkcalendar import Calendar,DateEntry
from name_pass import *

class Billing_App:

    def __init__(self,root):
        self.root = root
        width=root.winfo_screenwidth()
        height=root.winfo_screenheight()
        
        self.root.geometry("%dx%d+0+0"%(width,height))
        self.root.title("Home")
        
        self.cur_date=datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        self.cur_time=StringVar()
        self.cur_time=datetime.today().strftime("%H:%M:%S")

        self.name_bef=StringVar()
        self.phone_bef=StringVar()
        self.mail_bef=StringVar()
        self.address_bef=StringVar()

        self.id=0

        c=Canvas (self.root, bg="gray", height=int(height), width=int(width))
        image = Image.open("pic.jpg")

        self.photo = ImageTk.PhotoImage(image)
        self.item = c.create_image(int(height),int(width), image=self.photo)
        c.pack()

        self.fnc_frame=Frame(self.root,bd=5,bg="#ffffff",relief=RIDGE)
        self.fnc_frame.place(x=0,y=0,height=int(height*0.905),width=int(width*0.999))

        fnc_height=int(height* 0.9)
        fnc_width=int(width*0.9)


        def account():

            img5=Image.open("pic.jpg")
            img5=img5.resize((int(width*0.994),int(height* 0.895)),Image.ADAPTIVE)
            self.photoimg5=ImageTk.PhotoImage(img5)
            lblimg5=Label(self.fnc_frame,image=self.photoimg5,relief=RIDGE)
            lblimg5.place(x=0,y=0,width=int(width*0.994),height=int(height* 0.895))

            self.label_title=LabelFrame(self.fnc_frame,relief="groove",text="Contact Details",font=("times new roman",25,"bold"),bg="#ffffff")
            self.label_title.place(x=int(fnc_width*0.02),y=int(fnc_height*0.01),height=int(height* 0.5),width=int(width*0.25))

            self.detail_frame=LabelFrame(self.fnc_frame,relief="groove",text="Contact Book",font=("times new roman",25,"bold"),bg="#ffffff")
            self.detail_frame.place(x=int(width*0.282),y=int(fnc_height*0.01),height=int(height* 0.86),width=int(width*0.7))

            self.table_frame=Frame(self.detail_frame,bd=5)
            self.table_frame.place(x=int(width*0.03),y=int(fnc_height*0.1),height=int(height* 0.7),width=int(width*0.645))

            self.combo = ttk.Combobox(self.detail_frame,values=["Name","Phone Number","Email","Address","All Details"],width=int(fnc_width*0.02),state="readonly")
            self.combo.current(0)
            self.combo.place(x=int(width*0.2),y=int(fnc_height*0.02))
            
            self.filter_box = Entry(self.detail_frame,font=("arial",int(fnc_width*0.01)),bg="#D6F9FF")
            self.filter_box.place(x=int(width*0.33),y=int(fnc_height*0.02),width=int(width*0.18))


            lbl_name=Label(self.label_title,text="Name",font=("times new roman",16,"bold"),bg="#ffffff")
            lbl_name.grid(row=0,column=0,padx=int(fnc_width*0.01),pady=int(fnc_width*0.01),sticky=W)

            self.txt_name=Entry(self.label_title,font=("arial",16),width=19)
            self.txt_name.grid(row=0,column=1,padx=int(fnc_width*0.005),pady=int(fnc_width*0.01),sticky=W)

            lbl_phone=Label(self.label_title,text="Phone No.",font=("times new roman",16,"bold"),bg="#ffffff")
            lbl_phone.grid(row=1,column=0,padx=int(fnc_width*0.01),pady=int(fnc_width*0.01),sticky=W)

            self.txt_phone=Entry(self.label_title,font=("arial",16),width=19)
            self.txt_phone.grid(row=1,column=1,padx=int(fnc_width*0.005),pady=int(fnc_width*0.01),sticky=W)

            lbl_mail=Label(self.label_title,text="Email",font=("times new roman",16,"bold"),bg="#ffffff")
            lbl_mail.grid(row=2,column=0,padx=int(fnc_width*0.01),pady=int(fnc_width*0.01),sticky=W)

            self.txt_mail=Text(self.label_title,font=("arial",14),width=20,height=3)
            self.txt_mail.grid(row=2,column=1,padx=int(fnc_width*0.005),pady=int(fnc_width*0.01),sticky=W)
            self.txt_mail.configure(wrap="word")

            lbl_address=Label(self.label_title,text="Address",font=("times new roman",16,"bold"),bg="#ffffff")
            lbl_address.grid(row=3,column=0,padx=int(fnc_width*0.01),pady=int(fnc_width*0.01),sticky=W)

            self.txt_address=Text(self.label_title,font=("arial",14),width=20,height=4)
            self.txt_address.grid(row=3,column=1,padx=int(fnc_width*0.005),pady=int(fnc_width*0.01),sticky=W)
            self.txt_address.configure(wrap="word")

            def clear_all():
               for item in tree.get_children():
                  tree.delete(item)

            def displaySelectedItem(a):

                self.edit_btn["state"]="normal"
                self.delete_btn["state"]="normal"
                self.add_btn["state"]="disabled"

                conn=con.connect(host="localhost",database=db_name,user=user,passwd=pswd)
                cursor=conn.cursor(buffered = True)

                self.txt_name.delete(0,END)
                self.txt_phone.delete(0,END)
                self.txt_mail.delete("1.0","end")
                self.txt_address.delete("1.0","end")

                selectedItem = tree.selection()[0]
                sel=tree.item(selectedItem)['values']

                self.name_bef=sel[1]
                self.phone_bef=sel[2]
                self.mail_bef=sel[3]
                self.address_bef=sel[4]
                
                for i in range(len(sel)):
                    if sel[i]=="-":
                        sel[i]=""
                    else:
                        pass

                self.id=sel[0]

                self.txt_name.insert(0, sel[1])
                self.txt_phone.insert(0, sel[2])
                self.txt_mail.insert("1.0", sel[3])
                self.txt_address.insert("1.0", sel[4])
                

            def all_details():
                conn=con.connect(host="localhost",database=db_name,user=user,passwd=pswd)
                cursor=conn.cursor(buffered = True)
                sql="select * from contact_details"
                cursor.execute(sql)
                rec=cursor.fetchall()
                if rec:
                    for i in rec:
                        tree_insert=[]
                        for j in i:
                            if j=="NULL" or j==None or j=="":
                                tree_insert.append("-")
                            else:
                                tree_insert.append(j)
                        tree.insert("","end",values=tree_insert)
                conn.close()
             
            def details(Event):
                conn=con.connect(host="localhost",database=db_name,user=user,passwd=pswd)
                cursor=conn.cursor()
                fil=self.filter_box.get()
                sql=""
                if self.combo.get()=="All Details":
                    sql="select * from contact_details where name like '%{0}%' || phone like '%{0}%' || email like '%{0}%' || address like '%{0}%'".format(fil)
                elif self.combo.get()=="Name":
                    sql=f"select * from contact_details where name like '%{fil}%'"
                elif self.combo.get()=="Phone Number":
                    sql=f"select * from contact_details where phone like '%{fil}%'"
                elif self.combo.get()=="Email":
                    sql=f"select * from contact_details where email like '%{fil}%'"
                elif self.combo.get()=="Address":
                    sql=f"select * from contact_details where address like '%{fil}%'"
                else:
                    pass
                cursor.execute(sql)
                rec=cursor.fetchall()
                clear_all()
                if rec:
                    for i in rec:
                        tree_insert=[]
                        for j in i:
                            if j=="NULL" or j==None or j=="":
                                tree_insert.append("-")
                            else:
                                tree_insert.append(j)
                        tree.insert("","end",values=tree_insert)
                conn.close()



            scroll_right=Scrollbar(self.table_frame,orient='vertical')
            scroll_right.pack(side=RIGHT,fill='y')
            scroll_down=Scrollbar(self.table_frame,orient='horizontal')
            scroll_down.pack(side=BOTTOM,fill='x')
            tree=ttk.Treeview(self.table_frame,column=("c1","c2","c3","c4","c5"),show='headings')
            tree.configure(yscrollcommand=scroll_right.set,xscrollcommand=scroll_down.set)
            tree.configure(selectmode="extended",height=150)
            scroll_right.configure(command=tree.yview)
            scroll_down.configure(command=tree.xview)
            tree.column("#1",anchor="center",minwidth=0,width=0)
            tree.heading("#1",text="ID")
            tree.column("#2",anchor="center",width=250)
            tree.heading("#2",text="Name")
            tree.column("#3",anchor="center",width=150)
            tree.heading("#3",text="Phone no.")
            tree.column("#4",anchor="center",width=300)
            tree.heading("#4",text="Email")
            tree.column("#5",anchor="center",width=500)
            tree.heading("#5",text="Address")
            tree.pack()
            all_details()

            tree.bind("<<TreeviewSelect>>", displaySelectedItem)
            tree.bind("<Motion>", 'break')
            self.filter_box.bind('<KeyRelease>', details)
            self.combo.bind("<<ComboboxSelected>>", details)


            def add_contact():
                
                def add_new():
                    conn=con.connect(host="localhost",database=db_name,user=user,passwd=pswd)
                    cursor=conn.cursor()
                    que=messagebox.askyesno("Sure?","Are you sure?")
                    if que>0:
                        sq_check=f"select name,phone,email,address from contact_details"
                        cursor.execute(sq_check)
                        rec_check=cursor.fetchall()
                        rec_new=[]
                        
                        for i in rec_check:
                            i=list(i)
                            for j in range(0,len(i)):
                                if i[j]=="NULL" or i[j]==None:
                                    i[j]=""
                            rec_new.append(i)
                                      
                        if [self.txt_name.get(), self.txt_phone.get(), str(self.txt_mail.get("1.0", "end-1c")), str(self.txt_address.get("1.0","end-1c"))] in rec_new:
                            messagebox.showinfo("Message","Account already exists!")
                            self.txt_name.delete(0,"end")
                            self.txt_phone.delete(0,"end")
                            self.txt_mail.delete("1.0","end")
                            self.txt_address.delete("1.0","end")

                        else:
                            sql_id=f"select max(c_id) from contact_details"
                            cursor.execute(sql_id)
                            rec_id=cursor.fetchone()
                            if rec_id[0]==None:
                                c_id = 1
                            else:
                                c_id = rec_id[0] + 1

                            if self.txt_phone.get()=="":
                                phone="NULL"
                            else:
                                phone=self.txt_phone.get()

                            if str(self.txt_mail.get("1.0", "end-1c"))=="":
                                mail="NULL"
                            else:
                                mail=str(self.txt_mail.get("1.0", "end-1c"))
                            if str(self.txt_address.get("1.0","end-1c"))=="":
                                address="NULL"
                            else:
                                address=str(self.txt_address.get("1.0","end-1c"))
                             
                            sql=f"insert into contact_details values('{c_id}','{self.txt_name.get()}','{phone}','{mail}','{address}')"
                            
                            cursor.execute(sql)
                            conn.commit()
                            
                            clear_all()
                            all_details()
                            
                            self.txt_name.delete(0,"end")
                            self.txt_phone.delete(0,"end")
                            self.txt_mail.delete("1.0","end")
                            self.txt_address.delete("1.0","end")

                            conn.close()

                if self.txt_phone.get()!="" and (self.txt_phone.get().isdigit() == False or len(self.txt_phone.get())!= 10):
                    messagebox.showinfo("ERROR","Invalid Phone Number")
                elif ("@" not in str(self.txt_mail.get("1.0", "end-1c"))) and str(self.txt_mail.get("1.0", "end-1c"))!="" :
                    messagebox.showinfo("ERROR","Invalid Email")
                else:
                    add_new()
                        

            def edit_contact():
                que=messagebox.askyesno("Save","Do you want to save changes?")
                if que>0:
                    conn_ect=con.connect(host="localhost",database=db_name,user=user,passwd=pswd)
                    cur_sor=conn_ect.cursor(buffered = True)

                    if self.name_bef!=self.txt_name.get():
                        sql_update=f"update contact_details set name= '{self.txt_name.get()}' where c_id='{self.id}'"
                        cur_sor.execute(sql_update)
                        conn_ect.commit()
                    else:
                        pass

                    if self.phone_bef!=self.txt_phone.get():
                        sql_update=f"update contact_details set phone= '{self.txt_phone.get()}' where c_id='{self.id}'"
                        cur_sor.execute(sql_update)
                        conn_ect.commit()
                    else:
                        pass

                    if self.mail_bef!=str(self.txt_mail.get("1.0", "end-1c")):
                        sql_update=f"update contact_details set email= '{str(self.txt_mail.get("1.0", "end-1c"))}' where c_id='{self.id}'"
                        cur_sor.execute(sql_update)
                        conn_ect.commit()
                    else:
                        pass

                    if self.address_bef!=str(self.txt_address.get("1.0","end-1c")):
                        sql_update=f"update contact_details set address= '{str(self.txt_address.get("1.0","end-1c"))}' where c_id='{self.id}'"
                        cur_sor.execute(sql_update)
                        conn_ect.commit()
                    else:
                        pass
                    
                    clear_all()
                    all_details()
                    
                    conn_ect.close()
                    messagebox.showinfo("Success","Changes Saved Successfully")

                    self.txt_name.delete(0,"end")
                    self.txt_phone.delete(0,"end")
                    self.txt_mail.delete("1.0","end")
                    self.txt_address.delete("1.0","end")

                    self.edit_btn["state"]="disabled"
                    self.delete_btn["state"]="disabled"
                    self.add_btn["state"]="normal"

            def del_contact():
                que=messagebox.askyesno("Sure?","Are you sure?")
                if que>0:
                    conn=con.connect(host="localhost",database=db_name,user=user,passwd=pswd)
                    cursor=conn.cursor()
                    sql=f"delete from contact_details where c_id = '{self.id}'"
                    cursor.execute(sql)
                    conn.commit()

                    clear_all()
                    all_details()
                    
                    conn.close()
                    messagebox.showinfo("Success","Deleted Successfully")
                else:
                    pass

                self.txt_name.delete(0,"end")
                self.txt_phone.delete(0,"end")
                self.txt_mail.delete("1.0","end")
                self.txt_address.delete("1.0","end")

                self.edit_btn["state"]="disabled"
                self.delete_btn["state"]="disabled"
                self.add_btn["state"]="normal"
                
            def reset():
                
                self.edit_btn["state"]="disabled"
                self.delete_btn["state"]="disabled"
                self.add_btn["state"]="normal"

                self.txt_name.delete(0,"end")
                self.txt_phone.delete(0,"end")
                self.txt_mail.delete("1.0","end")
                self.txt_address.delete("1.0","end")
                

            self.btn_frame=Frame(self.label_title,relief="groove",bd=2,bg="#ffffff")
            self.btn_frame.place(x=int(fnc_width*0.012),y=int(fnc_height*0.42),height=int(height* 0.059),width=int(width*0.229))

            self.add_btn=Button(self.btn_frame,text="Add",height=1,width=6,font=("arial",14,"bold"),cursor="hand2",fg="#ffffff",bg="#1F1268",command=add_contact)
            self.add_btn.grid(row=0,column=0,pady=2,padx=2)

            self.edit_btn=Button(self.btn_frame,text="Update",height=1,width=6,font=("arial",14,"bold"),cursor="hand2",fg="#ffffff",bg="#1F1268",command=edit_contact)
            self.edit_btn.grid(row=0,column=1,pady=2,padx=2)
            self.edit_btn["state"]="disabled"

            self.delete_btn=Button(self.btn_frame,text="Delete",height=1,width=6,font=("arial",14,"bold"),cursor="hand2",fg="#ffffff",bg="#1F1268",command=del_contact)
            self.delete_btn.grid(row=0,column=2,pady=2,padx=2)
            self.delete_btn["state"]="disabled"

            self.reset_btn=Button(self.btn_frame,text="Reset",height=1,width=6,font=("arial",14,"bold"),cursor="hand2",fg="#ffffff",bg="#1F1268",command=reset)
            self.reset_btn.grid(row=0,column=3,pady=2,padx=2)

            s=ttk.Style()
            s.configure('Treeview',rowheight=24)


        account()

if __name__ == '__main__':
    root=Tk()
    obj=Billing_App(root)
    root.mainloop() 
