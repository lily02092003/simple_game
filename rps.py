from tkinter import *
import random
computer=random.choice(['R','S','P'])
def play():
    global text
    user=entry_window.get()
    if user==computer:
        text.set("IT IS A TIE!")
        btn_play.pack_forget()
    elif iswin(user,computer):
        text.set("YOU WIN!\n USER: "+str(user)+ "\nCOMPUTER: "+str(computer))
        btn_play.pack_forget()
    else:
        text.set("YOU LOSE!\n USER: "+str(user)+ "\nCOMPUTER: "+str(computer))
        #btn_play.pack_forget()
def iswin(user,computer):
    if (user=='R' and computer=='S') or (user=='S' and computer=='P') or (user=='P' and computer=='R'):
        return True
    return False
root=Tk()
root.title("ROCK PAPER SCISSORS")
root.geometry("500x150")
label1= Label(root,text='ENTER ROCK:R, PAPER:P , SCISSORS:S')
label1.pack()
entry_window=Entry(root,width=50,borderwidth=5)
entry_window.pack()
btn_play=Button(root,text="Play",command=play)
btn_play.pack()
btn_quit=Button(root,text='Quit',command=root.destroy)
btn_quit.pack()
text=StringVar()
text.set("")
guess_attempts=Label(root,textvariable=text)
guess_attempts.pack()
root.mainloop()