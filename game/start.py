from tkinter import *
from tkinter import ttk
import random
from PIL import ImageTk,Image
from tkinter import messagebox

class Game:

    def __init__(self,root):
        self.root = root
        width=root.winfo_screenwidth()
        height=root.winfo_screenheight()
        
        self.root.geometry("%dx%d+0+0"%(width*0.5125,height*0.4))
        self.root.title("Rock Paper Scissors")
        self.root.resizable(False,False)
        self.root.configure(background="#FFFFDD")

        title_head=Label(self.root,text="Rock Paper Scissors",fg="red",font=("Arial ",26,"bold"),bg="#FFFFDD")
        title_head.place(y=int(height*0.01),x=int(width*0.14))

        def main():

            main_frame=Frame(self.root,bg="#FFFFDD",height=int(height*0.4),width=int(width*0.4))
            main_frame.place(x=int(width*0.003),y=int(height*0.1))

            lbl_player=Label(main_frame,text="Player",font=("",14,"bold"),bg="#FFFFDD",fg="#020450",height=int(height*0.0043),width=int(width*0.01))
            lbl_player.grid(row=0,column=0)

            lbl_vs=Label(main_frame,text="VS",font=("",30,"bold"),bg="#FFFFDD")
            lbl_vs.grid(row=0,column=1,padx=int(width*0.02))

            lbl_cmp=Label(main_frame,text="Computer",font=("",14,"bold"),bg="#FFFFDD",fg="#186714",height=int(height*0.0043),width=int(width*0.01))
            lbl_cmp.grid(row=0,column=2)

            lbl_result=Label(main_frame,text="Result",font=("",16,"bold"),bg="#FFFFDD",height=int(height*0.003),width=int(width*0.022),highlightthickness=2)
            lbl_result.grid(row=1,column=0,columnspan=3,pady=int(width*0.01))
            lbl_result.config(highlightcolor="black",highlightbackground="black")

            score_frame=Frame(self.root,bg="#FFFFDD",height=int(height*0.4),width=int(width*0.4))
            score_frame.place(x=int(width*0.33),y=int(height*0.1))

            lbl_head=Label(score_frame,text="Scoreboard",font=("",14,"bold"),bg="#FFFFDD",borderwidth=2,relief="groove",height=int(height*0.0024),width=int(width*0.013))
            lbl_head.grid(row=0,column=0,columnspan=2)

            lbl_scpl=Label(score_frame,text="Player",font=("",14,"bold"),bg="#D1D6EF",borderwidth=2,relief="groove",height=int(height*0.0023),width=int(width*0.00651))
            lbl_scpl.grid(row=1,column=0)

            lbl_scmp=Label(score_frame,text="Computer",font=("",14,"bold"),bg="#BEF2AA",borderwidth=2,relief="groove",height=int(height*0.0023),width=int(width*0.00651))
            lbl_scmp.grid(row=1,column=1)

            player_sc=Label(score_frame,text="0",font=("",14,"bold"),bg="#FFFFDD",fg="#020450",borderwidth=2,relief="groove",height=int(height*0.0023),width=int(width*0.00651))
            player_sc.grid(row=2,column=0)

            cmp_sc=Label(score_frame,text="0",font=("",14,"bold"),bg="#FFFFDD",fg="#186714",borderwidth=2,relief="groove",height=int(height*0.0023),width=int(width*0.00651))
            cmp_sc.grid(row=2,column=1)


            def is_rock():
                lbl_player.config(text="Rock")
                computer_choice = random.choice(["Rock","Paper","Scissors"])
                if computer_choice == "Rock":
                    lbl_cmp.config(text="Rock")
                    lbl_result.config(text="It's a tie!")
                    lbl_result.config(highlightcolor="red",highlightbackground="red")
                elif computer_choice == "Paper":
                    lbl_cmp.config(text="Paper")
                    lbl_result.config(text="Computer wins!")
                    cmp_sc.config(text=str(int(cmp_sc.cget("text"))+1))
                    lbl_result.config(highlightcolor="#186714",highlightbackground="#186714")
                else:
                    lbl_cmp.config(text="Scissors")
                    lbl_result.config(text="Player wins!")
                    player_sc.config(text=str(int(player_sc.cget("text"))+1))
                    lbl_result.config(highlightcolor="#020450",highlightbackground="#020450")

            def is_paper():
                lbl_player.config(text="Paper")
                computer_choice = random.choice(["Rock","Paper","Scissors"])
                if computer_choice == "Rock":
                    lbl_cmp.config(text="Rock")
                    lbl_result.config(text="Player wins!")
                    player_sc.config(text=str(int(player_sc.cget("text"))+1))
                    lbl_result.config(highlightcolor="#020450",highlightbackground="#020450")
                elif computer_choice == "Paper":
                    lbl_cmp.config(text="Paper")
                    lbl_result.config(text="It's a tie!")
                    lbl_result.config(highlightcolor="red",highlightbackground="red")
                else:
                    lbl_cmp.config(text="Scissors")
                    lbl_result.config(text="Computer wins!")
                    cmp_sc.config(text=str(int(cmp_sc.cget("text"))+1))
                    lbl_result.config(highlightcolor="#186714",highlightbackground="#186714")
            
            def is_scissors():
                lbl_player.config(text="Scissors")
                computer_choice = random.choice(["Rock","Paper","Scissors"])
                if computer_choice == "Rock":
                    lbl_cmp.config(text="Rock")
                    lbl_result.config(text="Computer wins!")
                    cmp_sc.config(text=str(int(cmp_sc.cget("text"))+1))
                    lbl_result.config(highlightcolor="#186714",highlightbackground="#186714")
                elif computer_choice == "Paper":
                    lbl_cmp.config(text="Paper")
                    lbl_result.config(text="Player wins!")
                    player_sc.config(text=str(int(player_sc.cget("text"))+1))
                    lbl_result.config(highlightcolor="#020450",highlightbackground="#020450")
                else:
                    lbl_cmp.config(text="Scissors")
                    lbl_result.config(text="It's a tie!")
                    lbl_result.config(highlightcolor="red",highlightbackground="red")

            def end_game():
                main_frame.destroy()
                btn_end.destroy()

                score_frame.place(x=int(width*0.18))

                final_result=""

                lbl_final=Label(score_frame,text=f"{final_result}",font=("",13,"bold"),bg="#FFFFDD",height=int(height*0.0024),width=int(width*0.0145),highlightthickness=2,highlightcolor="black",highlightbackground="black")
                lbl_final.grid(row=3,column=0,columnspan=2,pady=int(width*0.005))


                if int(player_sc.cget("text")) > int(cmp_sc.cget("text")):
                    final_result="Player wins the game!"
                    lbl_final.config(text=final_result,highlightcolor="#020450",highlightbackground="#020450")
                elif int(player_sc.cget("text")) < int(cmp_sc.cget("text")):
                    final_result="Computer wins the game!"
                    lbl_final.config(text=final_result,highlightcolor="#186714",highlightbackground="#186714")
                else:
                    final_result="It's a tie game!"
                    lbl_final.config(text=final_result,highlightcolor="red",highlightbackground="red")

            
            def new_game():
                main_frame.destroy()
                score_frame.destroy()
                main()       


            #buttons
            btn_end=Button(score_frame,bg="#F51414",text="End Game",font=("",16,"bold"),command=end_game,fg="#fff",height=int(height*0.001),width=int(width*0.008))
            btn_end.grid(row=3,column=0,columnspan=2,pady=int(width*0.005))

            btn_new=Button(score_frame,bg="#F51414",text="New Game",font=("",16,"bold"),command=new_game,fg="#fff",height=int(height*0.001),width=int(width*0.008))
            btn_new.grid(row=4,column=0,columnspan=2)

            btn_frame=Frame(main_frame,bg="#FFFFDD")
            btn_frame.grid(row=2,column=0,columnspan=3)

            btn_rock=Button(btn_frame,bg="#F51414",text="Rock",font=("",16,"bold"),command=is_rock,fg="#fff",height=int(height*0.001),width=int(width*0.005))
            btn_rock.grid(row=2,column=0,padx=int(width*0.005))

            btn_ppr=Button(btn_frame,bg="#F51414",text="Paper",font=("",16,"bold"),command=is_paper,fg="#fff",height=int(height*0.001),width=int(width*0.005))
            btn_ppr.grid(row=2,column=1,padx=int(width*0.005))

            btn_scr=Button(btn_frame,bg="#F51414",text="Scissors",font=("",16,"bold"),command=is_scissors,fg="#fff",height=int(height*0.001),width=int(width*0.005))
            btn_scr.grid(row=2,column=2,padx=int(width*0.005))

        main()

if __name__ == '__main__':
    root=Tk()
    obj=Game(root)
    root.mainloop()