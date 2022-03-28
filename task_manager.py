import datetime
import os
print("\n Compulsory Task1 Capstone Project 3 \n")
#defining global variables
global user_name1
global user_password
global name
global user_input
global count_users
global count
global line
#create a log in system that gives registered user an access to menu
def add_task():
            global task_ds
            task_ds = 0
            task = open("tasks.txt", "r+")
            for line in task:
                temp = line.strip()
                temp = temp.split(", ")
                #request user to enter task details
                username = input("The task is assigined to : ")
                description = input("Description of task : ")
                start_date = input("Start date : ")
                due_date = input("Due date : ")
                complete = input("Task completed ? Yes or No : ")

                task.write("\n" + username + ", " + description + ", " + start_date + ", " + due_date + ", " + complete)
                task_ds += 1
                break

valid_username = ""
valid_password = ""
login = False
user3 = open("user.txt", "r")
#ask user to enter their username and password
while not login:
    username = input("Enter username : ")
    password = input("Enter password : ")

    #checking if username and password is correct
    for lines3 in user3:
        temp = lines3.strip()
        temp = temp.split(", ")
        valid_username = temp[0]  
        valid_password = temp[1]  
        if username == valid_username and password == valid_password: 
            login = True
            print("________________________________________________________________________")
            print("Welcome to Task Manager", username)
            print("________________________________________________________________________")
            user3.seek(0)
            break

    if username != valid_username or password != valid_password:
        login = False
        print("error incorrect username or password")
    user3.seek(0)

user3.close()

#declare a var for choices to creat a choice menu
choice = False

