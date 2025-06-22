import tkinter as tk
from tkinter import ttk
import random
from tkinter import messagebox
from sqlbackend import *
from ui2 import *


def run():
    win = tk.Tk()

    win.title('Gym Membership Management System ')
    win.geometry('1500x1500')
    win.config(bg = 'lightblue')

    image = tk.PhotoImage(file="title.png")
    label_image = tk.Label(win,image=image,height=75,width=160)
    label_image.place(x = 700,y = 20)

    label_title= tk.Label(win,text = "Welcome to SRU Gym",bg = 'lightblue',font=('Times New Roman', 30, 'bold'))
    label_title.place(x = 600,y = 125)

    label_title_new_entry = tk.Label(win,text="Add new entry",bg = 'lightblue',font=('Times New Roman',25))
    label_title_new_entry.place(x = 400,y = 200)

    label_new_entery = tk.Label(win,text='Enter your name')
    label_new_entery.place(x = 400,y = 270)

    label_age = tk.Label(win,text='Enter you age')
    label_age.place(x = 400,y = 320)

    label_email_id = tk.Label(win,text="Enter your Email_id")
    label_email_id.place(x = 400,y = 370)

    label_branch = tk.Label(win,text = "choose yor course")
    label_branch.place(x = 850 ,y = 320 )

    label_roll_no = tk.Label(win,text="Enter rollno")
    label_roll_no.place(x = 850,y = 270)


    label_phone_num = tk.Label(win,text='Enter your phone num')
    label_phone_num.place(x = 400,y = 420)

    label_uniue_code = tk.Label(win,text='your unique code')
    label_uniue_code.place(x =850,y= 370)

    def get_name():
        name = entry_name.get()
        if name:
            return name
        else:
            messagebox.showinfo('error','please enter name')

    
    def get_age():
        age = entry_age.get()
        try:
            if int(age):
                pass
        except ValueError:
                messagebox.showerror('error','enter a valid age')
                entry_age.delete(0,tk.END)
        if int(age) < 100 and int(age) > 10:
            return age
        else:
            messagebox.showinfo('error','sorry your age should be between 10 - 100')
    
    def get_email_id():
        email_id = entry_email_id.get()

        if email_id[len(email_id)-10::] != '@gmail.com' and len(email_id) < 10:
            entry_email_id.delete(0,tk.END)
            entry_email_id.insert(0,'please enter a valid email_id')
        else:
            return email_id 
            
    def get_roll_no():
        roll_no = entry_roll_no.get()

        if len(roll_no) < 10 or len(roll_no) > 10:
            messagebox.showinfo('error',"invalid roll_no num")
        elif len(roll_no) == 10:
            return roll_no


    def get_course_details():
        course = combo_box_for_courses.get()
        if course:
            return course
        else:
            combo_box_for_courses.insert(0,'please coose a course')
    
    def get_phone_num():
        phone_num = entry_phone_num.get()

        if len(phone_num) < 10 or len(phone_num) > 10:
            messagebox.showinfo('error','invalid phonum')
            entry_phone_num.delete(0,tk.END)

        elif len (phone_num) == 10:
            return phone_num
    
    def all_commands():
        name = get_name()
        age = get_age()
        email_id = get_email_id()
        roll_no = get_roll_no()
        course = get_course_details()
        phone_num = get_phone_num()
        
        def show_pop_up():
            if name and age and email_id and roll_no and course and phone_num:
                messagebox.showinfo("Welcome",f"your account is created your unique code {unique_code}")
                reset_all()
            else:
                # messagebox.showinfo("info","your credentials are wrong")
                if not name and not age and not email_id and not roll_no and not course  and not phone_num:
                    reset_all()
                else:
                    if not name:
                        entry_name.delete(0,tk.END)
                    if not age:
                        entry_age.delete(0,tk.END)
                    if not email_id:
                        entry_email_id.delete(0,tk.END)
                    if not roll_no:
                        entry_roll_no.delete(0,tk.END)
                    if not course:
                        combo_box_for_courses.delete(0,tk.END)
                    if not phone_num:
                        entry_phone_num.delete(0,tk.END) 

        def insert_into_unique_code():
            if name and age and email_id and roll_no and course  and phone_num:
                entry_unique_code.delete(0,tk.END )
                entry_unique_code.insert(0,unique_code)
            else:
                entry_unique_code.delete(0,tk.END)
                entry_unique_code.insert(0,'please enter valid credentials')

        
        insert_into_unique_code()
        show_pop_up()

        if name and age and email_id and roll_no and course  and phone_num and unique_code:
            conn = get_connection1()
            cursor = conn.cursor()

            query = "INSERT INTO basicinfo(name,age,email_id,roll_no,course_details,phone_num,unique_code) VALUES(%s,%s,%s,%s,%s,%s,%s)"

            data = (name,age,email_id,roll_no,course,phone_num,unique_code)

            cursor.execute(query,data)
            conn.commit()

            cursor.close()  
            conn.close() 
    
    def reset_all():
        entry_name.delete(0,tk.END)
        entry_age.delete(0,tk.END)
        entry_email_id.delete(0,tk.END)
        entry_roll_no.delete(0,tk.END)
        entry_phone_num.delete(0,tk.END)
        entry_unique_code.delete(0,tk.END)
        combo_box_for_courses.set('')


    entry_name = tk.Entry(win,width=30)
    entry_name.place(x = 500,y = 270)

    entry_age = tk.Entry(win,width=30)
    entry_age.place(x = 500,y = 320)

    entry_email_id = tk.Entry(win,width=35)
    entry_email_id.place(x = 525,y = 370)

    entry_roll_no = tk.Entry(win,width=30)
    entry_roll_no.place(x = 970 ,y = 270)

    combo_box_for_courses = ttk.Combobox(win,values=['b.tech','m.tech','Agriculture','BBA','MBA'],width=30)
    combo_box_for_courses.place(x = 970,y = 320)

    entry_phone_num = tk.Entry(win,width=30)
    entry_phone_num.place(x=540,y = 420)

    entry_unique_code = tk.Entry(win,width=30)
    entry_unique_code.place(x= 970,y = 370)

    if get_name:
        unique_code = ""
        for _ in range(4):
            random_num = random.randint(1,9)
            unique_code += str(random_num)


    button = tk.Button(win,text="submit",command=all_commands)
    button.place(x = 750,y = 500)

    def login():
        run1()
 
    button_for_reset = tk.Button(win,text="Login",command=login)
    button_for_reset.place(x = 825,y = 500)

    win.mainloop()
