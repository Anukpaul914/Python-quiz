from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import random
import json
'''questions = [
     "1.How many Keywords are there in C Programming language ?",
     "2.Which of the following functions takes A console Input in Python ?",
     "3.Which of the following is the capital of India ?",
     "4.Which of The Following is must to Execute a Python Code ?",
     "5.The Taj Mahal is located in  ?",
     "6.The append Method adds value to the list at the  ?",
     "7.Which of the following is not a costal city of india ?",
     "8.Which of The following is executed in browser(client side) ?",
     "9.Which of the following keyword is used to create a function in Python ?",
     "10.To Declare a Global variable in python we use the keyword ?"
    ]
answers_choice = [
     ["23","32","33","43",],
     ["get()","input()","gets()","scan()",],
     ["Mumbai","Delhi","Chennai","Lucknow",],
     ["TURBO C","Py Interpreter","Notepad","IDE",],
     ["Patna","Delhi","Benaras","Agra",],
     ["custom location","end","center","beginning",],
     ["Bengluru","Kochin","Mumbai","vishakhapatnam",],
     ["perl","css","python","java",],
     ["function","void","fun","def",],
     ["all","var","let","global",]
    ] '''
with open('./data.json', encoding="utf8") as f:
    data = json.load(f)
questions = [v for v in data[0].values()]
answers_choice = [v for v in data[1].values()]
ans = [1,1,1,1,3,1,0,1,3,3,3]
u_ans = []
indexes = []
def gen():
    global indexes
    while(len(indexes)<5):
        x = random.randint(0,9)
        
        if x in indexes:
            continue
        else:
            indexes.append(x)
            
    #print(indexes)
def show(score):
    label_quest.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    
    label_imgvpoor = Label(window,background = "white")
    label_imgvpoor.pack(pady=(50,0))    
    label_txt = Label(window,font=("Verdana",24,"bold"),background = "#ffffff")
    label_txt.pack() 
    
    label_imgavg = Label(window,background = "white")
    label_imgavg.pack(pady=(50,0))
    label_txt = Label(window,font=("Verdana",24,"bold"),background = "#ffffff")
    label_txt.pack()
    
    label_imgexcel = Label(window,background = "white")
    label_imgexcel.pack(pady=(0,50))
    label_txt = Label(window,font=("Verdana",24,"bold"),background = "#ffffff")
    label_txt.pack()

    if score>=20:
        img7 = ImageTk.PhotoImage(file="imgexcel.jpg")
        label_imgexcel.configure(image=img7)
        label_imgexcel.image = img7
        
        #label_txt.configure(text="Excellent")
    elif score>=10 and score<20:
        img6 = ImageTk.PhotoImage(file="imgavg.jpg")
        label_imgavg.configure(image=img6)
        label_imgavg.image = img6
        #label_txt.configure(text="Average")
    else:
        img3 = ImageTk.PhotoImage(file="imgvpoor.jpg")
        label_imgvpoor.configure(image=img3)
        label_imgvpoor.image = img3
        #label_txt.configure(text="Better luck next time")
def calc():
    global indexes,u_ans,ans
    x = 0
    score = 0
    for i in indexes:
        if u_ans[x] == ans[i]:
            score = score+5
        x += 1
    print(score)
    show(score)

q = 1
def selected():
    global label_quest,radiovar,r1,r2,r3,r4,u_ans,q
    
    x = radiovar.get()
    #print(x)
    u_ans.append(x)
    radiovar.set(-1)
    if q < 5:
        #show next question
        label_quest.config(text=questions[indexes[q]])
        r1['text'] = answers_choice[indexes[q]][0]
        r2['text'] = answers_choice[indexes[q]][1]
        r3['text'] = answers_choice[indexes[q]][2]
        r4['text'] = answers_choice[indexes[q]][3]
        q += 1
    else:
        print(indexes)
        print(u_ans)
        calc()
        
def quiz():
    global label_quest,radiovar,r1,r2,r3,r4
    label_quest =  Label(window,text=questions[indexes[0]],font=("Verdana",12),width=500,background="white",justify="center",wraplength=400)
    label_quest.pack(pady=(100,30))
    radiovar = IntVar()
    radiovar.set(-1)
    r1 = Radiobutton(window,text=answers_choice[indexes[0]][0],font=("Verdana",10),value=0,variable=radiovar,command=selected,background="white")
    r1.pack(pady=5)
    r2 = Radiobutton(window,text=answers_choice[indexes[0]][1],font=("Verdana",10),value=1,variable=radiovar,command=selected,background="white")
    r2.pack(pady=5)
    r3 = Radiobutton(window,text=answers_choice[indexes[0]][2],font=("Verdana",10),value=2,variable=radiovar,command=selected,background="white")
    r3.pack(pady=5)
    r4 = Radiobutton(window,text=answers_choice[indexes[0]][3],font=("Verdana",10),value=3,variable=radiovar,command=selected,background="white")
    r4.pack(pady=5)
   
def startfun():
    label_img.destroy()
    #label_txt.destroy()
    label_ins.destroy()
    label_rules.destroy()
    btnstart.destroy()
    gen()
    quiz()
window = Tk()
window.title("Quiz")
window.geometry('700x600')
window.resizable(0,0)
window.configure(background = "#ffffff")
img1 = ImageTk.PhotoImage(file="image1.jpg")
label_img = Label(window,image=img1,background = "#ffffff")
label_img.pack(pady=(40,0))
#label_txt = Label(window,text="QUIZ",font=("Verdana",24,"bold"),background = "#ffffff")
#label_txt.pack(pady=(0,50))
img2 = ImageTk.PhotoImage(file="image2.jpg")
btnstart = Button(window,image=img2,relief=FLAT,border=0,command=startfun)
btnstart.pack(pady=(50,0))
label_ins = Label(window,text="Read the rules \n and click the start once you are ready",font=("Verdana",14),background = "#ffffff",justify="center")
label_ins.pack(pady=(10,100))
label_rules = Label(window,text="This quiz contain 5 questions \n You will get 5 points for each correct answer \n There is no negative mark for wrong answers \n Once you select a radio button, it will be the final choice. \n Hence, think before you select",font=("Verdana",14),background = "#000000",foreground="yellow",width=100)
label_rules.pack()
window.mainloop()
