import tkinter as tk
from tkinter import ttk
import random
from tkinter import messagebox
from datetime import datetime
from sqlbackend import *


def run():
    win = tk.Tk()
    curr_date_and_time = str(datetime.now())[:16]
    date = curr_date_and_time[:10]
    time = curr_date_and_time[10:16]

    win.title('Gym Membership Management System ')
    win.geometry('5000x5000')
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
   

    def get_workouts():
        
        workouts = combox_box_for_workouts.get()
        if workouts:
            return workouts
        else:
            combox_box_for_workouts.insert(0,'please coose a workout')
    

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
            cursor = conn.cursor()
            query = "INSERT INTO basicinfo(name,age,email_id,roll_no,course_details,phone_num,unique_code) VALUES(%s,%s,%s,%s,%s,%s,%s)"


            data = (name,age,email_id,roll_no,course,phone_num,unique_code)

            cursor.execute(query,data)
            conn.commit()

            cursor.close()  
            conn.close() 

            # win.destroy()
            # run()
    
    def reset_all():
        entry_name.delete(0,tk.END)
        entry_age.delete(0,tk.END)
        entry_email_id.delete(0,tk.END)
        entry_roll_no.delete(0,tk.END)
        entry_phone_num.delete(0,tk.END)
        entry_unique_code.delete(0,tk.END)
        combo_box_for_courses.set('')
    
    def reset_all_2():
        entry_get_total_details.delete(0,tk.END)
        combox_box_for_workouts.set('')
        entry_for_date_and_time.delete(0,tk.END)
        
    
    def get_unique_code():
        code = entry_get_total_details.get()
        if code:
            backend_operation()
        else:
            messagebox.showinfo('error','please provide unique code')
    

    def backend_operation():
        code = entry_get_total_details.get()
        conn = get_connection1()
        curser1 = conn.cursor()

        workouts = get_workouts()
        def get_streak():
            if code:
                conn1 = get_connection2()
                curser2 = conn1.cursor()
                quary2 = "INSERT IGNORE INTO streak_info(unique_code,date,time,workouts) VALUES(%s,%s,%s,%s)"
                data2 = (code,date,time,workouts)
                curser2.execute(quary2,data2)
                conn1.commit()

                quary3 = 'SELECT * FROM streak_info WHERE unique_code = %s'
                data3 = code
                curser2.execute(quary3,(data3,))
                info2 = curser2.fetchall()

                label_date_time = tk.Label(win,text='Date',bg = 'lightblue',font=('Times New Roman',15))
                label_date_time.place(x = 25,y=100)

                label_time = tk.Label(win,text='Time',bg = 'lightblue',font=('Times New Roman',15))
                label_time.place(x = 125,y=100)

                label_workouts_streak = tk.Label(win,text='Workouts',bg = 'lightblue',font=('Times New Roman',15))
                label_workouts_streak.place(x = 175,y=100)

                X,Y = int(25),int(125)

                for i in range(len(info2)):

                    label_dates = tk.Label(win,text=f"{info2[i][1]}",bg='lightblue',font=('Times New Roman',15))
                    label_dates.place(x = X,y = Y)

                    label_time_output = tk.Label(win,text=f"{info2[i][2]}",bg='lightblue',font=('Times New Roman',15))
                    label_time_output.place(x = (X+100),y = Y)

                    label_workouts_output = tk.Label(win,text=f"{info2[i][3]}",bg='lightblue',font=('Times New Roman',15))
                    label_workouts_output.place(x = (X+180),y = Y)
                    Y += 25

            curser2.close()  
            conn1.close()

        if workouts:
            quary1 = "SELECT * FROM basicinfo WHERE unique_code = %s"
            data1 = code
            curser1.execute(quary1,(data1,))
            info = curser1.fetchall()
        
            if info:

                label_output_name = tk.Label(win,text=f"Name : {info[0][0]}",bg='lightblue',font=('Times New Roman',15))
                label_output_name.place(x = 900,y = 640)

                label_output_age =tk.Label(win,text=f"Age: {info[0][1]}",bg='lightblue',font=('Times New Roman',15))
                label_output_age.place(x = 900,y = 665)

                label_output_emailid =tk.Label(win,text=f"Email_id: {info[0][2]}",bg='lightblue',font=('Times New Roman',15))
                label_output_emailid.place(x = 900,y = 690)

                label_output_roll_no =tk.Label(win,text=f"Roll_no: {info[0][3]}",bg='lightblue',font=('Times New Roman',15))
                label_output_roll_no.place(x = 900,y = 715)

                label_output_phonum =tk.Label(win,text=f"Phone_num: {info[0][5]}",bg='lightblue',font=('Times New Roman',15))
                label_output_phonum.place(x = 900,y = 740)

                label_output_coursedetails =tk.Label(win,text=f"Course Details: {info[0][4]}",bg='lightblue',font=('Times New Roman',15))
                label_output_coursedetails.place(x = 900,y = 765)

                label_output_age =tk.Label(win,text=f"Unique_code: {info[0][6]}",bg='lightblue',font=('Times New Roman',15))
                label_output_age.place(x = 1150,y = 640)

                label_date_and_time = tk.Label(win,text=f"Date & time  {curr_date_and_time}",bg='lightblue',font=('Times New Roman',15))
                label_date_and_time.place(x = 1150,y = 665 )

                button_for_streak = tk.Button(win,text='get complete streak',command=get_streak)
                button_for_streak.place(x = 1170,y = 700)

                entry_for_date_and_time.insert(0,curr_date_and_time)

                conn.commit()

                curser1.close()  

                conn.close() 

            else:
                messagebox.showinfo('error',f"no user,invalid unique code{code}")
                entry_get_total_details.delete(0,tk.END)

        
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

    combox_box_for_workouts = ttk.Combobox(win,values=['chest','back','arms','shoulders','legs','forearms'],width=30)
    combox_box_for_workouts.place(x = 550,y = 685)

    entry_phone_num = tk.Entry(win,width=30)
    entry_phone_num.place(x=540,y = 420)

    entry_unique_code = tk.Entry(win,width=30)
    entry_unique_code.place(x= 970,y = 370)

    entry_for_date_and_time = tk.Entry(win,width=20)
    entry_for_date_and_time.place(x = 515,y= 730)


    if get_name:
        unique_code = ""
        for _ in range(4):
            random_num = random.randint(1,9)
            unique_code += str(random_num)


    button = tk.Button(win,text="submit",command=all_commands)
    button.place(x = 750,y = 500)
 

    button_for_reset = tk.Button(win,text="Reset",command=reset_all)
    button_for_reset.place(x = 825,y = 500)

    button_for_reset2 = tk.Button(win,text='Reset',command=reset_all_2)
    button_for_reset2.place(x = 825,y=685)

    label_for_old_user = tk.Label(win,text="Already a user?get your details with unique code",bg="lightblue",font=('Times New Roman', 20, 'bold'))
    label_for_old_user.place(x = 400,y = 575)

    label_get_total_info = tk.Label(win,text = "Enter you Unique code to get details")
    label_get_total_info.place(x=400,y = 640)

    label_workouts = tk.Label(win,text='coose your workouts')
    label_workouts.place(x = 400 , y = 685)

    label_for_date = tk.Label(win,text= 'date and time')
    label_for_date.place(x = 400,y = 730)

    entry_get_total_details = tk.Entry(win,width=30)
    entry_get_total_details.place(x=625,y = 640)
   
    button_to_get_details = tk.Button(win,text="submit",command = get_unique_code)
    button_to_get_details.place(x = 825,y = 640)


    win.mainloop()
