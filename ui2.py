import tkinter as tk
from datetime import datetime
from tkinter import ttk
from tkinter import messagebox as mb
from sqlbackend import *


def run1():
    win1 = tk.Tk()

    curr_date_and_time = str(datetime.now())[:16]
    date = curr_date_and_time[:10]
    time = curr_date_and_time[10:16]

    win1.title('login page')
    win1.geometry('1500x1500')
    win1.config(bg = 'lightblue')

    
    def get_workouts():
        workouts = combox_box_for_workouts.get()
        if workouts:
            return workouts
        else:
            combox_box_for_workouts.insert(0,'please coose a workout')

    def get_unique_code():
        code = entry_get_total_details.get()
        if code:
            backend_operation()
            pass
        else:
            mb.showinfo('error','please provide unique code')

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

                label_date_time = tk.Label(win1,text='Date',bg = 'lightblue',font=('Times New Roman',15))
                label_date_time.place(x = 825,y=115)

                label_time = tk.Label(win1,text='Time',bg = 'lightblue',font=('Times New Roman',15))
                label_time.place(x = 925,y=115)

                label_workouts_streak = tk.Label(win1,text='Workouts',bg = 'lightblue',font=('Times New Roman',15))
                label_workouts_streak.place(x = 990,y=115)

                X,Y = int(825),int(150)

                for i in range(len(info2)):

                    label_dates = tk.Label(win1,text=f"{info2[i][1]}",bg='lightblue',font=('Times New Roman',15))
                    label_dates.place(x = X,y = Y)

                    label_time_output = tk.Label(win1,text=f"{info2[i][2]}",bg='lightblue',font=('Times New Roman',15))
                    label_time_output.place(x = (X+100),y = Y)

                    label_workouts_output = tk.Label(win1,text=f"{info2[i][3]}",bg='lightblue',font=('Times New Roman',15))
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

                label_output_name = tk.Label(win1,text=f"Name : {info[0][0]}",bg='lightblue',font=('Times New Roman',15))
                label_output_name.place(x = 250,y = 300)

                label_output_age =tk.Label(win1,text=f"Age: {info[0][1]}",bg='lightblue',font=('Times New Roman',15))
                label_output_age.place(x = 250,y = 325)

                label_output_emailid =tk.Label(win1,text=f"Email_id: {info[0][2]}",bg='lightblue',font=('Times New Roman',15))
                label_output_emailid.place(x = 250,y = 350)

                label_output_roll_no =tk.Label(win1,text=f"Roll_no: {info[0][3]}",bg='lightblue',font=('Times New Roman',15))
                label_output_roll_no.place(x = 250,y = 375)

                label_output_phonum =tk.Label(win1,text=f"Phone_num: {info[0][5]}",bg='lightblue',font=('Times New Roman',15))
                label_output_phonum.place(x = 250,y = 400)

                label_output_coursedetails =tk.Label(win1,text=f"Course Details: {info[0][4]}",bg='lightblue',font=('Times New Roman',15))
                label_output_coursedetails.place(x = 250,y = 425)

                label_output_age =tk.Label(win1,text=f"Unique_code: {info[0][6]}",bg='lightblue',font=('Times New Roman',15))
                label_output_age.place(x = 500,y = 300)

                label_date_and_time = tk.Label(win1,text=f"Date & time  {curr_date_and_time}",bg='lightblue',font=('Times New Roman',15))
                label_date_and_time.place(x = 500,y = 325 )

                button_for_streak = tk.Button(win1,text='get complete streak',command=get_streak)
                button_for_streak.place(x = 520,y = 365)

                entry_for_date_and_time.insert(0,curr_date_and_time)

                conn.commit()
                curser1.close()
                conn.close()  

            else:
                mb.showinfo('error',f"no user,invalid unique code {code}")
                entry_get_total_details.delete(0,tk.END)


    def reset_all_2():
       win1.destroy()
       run1()

    def register():
        win1.destroy()
        


    label_for_old_user = tk.Label(win1,text="Already a user?get your details with unique code",bg="lightblue",font=('Times New Roman', 20, 'bold'))
    label_for_old_user.place(x = 250,y = 50)

    label_get_total_info = tk.Label(win1,text = "Enter you Unique code")
    label_get_total_info.place(x=250,y = 115)

    label_workouts = tk.Label(win1,text='choose your workouts')
    label_workouts.place(x = 250 , y = 165)

    label_for_date = tk.Label(win1,text= 'date and time  ')
    label_for_date.place(x = 250,y = 215)

    entry_get_total_details = tk.Entry(win1,width=30)
    entry_get_total_details.place(x=400,y = 115)
    
    entry_for_date_and_time = tk.Entry(win1,width=30)
    entry_for_date_and_time.place(x = 400,y= 215)

    combox_box_for_workouts = ttk.Combobox(win1,values=['chest','back','arms','shoulders','legs','forearms'],width=30)
    combox_box_for_workouts.place(x = 400,y = 165)

    button_to_get_details = tk.Button(win1,text="submit",command= get_unique_code)
    button_to_get_details.place(x = 400,y = 265)

    button_for_reset2 = tk.Button(win1,text='New login',command=reset_all_2)
    button_for_reset2.place(x = 465,y=265)

    button_for_new_register = tk.Button(win1,text="Sign up",command=register)
    button_for_new_register.place(x = 540,y = 265)

    win1.mainloop()
