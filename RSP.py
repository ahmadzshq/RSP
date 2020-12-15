import tkinter as tK

import random

root = tK.Tk()
root.geometry('700x700')
root.resizable(0,0)
root.title('RPS')
root.config(bg='seashell3')


user_take=tK.StringVar()
L1 = tK.Label(root, text='choose: rock, paper, scissors',
    font='arial 15 bold', 
    bg = 'seashell2')
L1.place(x= 20, y=70)
E1 = tK.Entry(root, font = 'arial 15 bold', 
    textvariable = user_take,
    bg='seashell2')
E1.place(x=90, y=130)


comp_pick = random.randint(1,3)
if comp_pick == 1:
    comp_pick = 'rock'
elif comp_pick ==2:
    comp_pick = 'paper'
else:
    comp_pick = 'scissors'

Result = tK.StringVar()
Result.set('invalid: choose any one -- rock, paper, scissors')

E2 = tK.Entry(root, font = 'arial 15 bold',
     textvariable = Result,
     bg = 'seashell2',
     width = len(Result.get()) )
E2.place(x=90, y=190)



def play():
    user_pick = user_take.get()
    if user_pick == comp_pick:
        Result.set('tie,you both select same')
    elif user_pick == 'rock' and comp_pick == 'paper':
        Result.set('you loose,computer select paper')
    elif user_pick == 'rock' and comp_pick == 'scissors':
        Result.set('you win,computer select scissors')
    elif user_pick == 'paper' and comp_pick == 'scissors':
        Result.set('you loose,computer select scissors')
    elif user_pick == 'paper' and comp_pick == 'rock':
        Result.set('you win,computer select rock')
    elif user_pick == 'scissors' and comp_pick == 'rock':
        Result.set('you loose,computer select rock')
    elif user_pick == 'scissors' and comp_pick == 'paper':
        Result.set('you win ,computer select paper')
    else:
        Result.set('invalid: choose any one -- rock, paper, scissors')

tK.Button(root, font = 'arial 13 bold', text = 'PLAY'  ,padx =5,bg ='seashell4' ,command = play).place(x=150,y=250)



root.mainloop()