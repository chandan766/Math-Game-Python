from tkinter import * 
from tkinter import messagebox
import random
import time

def on_closing():
    global true 
    global false 
    if messagebox.showinfo("Score",f"Your total score is {true-false}"):
        win.destroy()

def q_btn():
    global result
    lbl_count_lbl.place_forget()
    lbl_count.place_forget()
    lbl5['text']=""
    lbl6['text']=""
    ans.set("")
    operator = ['+','-','x','÷']
    gen_op1 = random.randint(1,1000)
    op = random.randint(0,3)
    gen_opr = operator[op]
    op1 = str(gen_op1)
    gen_op3 = random.randint(1,1000)
    while((gen_op1< gen_op3)and(gen_opr=="-" or "÷") or gen_op1%gen_op3 != 0):
        gen_op3 = random.randint(1,1000)


    op3 = str(gen_op3)
    if gen_opr=='+':
        result1 = gen_op1+gen_op3
    elif gen_opr=='-':
        result1 = gen_op1-gen_op3
    elif gen_opr=='x':
        result1 = gen_op1*gen_op3
    elif gen_opr=='÷':
        result1 = gen_op1//gen_op3
    result = str(result1)
    lbl3.config(text=str(gen_op1)+gen_opr+str(gen_op3))
    entry.focus()
    
def check():
    global true 
    global false
    global second
    if ans.get() == "":
        pass
    else:
        if ans.get() == result:
            true += 1
            lbl6['text']=""
            lbl5['text']="True"
            lbl5['fg']="green"
            lbl9_entry["text"]=str(true)
        else:
            false += 1
            lbl5['text']="False"
            lbl5['fg'] = "red"
            lbl6['text']="The True ans is "+result
            lbl10_entry["text"]=str(false)
        second = 5
        clock_counter()

def clock_counter():
        global second
        if second == 0:
            q_btn()
        else:
            lbl_count_lbl.place(x=150,y=310)
            lbl_count.place(x=260,y=310,width=20)
            lbl_count.config(text= str(second))
            second -= 1
            win.after(1000,clock_counter)
        
def about():
    messagebox.showinfo("About","This software is developed by Chandan Maurya.\nFor any valuable feedback kindly mail me.\nEmail: cr3992@gmail.com")       
def on_enter_about(e):
    btn_about['fg']="red"
    btn_about.config(font=("times new roman",11,"bold"))
def on_leave_about(e):
    btn_about['fg']="brown"
    btn_about.config(font=("times new roman",10,"bold"))

def reset():
    global true 
    global false 
    true = 0
    false= 0
    lbl9_entry["text"] = ""
    lbl10_entry["text"] =""

def on_enter_reset(e):
    btn_reset['fg']="red"
    btn_reset.config(font=("times new roman",11,"bold"))
def on_leave_reset(e):
    btn_reset['fg']="brown"
    btn_reset.config(font=("times new roman",10,"bold"))



def press_enter(e):
    on_enter_chk(e)
    check()
    win.after(100,on_leave_chk,e)
def press_q(e):
    on_enter_q(e)
    q_btn()
    win.after(100,on_leave_q,e)
def on_enter_q(e):
    btn_q['bg']="blue"
    btn_q.config(font=("times new roman",13,"bold"))
def on_leave_q(e):
    btn_q['bg']="darkblue"
    btn_q.config(font=("times new roman",12,"bold"))
def on_enter_chk(e):
    btn_chk['bg']="darkblue"
    btn_chk.config(font=("times new roman",13,"bold"))
def on_leave_chk(e):
    btn_chk['bg']="blue"
    btn_chk.config(font=("times new roman",12,"bold"))

win = Tk()
ans = StringVar()

true = 0
false= 0
second = 5

win.title("Math Game")
win.config(bg="white")
win.geometry("480x360+400+200")
win.resizable(width=False, height=False)
lbl1 = Label(win,text="Math Game",bg="yellow",fg="purple",font=("arial",15,"bold"))
lbl1.pack(fill=X)
lbl2= Label(win,text="Tap on Q button to the Question",bg="white",fg="lightgray",font=("times new roman",8,"bold"))
lbl2.pack()
btn_q = Button(win,text="Q",bg="darkblue",fg="white",font=("times new roman",12,"bold"),activebackground="green",command=q_btn)
btn_q.place(x=40,y=80,width=70)
btn_q.bind("<Enter>",on_enter_q)
btn_q.bind("<Leave>",on_leave_q)
lbl3 = Label(win,text="",font=("times new roman",15,"bold"),bg="white")
lbl3.place(x=200,y=80)
lbl4 = Label(win,text="Type your answer here",font=("times new roman",12,"bold"),bg="orange",fg="brown")
lbl4.place(x=40,y=120)
entry = Entry(win,textvariable=ans,font=("times new roman",12,"bold"),bg="lightgray",justify=CENTER)
entry.place(x=200,y=120,width=80,height=26)
entry.focus()
btn_chk = Button(win,text="Check",bg="blue",fg="white",font=("times new roman",12,"bold"),activebackground="green",command=check)
btn_chk.place(x=200,y=150,width=70)
btn_chk.bind("<Enter>",on_enter_chk)
btn_chk.bind("<Leave>",on_leave_chk)
lbl5 = Label(win,text="",font=("times new roman",15,"bold"),bg="white")
lbl5.place(x=200,y=210)
lbl6 = Label(win,text="",font=("times new roman",12,"bold"),bg="white",fg="lightgray")
lbl6.place(x=200,y=240)
lbl7 = Label(win,text="Note:- Press Q button (from keyboard/mouse) for new question\n\tYour Total score is True - False",font=("times new roman",10,"bold"),bg="white",fg="gray")
lbl7.place(x=20,y=260)
lbl_count_lbl = Label(win,text="New Question:",font=("times new roman",12,"bold"),bg="white")
lbl_count_lbl.place(x=150,y=310)
lbl_count = Label(win,text="",font=("times new roman",12,"bold"),bg="gray",fg="black")
lbl_count.place(x=260,y=310,width=20)
lbl8 = Label(win,text="Score",font=("times new roman",15,"bold"),bg="black",fg="orange")
lbl8.place(x=360,y=80,width=95)
lbl9 = Label(win,text="True",font=("times new roman",15,"bold"),bg="white",fg="black")
lbl9.place(x=355,y=120)
lbl9_entry = Label(win,text="",font=("times new roman",12,"bold"),bg="green",fg="white")
lbl9_entry.place(x=405,y=120,width=50)
lbl10 = Label(win,text="False",font=("times new roman",15,"bold"),bg="white",fg="black")
lbl10.place(x=355,y=150)
lbl10_entry = Label(win,text="",font=("times new roman",12,"bold"),bg="red",fg="white")
lbl10_entry.place(x=405,y=150,width=50)
btn_about = Button(win,text="About",bg="white",bd=1,fg="brown",font=("times new roman",10,"bold"),activebackground="green",command=about)
btn_about.place(x=20,y=310)
btn_about.bind("<Enter>",on_enter_about)
btn_about.bind("<Leave>",on_leave_about)
btn_reset = Button(win,text="Reset Score",bg="white",bd=1,fg="brown",font=("times new roman",10,"bold"),activebackground="green",command=reset)
btn_reset.place(x=380,y=310)
btn_reset.bind("<Enter>",on_enter_reset)
btn_reset.bind("<Leave>",on_leave_reset)
win.bind("<Return>",press_enter)
win.bind("q",press_q)
win.protocol("WM_DELETE_WINDOW",on_closing)

q_btn()
win.mainloop()