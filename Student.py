import tkinter
from calendar import Calendar
from tkinter import messagebox
import re
from tkcalendar import Calendar
from datetime import date
from tkinter import *
import random
from tktimepicker import AnalogPicker, AnalogThemes
import sqlite3
from datetime import datetime
from  tkinter import ttk
import logging
logging.basicConfig(filename='BookLog.log',
                    filemode='a',
                    format='%(asctime)s , %(message)s',
                    level=logging.DEBUG)



# self.tree.item(self.tree.selection()[0])['values']
class Student:
    def __init__(self,q):
        self.canshow = False
        self.canshow2 = True
        self.stID = q
        self.window = tkinter.Tk()
        self.window.title("Student")
        self.window.geometry('1100x710')
        self.window.iconbitmap(default='KSU.ico')
        self.window.configure(bg="#226969")
        self.window.geometry("+400+100")  # to position the window in the center
        self.bg = PhotoImage(file="cancs.png")
        self.canvas = tkinter.Canvas(self.window, width=700, height=500)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg, anchor="nw")
        self.notebook = ttk.Notebook(self.canvas)
        self.notebook.pack(pady=10, expand=True,)


        self.buttonBack = tkinter.Button(self.canvas, text='Logout',command= lambda : self.go_sgn())
        self.frame = tkinter.Frame(self.canvas,background="#226969")
        self.frame.pack(pady=20)
        self.EmpForm = tkinter.LabelFrame(self.frame, text="Book Event")
        self.EmpForm.grid(row=0, column=1)
        self.EmpForm.configure(bg="#F1EFF1")
        self.tree = ttk.Treeview(self.EmpForm)
        self.sub = Button(self.EmpForm, text='Book!', fg='black', bg="white", height=1, width=7, cursor='hand2',command= lambda : self.book())
        self.sub.grid(row=8, column=1)

        self.tree['columns'] = ("Event Number", "Event Name", "Event Location", "Event Date","State")
        self.tree.column("#0", width=0,minwidth=0)
        self.tree.column("Event Number", anchor=CENTER, width=85)
        self.tree.column("Event Name", anchor=CENTER, width=120)
        self.tree.column("Event Location",anchor=CENTER, width=120)
        self.tree.column("Event Date",anchor=CENTER, width=100)
        self.tree.column("State",anchor=CENTER, width=100)
        self.tree.heading("Event Number",text="Event Number",anchor=CENTER)
        self.tree.heading("Event Name",text="Event Name",anchor=CENTER)
        self.tree.heading("Event Location", text = "Event Location",anchor=CENTER)
        self.tree.heading("Event Date", text= "Event Date",anchor=CENTER)
        self.tree.heading("State", text= "Status",anchor=CENTER)
        con = sqlite3.connect("CentralDataBase.db")
        g= con.execute(f"Select * from Events order by EventDate DESC").fetchall()
        cot = 0
        h = con.execute(f"SELECT  EventNumber from reg where StudentID = {self.stID}").fetchall()
        for i in g:
            ins = True
            if datetime.strptime(i[4], "%Y-%m-%d %H:%M") > datetime.today():
                for n in h:
                    if n[0] == i[0]:
                        ins = False
                if ins:
                    c =  con.execute(f"Select EventCapacity, EventAttendance from Events where EventNumber = {i[0]}").fetchall()
                    if c[0][0] == c[0][1]:
                        self.tree.insert(parent='',index='end',iid=cot,values=(i[0],i[1],i[2],i[4],"Full!"))
                        cot = cot+1
                    else:
                        self.tree.insert(parent='', index='end', iid=cot, values=(i[0], i[1], i[2], i[4],"Available"))
                        cot = cot + 1



        self.tree.grid(row=0,column=1,pady=10,padx=10)


        #Second tab

        self.notebook.add(self.frame, text='Book a Ticket')


        self.view = tkinter.Frame(self.canvas, background="#226969")

        self.view.pack(pady=20)
        self.stform = tkinter.LabelFrame(self.view, text="Booked Events",padx=5,)
        self.stform.grid(row=0, column=2,ipady=10)
        self.stform.configure(bg="#F1EFF1")
        self.tree2 = ttk.Treeview(self.stform)
        self.tree2['columns'] = ("Event Number", "Event Name", "Event Location", "Event Date")
        self.tree2.column("#0", width=0, minwidth=0)
        self.tree2.column("Event Number", anchor=CENTER, width=95)
        self.tree2.column("Event Name", anchor=CENTER, width=145)
        self.tree2.column("Event Location", anchor=CENTER, width=145)
        self.tree2.column("Event Date", anchor=CENTER, width=120)
        self.tree2.heading("Event Number", text="Event Number", anchor=CENTER)
        self.tree2.heading("Event Name", text="Event Name", anchor=CENTER)
        self.tree2.heading("Event Location", text="Event Location", anchor=CENTER)
        self.tree2.heading("Event Date", text="Event Date", anchor=CENTER)
        self.tree2.grid(row=3, column=2, padx=15, pady=10)
        self.sub4 = Button(self.stform, text='Show', fg='black', bg="white", height=1, width=7, cursor='hand2',
                          command=lambda: self.showBooked())
        self.sub4.grid(row=1, column=2)
        self.notebook.add(self.view, text='View my tickets')
        con.commit()
        con.close()
        self.buttonBack.pack()
        self.window.mainloop()

    def gost(d):
        Student(d)
    def showBooked(self):
        self.canshow = True
        if self.canshow2:
            self.canshow2 = False
            con = sqlite3.connect("CentralDataBase.db")
            b = con.execute(f"SELECT * FROM Reg where StudentID = {self.stID}").fetchall()
            self.ct = 0
            for i in b:
                if datetime.strptime(i[4], "%Y-%m-%d %H:%M") > datetime.today():
                    self.tree2.insert(parent='', index='end', iid=self.ct, values=(i[1], i[2], i[3], i[4]))
                    self.ct = self.ct + 1



    def go_sgn(self):
        self.window.destroy()
        import Signup
        Signup.Signup()
    def book(self):


        if self.tree.selection() == ():
            messagebox.showerror("Error!", "You didn't select any thing!")
        else:
            g = self.tree.item(self.tree.selection()[0])['values']
            con = sqlite3.connect("CentralDataBase.db")
            f = con.execute(f"Select EventCapacity, EventAttendance from Events where EventNumber = {g[0]}").fetchall()
            if f[0][0] == f[0][1]:
                messagebox.showerror("Error!", "This event is full!")
            else:
                con.execute("""INSERT INTO Reg(StudentID, EventNumber,EventName,EventLocation,EventDate) VALUES (?,?,?,?,?);""", (self.stID, g[0], g[1],g[2],g[3]))
                logging.info(f' {g[1]}  {g[2]}  {self.stID}')
                con.execute(f"UPDATE Events set EventAttendance = EventAttendance+1 WHERE EventNumber = {g[0]}")
                con.commit()
                messagebox.showinfo("Nice", "You booked successfully")
                con.close()
                self.tree.delete(self.tree.selection()[0])
                if self.canshow :
                    self.tree2.insert(parent='', index='end', iid=self.ct, values=(g[0], g[1], g[2], g[3]))
                    self.ct = self.ct +1




if __name__ == "__main__":
    Student(4421026355)