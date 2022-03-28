This program will work with two text files, user.txt and tasks.txt. Open
each of the files that accompany this project and take note of the
following:
○ tasks.txt stores a list of all the tasks that the team is working on.
Open the tasks.txt file that accompanies this project. Note that
this text file already contains data about two tasks. The data for
each task is stored on a separate line in the text file. Each line
includes the following data about a task in this order:
■ The username of the person to whom the task is assigned.
■ The title of the task.
■ A description of the task.
■ The date that the task was assigned to the user.
■ The due date for the task.
■ Either a ‘Yes’ or ‘No’ value that specifies if the task has been
completed yet.
○ user.txt stores the username and password for each user that has
permission to use your program (task_manager.py). Open the
user.txt file that accompanies this project. Note that this text file
already contains one default user that has the username, ‘admin’



and the password, ‘adm1n’. The username and password for each
user must be written to this file in the following format:
■ First, the username followed by a comma, a space and then
the password.
■ One username and corresponding password per line.
● Your program should allow your users to do the following:
○ Login. The user should be prompted to enter a username and
password. A list of valid usernames and passwords are stored in a
text file called user.txt. Display an appropriate error message if the
user enters a username that is not listed in user.txt or enters a valid
username but not a valid password. The user should repeatedly be
asked to enter a valid username and password until they provide
appropriate credentials.


○ If the user chooses ‘r’ to register a user, the user should be
prompted for a new username and password. The user should also
be asked to confirm the password. If the value entered to confirm
the password matches the value of the password, the username
and password should be written to user.txt in the appropriate
format.
○ If the user chooses ‘a’ to add a task, the user should be prompted to
enter the username of the person the task is assigned to, the title of
the task, a description of the task and the due date of the task. The

data about the new task should be written to tasks.txt. The date on
which the task is assigned should be the current date. Also assume
that whenever you add a new task, the value that indicates whether
the task has been completed or not is ‘No’.
○ If the user chooses ‘va’ to view all tasks, display the information for
each task on the screen in an easy to read format.
○ If the user chooses ‘vm’ to view the tasks that are assigned to them,
only display all the tasks that have been assigned to the user that is
currently logged-in in a user-friendly, easy to read manner.



