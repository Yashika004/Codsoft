import random
import pyperclip
from tkinter import *
from tkinter import ttk


def create():

	txt_pass.delete(0, END)

	length = int(txt_len.get())

	alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
	alnum = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
	alnumsym = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
	password = ""

	if var_radio.get() == 1:
		for i in range(0, length):
			password = password + random.choice(alphabets)
		return password

	elif var_radio.get() == 2:
		for i in range(0, length):
			password = password + random.choice(alnumsym)
		return password

	else:
		for i in range(0, length):
			password = password + random.choice(alnum)
		return password


def gen_pass():

	if txt_len.get().isdigit()==False and txt_len.get()!="":
		lbl_warn.config(text="Error: Length must be a number",fg="red")

	elif txt_len.get()=="":
		lbl_warn.config(text="Please enter the length of the password",fg="red")

	elif int(txt_len.get())<8:

		lbl_warn.config(text="Password Length should be atleast 8 characters",fg="red")

		txt_pass["state"]="normal"
		txt_pass.delete(0, END)
		txt_pass["state"]="disabled"

	elif int(txt_len.get())>15:
		lbl_warn.config(text="Password Length should not exceed 15 characters",fg="red")

	else:
		password1 = create()

		txt_pass["state"]="normal"
		txt_pass.delete(0, END)
		txt_pass.insert(0,password1)
		txt_pass["state"]="disabled"

		lbl_warn.config(text="")

def gen_pass_ev(Event):
	gen_pass()


def copy_pass():
	pyperclip.copy(txt_pass.get())

	txt_pass["state"]="normal"
	txt_pass.delete(0, END)
	txt_pass["state"]="disabled"

	txt_len.delete(0,END)
	txt_len.insert(0,"8")


# Main Function
root = Tk()

width=root.winfo_screenwidth()
height=root.winfo_screenheight()

root.title("Random Password Generator")
root.geometry("%dx%d+0+0"%(width*0.23,height*0.1))
root.resizable(False,False)
root.config(background="#BBE089")

var_radio = IntVar()


main_frame=Frame(root,bg="#BBE089")
main_frame.place(x=int(width*0.01),y=int(height*0.01))

lbl_len = Label(main_frame, text="Length",bg="#BBE089")
lbl_len.grid(row=0,column=0)

txt_len = Entry(main_frame,width=6,bg="#F0FAD7")
txt_len.insert(0,"8")
txt_len.grid(row=0,column=1)
txt_len.bind('<Return>', gen_pass_ev)

lbl_pass = Label(main_frame, text="Password",bg="#BBE089")
lbl_pass.grid(row=1,column=0)

txt_pass = Entry(main_frame,bg="#F0FAD7")
txt_pass.grid(row=1,column=1,columnspan=2)
txt_pass["state"]="readonly"

lbl_warn=Label(main_frame,bg="#BBE089")
lbl_warn.grid(row=2,column=0,columnspan=5)

radio_easy = Radiobutton(main_frame, text="Easy", variable=var_radio, value=1,bg="#BBE089")
radio_easy.grid(row=0, column=2, sticky='E')
radio_medium = Radiobutton(main_frame, text="Medium", variable=var_radio, value=0,bg="#BBE089")
radio_medium.grid(row=0, column=3, sticky='E')
radio_strong = Radiobutton(main_frame, text="Strong", variable=var_radio, value=2,bg="#BBE089")
radio_strong.grid(row=0, column=4, sticky='E')

btn_copy = Button(main_frame, text="Copy", command=copy_pass,bg="#F7FFD6")
btn_copy.grid(row=1, column=3)

gen_btn = Button(main_frame, text="Generate", command=gen_pass,bg="#F7FFD6")
gen_btn.grid(row=1, column=4)

root.mainloop()