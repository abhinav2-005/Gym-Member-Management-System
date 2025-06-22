import mysql.connector

def get_connection1():
    return mysql.connector.connect(
        host="localhost",       
        user="root",   
        password="#include<stdio.h>",   
        database="studentinfo"    
    )
def get_connection2():
    return mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '#include<stdio.h>',
        database = 'dates_and_time_info'
    )

