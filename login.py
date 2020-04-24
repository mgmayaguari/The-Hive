from tkinter import *
from tkinter import messagebox

import su
import welcome
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="alfheim",
    database="TheHive"
)

cursor = db.cursor()


class LoginWindow:

    def __init__(self):
        self.win = Tk()
        self.win.title("The Hive")
        self.win.geometry('{}x{}'.format(800, 450))
        self.canvas = Canvas(self.win, bg='#454b54')

        self.userLabel = Label(self.canvas, text="Enter Username", font='Arial 20 bold', bg='#454b54',
                               fg='#f7cc35')
        self.username = Entry(self.canvas, font='Arial 20 bold', bg='white')

        self.passLabel = Label(self.canvas, text="Enter Password", font='Arial 20 bold', bg='#454b54',
                               fg='#f7cc35')
        self.password = Entry(self.canvas, show='*', font='Arial 20 bold', bg='white')

        self.backButton = Button(self.canvas, text="Back", font='Arial 20 bold', bg='#454b54',
                                 fg='#f7cc35', command=self.welcome)
        self.logButton = Button(self.canvas, text="Login", font='Arial 20 bold', bg='#454b54', fg='#f7cc35',
                                command=lambda: self.log_btn())

    def main(self):
        self.canvas.pack(expand=TRUE, fill=BOTH)
        self.userLabel.pack(expand=TRUE)
        self.username.pack(expand=TRUE)

        self.passLabel.pack(expand=TRUE)
        self.password.pack(expand=TRUE)

        self.backButton.pack(expand=TRUE)
        self.logButton.pack(expand=TRUE)

        self.win.mainloop()

    def su(self):
        self.win.destroy()
        superUser = su.main()
        superUser.main()

    def welcome(self):
        self.win.destroy()
        wel = welcome.WelcomeWindow()
        wel.main()

    def log_btn(self):
        username = self.username.get()
        password = self.password.get()

        cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))
        account = cursor.fetchone()

        if account:
            self.su()
        elif username == "" or password == "":
            messagebox.showwarning("Login Status", "All fields are required!")
        else:
            messagebox.showerror("Login Status", "Account does not exist!")