#once user is login show the choice menu so that user can see their options
def menu():
    while login == True:
        choice = input("""Please select one of the following options :
        r - Register user
        a - Add task
        va - View all tasks
        vm - View my tasks
        gr - generate reports
        ds - display statistics
        e - Exit
        """)

        def reg_user():
            #only adim has privilage to acceses this option
            global user_ds
            user_ds = 0
            admin_login = False
            while not admin_login:
                print("________________________________________________________________________")
                print("Log in as Admin to register a new user.")
                print("________________________________________________________________________")
                 #granting an admin to have accses to register a user name and password
                if username == "admin" and password == "adm1n": 
                    admin_login = True
                    print("Welcome ", username)
                    new_username = input(
                        "Enter new username : ")
                    new_password = input(
                        "Enter new password : ")
                    password1 = input(
                        "Confirm password : ")

                    #open user txt file again
                    with open("user.txt") as file:
                        #check if username is already in user.txt file
                        user_in_file = False
                        while user_in_file == False:
                            if new_username in file.read() or new_password in file.read():
                                print("Username already exist")
                                break
                            else:
                                user_in_file = True

                        #if username or password is not in the user.txt file the new user is added
                        if user_in_file == True:
                            if password1 == new_password:
                                with open("user.txt", "a") as user:
                                    user.write("\n" + new_username + ", " + new_password)
                                    user_ds += 1
                                print("________________________________________________________________________")
                                print("New user added")
                                print("________________________________________________________________________")
                            else:
                                print("Password do not match ")
                            user.close()
                else:
                    print("only Admin is allowed to register a user.")
                    break

        #admin can register a user or add new task
        if choice == "r": 
            choice = True
            print(reg_user())
        
        #user choices to add task
        if choice == "a":  
            choice = True
            print(add_task())

        def view_all():
            count = 0
            tasks = open("tasks.txt", "r+")
            for lines in tasks:
                count += 1
                lin = lines.strip()
                lin = lin.split(", ")
                print("________________________________________________________________________")
                print("Username : ", lin[0])
                print("Description : ", lin[1])
                print("Start Date : ", lin[2])
                print("Due Date : ", lin[3])
                print("Completed : ", lin[4])
                print("\n")
                print("________________________________________________________________________")
            tasks.close()

        #user to choose to view all task
        if choice == "va": 
            global new_state
            new_state = 0
            choice = True
            print(view_all())
        def view_mine():
            num_task = 0
            user_input = input("Task assigned to: ?\n")
            infile = open("tasks.txt", "r+")  
            for row in infile:  
                field = row.split(", ")  
                view_more = infile.readlines()

                #check the field in tasks file
                if field:  
                    num_task += 1
                    print("________________________________________________________________________")
                    print("Task Number: " + str(num_task) + "\nUsername: " + field[0] + "\nDescription: " + field[1] +
                          "\n Date: " + field[2] + "\nDue Date: " + field[
                              3] + "\n" + "Completed: " + field[4])
                    print("________________________________________________________________________")
                    #display the user's tasks
                    editTask = input(
                        "Would you like to edit a task? (Edit) or return to the menu? (-1)\n")
                    if editTask == "editTask".lower():
                        file = open('tasks.txt', 'r+')
                        num_task1 = int(input("Enter Task number?\n"))
                        num_task1 -= 1
                        taskFile1 = file.readlines()
                        for line in taskFile1:
                            taskFile1 = file.readlines()
                            break
                        taskComplete = input("completed? \n")
                        if taskComplete == "Yes":
                            with open("tasks.txt", 'r+') as taskFile:
                                for line in taskFile:
                                    field1 = line.strip()
                                    field1 = field1.split(", ")
                                    taskFile = file.readlines()
                                    new_state = taskFile.replace(field1[4], "Yes")
                                    print("________________________________________________________________________")
                                    print(new_state)
                                    print("________________________________________________________________________")
                        #updated_string = view_more.replace(taskFile1[num_task].strip(), new_state)
                        with open('tasks.txt', 'a+') as file:
                            file.write(new_state)
        #user choices to view their task only
        if choice == "vm":
            choice = True
            print("________________________________________________________________________")
            print(view_mine())
            print("________________________________________________________________________")

        #display statistics function
        def display_statistics(name1, user_password, count_users, count, line):
            while True:
                name1 = ""
                count_users = 0
                count = 0
                line = []
                print("________________________________________________________________________")
                print("Statistics of the Tasks")
                print("________________________________________________________________________")
                infile = open("user.txt", "r")
                
                #checking for the users in the file
                for user in infile:
                    if user[0]:
                        count_users += 1
                print("________________________________________________________________________")
                print("Total number of Users: ", count_users)
                print("________________________________________________________________________")
                break

        if choice == "ds":
            #call the display statistics function
            display_statistics("user_name", "user_password", "count_users", "count",
                               "line")  

        def generate_reports():
            #Generates task report
            infile = open("tasks.txt", "r")
            info = infile.readlines()
            #Intialising counting variables and Checking through tasks info
            num_of_tasks = 0
            num_of_complete_tasks = 0
            num_of_uncompleted_tasks = 0
            num_of_overdue_tasks = 0
            
            for line in info:
                num_of_tasks += 1
                if "Yes" in line:
                    num_of_complete_tasks += 1
                if "No" in line:
                    num_of_uncompleted_tasks += 1
                    info = line.split(", ")
                due_date = line[4]
                date = datetime.datetime.now()
                line = ", ".join(line)

            #Working out the percentages
            percentage_incomplete = (num_of_uncompleted_tasks / num_of_tasks) * 100
            percentage_overdue = (num_of_overdue_tasks / num_of_tasks) * 100
            print("________________________________________________________________________")
            print('The percentage is :' + str(percentage_incomplete))
            print('The percentage overdue is:' + str(percentage_overdue))
            print("________________________________________________________________________")

        if choice == "gr":
            choice = True
            print("________________________________________________________________________")
            print(generate_reports())
            print("________________________________________________________________________")
        #if the user selets "e" the program stops
        if choice == "e":
            choice = True
            print("Good Bye !")
            break

        else:
            choice = False
            print("Please select a valid option")
menu()
