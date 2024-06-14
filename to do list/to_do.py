from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector as con
from name_pass import *

class To_do_list:

    def __init__(self,root):
        self.root = root
        width=root.winfo_screenwidth()
        height=root.winfo_screenheight()
        
        self.root.geometry("%dx%d+0+0"%(width*0.8125,height*0.9))
        self.root.title("Home")
        self.root.resizable(False,False)

        self.sel=[]

        c=Canvas (self.root, bg="gray", height=int(height), width=int(width))
        image = Image.open("pic.jpg")

        self.photo = ImageTk.PhotoImage(image)
        self.item = c.create_image(int(height),int(width), image=self.photo)
        c.pack()

        self.fnc_frame=Frame(self.root,bd=5,bg="#ffffff",relief=RIDGE)
        self.fnc_frame.place(x=0,y=0,height=int(height*0.895),width=int(width*0.810))

        fnc_height=int(height* 0.9)
        fnc_width=int(width*0.9)

        img5=Image.open("pic.jpg")
        img5=img5.resize((int(width*0.994),int(height* 0.895)),Image.ADAPTIVE)
        self.photoimg5=ImageTk.PhotoImage(img5)
        lblimg5=Label(self.fnc_frame,image=self.photoimg5,relief=RIDGE)
        lblimg5.place(x=0,y=0,width=int(width*0.994),height=int(height* 0.895))


        self.table_frame=Frame(self.fnc_frame,bd=5)
        self.table_frame.place(x=int(width*0.08),y=int(fnc_height*0.19),height=int(height* 0.6),width=int(width*0.645))

        self.combo = ttk.Combobox(self.fnc_frame,values=["Pending","Processing","Completed","All"],width=int(fnc_width*0.015),state="readonly")
        self.combo.current(3)
        self.combo.place(x=int(width*0.106),y=int(fnc_height*0.1))
            
        self.filter_box = Entry(self.fnc_frame,font=("arial",int(fnc_width*0.01)),bg="#f2fdff")
        self.filter_box.place(x=int(width*0.205),y=int(fnc_height*0.1),width=int(width*0.42))


        def clear_all():
            for item in tree.get_children():
                tree.delete(item)

        def all_details():
            clear_all()
            conn=con.connect(host="localhost",database=db_name,user=user,passwd=pswd)
            cursor=conn.cursor(buffered = True)
            sql="select * from task_record"
            cursor.execute(sql)
            rec=cursor.fetchall()
            if rec:
                for x in range (len(rec)):
                    i=list(rec[x])
                    tree_insert=[]
                    for j in range(0,3):
                        if i[j]=="NULL" or i[j]==None or i[j]=="":
                            tree_insert.append("-")
                        else:
                            tree_insert.append(i[j])
                    tree_insert.insert(1,x+1)
                    tree.insert("","end",values=tree_insert)
            conn.close()
             
        def details(Event):
            fil=self.filter_box.get()

            if self.combo.get()=="Processing":
                sql=f"select * from task_record where status='Processing' and task like '%{fil}%'"
            elif self.combo.get()=="Pending":
                sql=f"select * from task_record where status='Pending' and task like '%{fil}%'"
            elif self.combo.get()=="Completed":
                sql=f"select * from task_record where status='Completed' and task like '%{fil}%'"
            else:
                sql=f"select * from task_record where task like '%{fil}%'"
            details_(sql)

        def details_(sql):
                
            conn=con.connect(host="localhost",database=db_name,user=user,passwd=pswd)
            cursor=conn.cursor(buffered=True)

            clear_all()
            cursor.execute(sql)
            rec=cursor.fetchall()
            if rec:
                for x in range (len(rec)):
                    i=list(rec[x])
                    tree_insert=[]
                    for j in range(0,3):
                        if i[j]=="NULL" or i[j]==None or i[j]=="":
                            tree_insert.append("-")
                        else:
                            tree_insert.append(i[j])
                    tree_insert.insert(1,x+1)
                    tree.insert("","end",values=tree_insert)
            conn.close()

        
        def update():
            global pop
            pop=Toplevel(self.root)
            pop.title("Update Task")
            pop.geometry("380x220")
            pop.configure(bg="#ffffff")
            pop.resizable(False,False)

            def update_event(Event):
                save()

            pop.label_title=Frame(pop,relief="groove",bg="#ffffff")
            pop.label_title.place(x=int(fnc_width*0.01),y=int(fnc_height*0.01),height=int(height* 0.65),width=int(width*0.25))

            lbl_name=Label(pop.label_title,text="Task",font=("times new roman",16,"bold"),bg="#ffffff")
            lbl_name.grid(row=1,column=0,padx=int(fnc_width*0.01),pady=int(fnc_width*0.01),sticky=W)

            pop.txt_name=Text(pop.label_title,font=("arial",14),width=20,height=3)
            pop.txt_name.grid(row=1,column=1,padx=int(fnc_width*0.01),pady=int(fnc_width*0.01),sticky=W)
            pop.txt_name.configure(wrap="word")
            pop.txt_name.bind('<Return>', update_event)

            lbl_st=Label(pop.label_title,text="Status",font=("times new roman",16,"bold"),bg="#ffffff")
            lbl_st.grid(row=2,column=0,padx=int(fnc_width*0.01),pady=int(fnc_width*0.01),sticky=W)

            pop.status = ttk.Combobox(pop.label_title,values=["Pending","Processing","Completed"],font=("",16),width=12,state="readonly")
            pop.status.grid(row=2,column=1,padx=int(fnc_width*0.01),pady=int(fnc_width*0.01),sticky=W)

            pop.txt_name.delete(1.0,"end")
            pop.txt_name.insert("end",f"{self.sel[2]}")

            pop.status.set(self.sel[3])

            def save():
                pop.status["state"]="disabled"
                pop.txt_name["state"]="disabled"

                conn=con.connect(host="localhost",database=db_name,user=user,passwd=pswd)
                cursor=conn.cursor(buffered = True)
                inp=str(pop.txt_name.get("1.0", "end-1c"))
                sql=f"update task_record set task='{inp}' , status='{pop.status.get()}' where t_id={self.sel[0]}"
                cursor.execute(sql)
                conn.commit()
                conn.close()

                clear_all()
                all_details()

                pop.destroy()

                delete_btn["state"]="disabled"
                edit_btn["state"]="disabled"


            save_btn=Button(pop.label_title,text="Save",width=10,font=("arial",12,"bold"),cursor="hand2",fg="#ffffff",bg="#09056e",command=save)
            save_btn.grid(row=3,column=0,columnspan=2)


        def delete():
            conn=con.connect(host="localhost",database=db_name,user=user,passwd=pswd)
            cursor=conn.cursor(buffered = True)
            sql=f"delete from task_record where t_id={self.sel[0]}"
            cursor.execute(sql)
            conn.commit()
            conn.close()

            delete_btn["state"]="disabled"
            edit_btn["state"]="disabled"

            clear_all()
            all_details()

        
        def add_data():
            if self.filter_box.get()=="":
                messagebox.showinfo("","Please enter a task first!")
            else:
                if self.combo.get()=="All":
                    status="Processing"
                else:
                    status=self.combo.get()
                conn=con.connect(host="localhost",database=db_name,user=user,passwd=pswd)
                cursor=conn.cursor(buffered=True)
                sql=f"insert into task_record(task,status) values ('{self.filter_box.get()}','{status}')"
                cursor.execute(sql)
                conn.commit()
                conn.close()

                self.combo.current(3)
                self.filter_box.delete(0,"end")
                all_details()


        def displaySelectedItem(Event):
            selectedItem = tree.selection()[0]
            self.sel=tree.item(selectedItem)['values']
            edit_btn["state"]="normal"
            delete_btn["state"]="normal"



        scroll_right=Scrollbar(self.table_frame,orient='vertical')
        scroll_right.pack(side=RIGHT,fill='y')
        tree=ttk.Treeview(self.table_frame,column=("c1","c2","c3","c4"),show='headings')
        tree.configure(yscrollcommand=scroll_right.set)
        tree.configure(selectmode="extended",height=150)
        scroll_right.configure(command=tree.yview)
        tree.column("#1",anchor="center",width=0,minwidth=0)
        tree.heading("#1",text="ID")
        tree.column("#2",anchor="center",width=100)
        tree.heading("#2",text="S.No.")
        tree.column("#3",anchor="center",width=650)
        tree.heading("#3",text="Task")
        tree.column("#4",anchor="center",width=200)
        tree.heading("#4",text="Status")
        tree.pack()
        all_details()

        tree.bind("<Motion>", 'break')
        tree.bind("<<TreeviewSelect>>", displaySelectedItem)

        self.filter_box.bind('<KeyRelease>', details)
        self.combo.bind("<<ComboboxSelected>>", details)

        s=ttk.Style()
        s.configure('Treeview',rowheight=30)
        s.configure("Treeview.Heading", font=("Arial", 14),rowheight=100)
        s.configure("Treeview", font=("None", 10))


        edit_btn=Button(self.fnc_frame,text="Update",width=10,font=("arial",12,"bold"),cursor="hand2",fg="#ffffff",bg="#09056e",command=update)
        edit_btn.place(x=int(width*0.33),y=int(fnc_height*0.875))
        edit_btn["state"]="disabled"

        delete_btn=Button(self.fnc_frame,text="Remove",width=10,font=("arial",12,"bold"),cursor="hand2",fg="#ffffff",bg="#09056e",command=delete)
        delete_btn.place(x=int(width*0.41),y=int(fnc_height*0.875))
        delete_btn["state"]="disabled"

        add_btn=Button(self.fnc_frame,text="Add",width=10,font=("arial",12,"bold"),cursor="hand2",fg="#ffffff",bg="#09056e",command=add_data)
        add_btn.place(x=int(width*0.63),y=int(fnc_height*0.095))




if __name__ == '__main__':
    root=Tk()
    obj=To_do_list(root)
    root.mainloop() 