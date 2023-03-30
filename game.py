from tkinter import *
import random
attempts=5
answer=random.randint(1,10)
def guessgame():
    global attempts
    global text
    attempts-=1
    guess=int(entry_window.get())
    if answer==guess:
        text.set("YOU WIN!! THE NUMBER WAS "+str(guess))
        btn_check.pack_forget()
    elif attempts==0:
        text.set("YOU HAVE EXHAUSTED ALL YOUR ATTEMPTS!!")
        btn_check.pack_forget()
    elif guess<answer:
        text.set("INCORRECT! YOU HAVE "+str(attempts)+"attempts left. THINK HIGHER!! ")
    elif guess>answer:
           text.set("INCORRECT! YOU HAVE "+str(attempts)+"attempts left. THINK LOWER!! ")
root=Tk()
root.title("Guess the Number")
root.geometry("500x150")
label1= Label(root,text='Guess a number between 1 to 10')
label1.pack()
entry_window=Entry(root,width=50,borderwidth=5)
entry_window.pack()
btn_check=Button(root,text="Check",command=guessgame)
btn_check.pack()
btn_quit=Button(root,text='Quit',command=root.destroy)
btn_quit.pack()
text=StringVar()
text.set("YOU HAVE 5 attempts!")
guess_attempts=Label(root,textvariable=text)
guess_attempts.pack()
root.mainloop()