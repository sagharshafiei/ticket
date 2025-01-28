from tkinter import *
import tkinter.messagebox as msg
from view.component import *
from controller.ticket_controller import *

class TicketView:
    def save_click(self):
        status, data = save(self.name.variable.get(), self.title.variable.get(),self.description.variable.get(),
                            self.time.variable.get(),self.date.variable.get(),self.state.variable.get())
        if status:
            msg.showinfo("Save", f"Ticket Saved\n{data}")
            self.reset_form()
        else:
            msg.showerror("Save Error", f"Error\n{data}")

    def edit_click(self):
        status, data = edit(self.id.variable.get(), self.name.variable.get(), self.title.variable.get(),self.description.variable.get(),
                            self.time.variable.get(),self.date.variable.get(),self.state.variable.get())
        if status:
            msg.showinfo("Edit", f"Ticket Edited\n{data}")
            self.reset_form()
        else:
            msg.showerror("Edit Error", f"Error\n{data}")

    def remove_click(self):
        status, data = remove_by_id(self.id.variable.get())
        if status:
            msg.showinfo("Remove", f"Ticket Removed\n{data}")
            self.reset_form()
        else:
            msg.showerror("Remove Error", f"Error\n{data}")

    def select_table(self, selected_member):
        self.id.variable.set(selected_member[0])
        self.name.variable.set(selected_member[1])
        self.title.variable.set(selected_member[2])
        self.description.variable.set(selected_member[3])
        self.time.variable.set(selected_member[4])
        self.date.variable.set(selected_member[5])
        self.state.variable.set(selected_member[6])

    def reset_form(self):
        self.id.variable.set(0)
        self.name.variable.set("")
        self.title.variable.set("")
        self.description.variable.set("")
        self.time.variable.set("")
        self.date.variable.set("")
        self.state.variable.set("")
        status, member_list = find_all()
        self.table.refresh_table(member_list)

    def __init__(self):
        self.win = Tk()
        self.win.title("Ticket")
        self.win.geometry("850x350")

        self.id = LabelAndEntry(self.win, "Id", 20,20, data_type="int", state="readonly")
        self.name = LabelAndEntry(self.win, "Name", 20, 60)
        self.title = LabelAndEntry(self.win, "title", 20, 100)
        self.description = LabelAndEntry(self.win, "Description", 20, 140)
        self.time =LabelAndEntry(self.win, "Time", 20, 180)
        self.date = LabelAndEntry(self.win, "Date", 20, 220)
        self.state = LabelAndEntry(self.win, "State", 20, 260)


        self.table = Table(
            self.win,
            ["Id", "Name", "Title", "Description","time","date","state"],
            [60,80,80,100,80,80,80],
            250,40,
            self.select_table
        )

        Button(self.win, text="New", width= 10, command=self.reset_form).place(x=20,y=300)
        Button(self.win, text="Save", width= 10, command=self.save_click).place(x=120,y=300)
        Button(self.win, text="Edit", width= 10, command=self.edit_click).place(x=220,y=300)
        Button(self.win, text="Remove", width= 10, command=self.remove_click).place(x=320,y=300)

        self.reset_form()

        self.win.mainloop()

