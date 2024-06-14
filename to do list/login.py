from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
import os


class To_do_list:

    def __init__(self,root):
        self.root = root 
        width=root.winfo_screenwidth()
        height=root.winfo_screenheight()
        self.root.geometry("%dx%d+0+0"%(width*0.8125,height*0.9))
        self.root.title("Login")
        self.root.resizable(False,False)
        
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

        wx=int(width*0.8125)-int(height*0.26)
        blackframe_width=wx
        blackframe_height=int(height*0.64)
        
        blackframe_x_place=int(height*0.13)
        blackframe_y_place=int(height*0.13)
        frame=Frame(self.fnc_frame, bg="#ffffff")
        frame.place(x=int(blackframe_x_place),y=int(blackframe_y_place), width=int(blackframe_width), height=int(blackframe_height))

        img6=Image.open("uname.jpg")
        img6=img6.resize((int(width*0.25),int(width* 0.25)),Image.ADAPTIVE)
        self.photoimg6=ImageTk.PhotoImage(img6)
        lblimg6=Label(frame,image=self.photoimg6)
        lblimg6.place(x=int(width*0.06),y=int(width*0.055),height=int(width*0.25),width=int(width*0.25))

        entity_width=int(blackframe_width*0.3)
        entity_start=int(blackframe_width*0.58)
        entity_login=int(blackframe_width*0.68)
        login_width=int(blackframe_width*0.1)
        user_pass_lable_start=int(blackframe_width*0.58)
        user_lable_height=int(blackframe_height*0.25)
        user_entity_height=int(blackframe_height*0.33)
        pass_lable_height=int(blackframe_height*0.46)
        pass_entity_height=int(blackframe_height*0.54)
        login_entity_height=int(blackframe_height*0.73)
        login_height=int(blackframe_width*0.05)
        
        font_size=int(blackframe_width*0.02)
        
        entity_show=int(blackframe_width*0.78)
        show_entity_height=int(blackframe_height*0.66)

        def login():
            if self.txt_pswd.get()=="" or self.txt_user.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            elif self.txt_pswd.get()!="Login@123" or self.txt_user.get()!="admin":
                messagebox.showerror("Error","Invalid Username/Password",parent=self.root)
            else:
                self.root.quit
                self.root.destroy()
                os.system('python customer.py')

        def login_(Event):
            if self.txt_pswd.get()=="" or self.txt_user.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            elif self.txt_pswd.get()!="Login@123" or self.txt_user.get()!="admin":
                messagebox.showerror("Error","Invalid Username/Password",parent=self.root)
            else:
                self.root.quit
                self.root.destroy()
                os.system('python to do list/to_do.py')

        lbl_user=Label(frame,text="Username",font=("times new roman",int(font_size), "bold"), fg="black", bg="#ffffff")
        lbl_user.place(x=int(user_pass_lable_start),y=int(user_lable_height))

        self.txt_user=Entry(frame,font=("times new roman",int(font_size), "bold"))
        self.txt_user.place(x=int(entity_start), y=int(user_entity_height), width=int(entity_width))
        self.txt_user.bind('<Return>', login_)

        lbl_pswd=Label(frame,text="Password",font=("times new roman",int(font_size), "bold"), fg="black", bg="#ffffff")
        lbl_pswd.place(x=int(user_pass_lable_start), y=int(pass_lable_height))

        self.txt_pswd=Entry(frame,font=("times new roman",int(font_size), "bold"),show="\u2022")
        self.txt_pswd.place(x=int(entity_start), y=int(pass_entity_height), width=int(entity_width))
        self.txt_pswd.bind('<Return>', login_)
        a=0
        check=Checkbutton(frame,text="Show Password",bg="#ffffff",fg="black",activebackground="#f2fdff",activeforeground="black",variable=a,onvalue=1,offvalue=0,command=self.show_hide)
        check.place(x=int(entity_show), y=int(show_entity_height))
        
        self.login_btn=Button(frame,text="LOGIN",font=("arial",16),width=14,height=1,cursor="hand2",fg="#000000",bg="#ffffff",command=login)
        self.login_btn.place(x=int(entity_login), y=int(login_entity_height), width=int(login_width), height=int(login_height))

        


    def show_hide(self):
        if self.txt_pswd.cget('show') == '':
            self.txt_pswd.config(show='\u2022')
        else:
            self.txt_pswd.config(show='')
    
if __name__ == '__main__':
    root=Tk()
    obj=To_do_list(root)
    root.mainloop()
