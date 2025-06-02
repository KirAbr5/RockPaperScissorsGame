import random
import tkinter as tk

window = tk.Tk()
window.geometry("500x400")
window.title("Игра Камень-Ножицы-Бумага")
window.configure(bg='#abc4ff')

USER_SCORE = 0
COMP_SCORE = 0
USER_CHOICE = ""
COMP_CHOICE = ""

def choice_to_number(choice):
    rps = {'камень':0,'бумага':1,'ножницы':2}
    return rps[choice]
def number_to_choice(number):
    rps = {0:'камень',1:'бумага',2:'ножницы'}
    return rps[number]
def random_pc_choice():
    return random.choice(['камень','бумага','ножницы'])
def result(human_choice,comp_choice):
    global USER_SCORE
    global COMP_SCORE
    user=choice_to_number(human_choice)
    comp=choice_to_number(comp_choice)
    if(user==comp):
        print("Ничья")
    elif((user-comp)%3==1):
        print("Игрок выиграл")
        USER_SCORE+=1
    else:
        print("Компьтер выиграл")
        COMP_SCORE+=1
    text_area = tk.Text(master=window,height=12,width=30,bg="#edf2fa")
    text_area.grid(column=0,row=4)
    answer = "Твой выбор: {uc} \nВыбор компьютера : {cc} \n Твой рекорд : {u} \n Рекорд компьютера : {c} ".format(uc=USER_CHOICE,cc=COMP_CHOICE,u=USER_SCORE,c=COMP_SCORE)
    text_area.insert(tk.END,answer)
def rock():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='камень'
    COMP_CHOICE=random_pc_choice()
    result(USER_CHOICE,COMP_CHOICE)
def paper():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='бумага'
    COMP_CHOICE=random_pc_choice()
    result(USER_CHOICE,COMP_CHOICE)
def scissor():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='ножницы'
    COMP_CHOICE=random_pc_choice()
    result(USER_CHOICE,COMP_CHOICE)
window.grid_rowconfigure((0,1,2,3,4,5), weight=1)
window.grid_columnconfigure(0, weight=1)
button1 = tk.Button(text="       Камень 🗿       ",bg="#d7e3fc",command=rock)
button1.grid(column=0,row=1)
button2 = tk.Button(text="       Бумага 📃      ",bg="#ccdbfd",command=paper)
button2.grid(column=0,row=2)
button3 = tk.Button(text="      Ножницы ✂️     ",bg="#c1d3fe",command=scissor)
button3.grid(column=0,row=3)

window.mainloop()