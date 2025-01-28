from tkinter import *
from model.entity.user import User
from model.da.da import DataAccess
import tkinter.messagebox as msg
from view.ticket_view import TicketView

class UserView:
    window_count = 0

    def button_click(self):
        try :
            user =User(self.username.get(),self.password.get())
            user_da = DataAccess(User)
            if user_da.find_by(User.username==user.username):
                if user_da.find_by(User.password==user.password):
                    self.win.destroy()
                    ticket = TicketView()
                else:
                    msg.showerror("Login Error", "Wrong Username or Password")

        except Exception as e:
            msg.showerror("Login Error", f"{e}")

    def __init__(self):
        self.win = Tk()
        self.win.geometry('250x200')
        self.win.title('User View')

        Label(self.win, text='Username:').place(x=20, y=20)
        self.username = StringVar()
        Entry(self.win, textvariable=self.username).place(x=80, y=20)

        Label(self.win, text='Password:').place(x=20, y=60)
        self.password = StringVar()
        Entry(self.win, textvariable=self.password).place(x=80, y=60)

        Button(self.win , text = "Login" , command=self.button_click).place(x=80, y= 120)

        self.win.mainloop()

