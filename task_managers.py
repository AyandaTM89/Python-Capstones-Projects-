#importing the modules or libraries
import datetime
import os

print("Capstone Project 2 \n")
#decleration of variables and values
menu = ""
contents = ""
user_name = ""
password = ""
my_tasks = ""
#admin adding a memeber or user to the file user.txt
user_file = open("user.txt", "r")
#looping into the user file using a for loop
for lines in user_file:
    x = lines.strip()
    y = x.split(", ")
    user_name = y[0]
    password = y[1]

# using a while loop for to enter a user name and a password
while True:
    userName = input("Enter user name: ")
    password1 = input("Enter password: ")
    if userName == user_name and password1 == password:
        print("\n Welcom " + userName)
#a menu option to select for every user choice
        while True:
            menu = input('''Select one of the following Options below:
            r - Registering a user
            a - Adding a task
            va - View all tasks
            vm - view my task
            e - Exit
            : ''').lower()
#registering a new user details into a user file . "user.txt"
            if menu == 'r' :
                print("Register a new user")
                if userName == "admin" and password1 == "adm1n": 
                    user_name =  input("Enter a new user name : ")
                    new_password = input("Enter password: ")
                    new_password1 = input ("Confirm password: ")
                if new_password == new_password1:
                    user_file = open("user.txt", "r+")
                    user_file.write(f"\n{user_name}, {new_password}")
                    for lines in user_file:
                        x = lines.strip()
                        y = x.split(", ")
                        user_name = y[0]
                        password = y[1]
                        
                    print("New user registered \n")
                    user_file.close()
                else:
                    print("\n only admin can register the user \n")
#adding a task by a logged in user ,admin or a registerd user into a task file "task.txt"                   
            elif menu == "a" :
                task_user_name = input("Enter the Name of the person assigned to the task: ")
                title_of_task = input("Enter the tittle of the task: ")
                description = input("Discription: ")
                assign_date = input("Assignment date: ")
                due_date = input("Enter the due date: ")
                task_completed = input("is the dask finished ? Yes or No: ")
                user_file = open("tasks.txt", "a")
                user_file.write(f"\n {task_user_name}, {title_of_task}, {description}, {assign_date}, {due_date}, {task_completed}")
                print("\n Task Added \n")
                user_file.close()
#user viewing the all tasks the created in the file task.txt
            elif menu == "va":
                    print("\n View all Tasks \n")
                    with open("tasks.txt", "r+") as user_file:
                        for lines in user_file:
                            x = lines.strip()
                            y = x.split(", ") 
                            print("-------------------------------------------------------------------")                           
                            print("Task Assigned to: " + y[0])
                            print("Title of Task : " + y[1])
                            print("Description: " + y[2])
                            print("Assign Date: " + y[3])
                            print("Due Date: " + y[4])
                            print("Task completed ? " + y[5])
                            print("-------------------------------------------------------------------")
##user/admin viewing their tasks they created in the file task.txt
            elif menu == "vm":
                print("\n View my tasks \n")
                with open("tasks.txt", "r+")as user_file:
                    for lines in user_file:
                       
                        x = lines.strip()
                        y = x.split(", ")
                        if user_name == y[0]:
                            print("-------------------------------------------------------------------")
                            print("Task was assigned to : " + y[0])
                            print("Title of Task : " + y[1])
                            print("Description: " + y[2])
                            print("Assign Date: " + y[3])
                            print("Due Date: " + y[4])
                            print("Task completed ? " + y[5])
                            print("-------------------------------------------------------------------") 
#elif statement to update the  user that they exited the menu  
            elif menu == "e":
                print("good bye !")
                break                          
#closing of a user file user.txt
            user_file.close()
    else:
        print("invalid user or password")