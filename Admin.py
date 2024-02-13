import sys
import tkinter
from calendar import Calendar
from tkinter import messagebox
import re
from tkcalendar import Calendar
from datetime import date
from tkinter import *
import random
from tktimepicker import AnalogPicker, AnalogThemes
import sqlite3,csv
from pathlib import Path
import logging


class Admin:
    def __init__(self):
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame2")
        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        self.window = Tk()
        self.window.title("Admin")

        self.window.geometry("1279x833")
        self.window.configure(bg="#226969")

        canvas = Canvas(
            self.window,
            bg="#226969",
            height=833,
            width=1279,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        canvas.place(x=0, y=0)
        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(
            639.0,
            453.0,
            image=image_image_1
        )

        canvas.create_text(
            866.0,
            227.0,
            anchor="nw",
            text="Event location:",
            fill="#FFFFFF",
            font=("Inter", 30 * -1)
        )

        canvas.create_text(
            207.0,
            228.0,
            anchor="nw",
            text="Event name:",
            fill="#FFFFFF",
            font=("Inter", 30 * -1)
        )

        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = canvas.create_image(
            303.0,
            305.0,
            image=entry_image_1
        )
        self.entEN = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=15
        )
        self.entEN.place(
            x=26.0,
            y=276.0,
            width=554.0,
            height=56.0
        )

        entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_2 = canvas.create_image(
            974.0,
            305.5,
            image=entry_image_2
        )
        self.entEVl = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=15
        )
        self.entEVl.place(
            x=697.0,
            y=276.0,
            width=554.0,
            height=57.0
        )

        canvas.create_text(
            190.0,
            407.0,
            anchor="nw",
            text="Event capacity:",
            fill="#FFFFFF",
            font=("Inter", 30 * -1)
        )

        entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        entry_bg_3 = canvas.create_image(
            303.0,
            484.5,
            image=entry_image_3
        )
        self.entEVc = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=15
        )
        self.entEVc.place(
            x=26.0,
            y=455.0,
            width=554.0,
            height=57.0
        )

        canvas.create_text(
            892.0,
            407.0,
            anchor="nw",
            text="Event date:",
            fill="#FFFFFF",
            font=("Inter", 30 * -1)
        )

        entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_4.png"))
        entry_bg_4 = canvas.create_image(
            974.0,
            484.5,
            image=entry_image_4
        )
        self.entEVd = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            foreground="grey",
            font=15
        )
        self.entEVd.place(
            x=697.0,
            y=455.0,
            width=554.0,
            height=57.0
        )
        self.entEVd.bind("<FocusIn>", self.showdate)
        self.entEVd.insert(0, "Select date and time")
        image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        image_2 = canvas.create_image(
            640.0,
            102.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.clcsub(),
            relief="flat"
        )
        button_1.place(
            x=185.0,
            y=596.0,
            width=209.0,
            height=73.0
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.logout(),
            relief="flat"
        )
        button_2.place(
            x=589.0,
            y=731.0,
            width=102.0,
            height=36.0
        )

        button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.bcup(),
            relief="flat"
        )
        button_3.place(
            x=915.0,
            y=605.0,
            width=102.0,
            height=56.0
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def logout(self):
      self.window.destroy()
      import Signup
      Signup.Signup()

    def showdate(self,d):
       self.entEVd.destroy()
       self.entEVd = Entry(
           bd=0,
           bg="#D9D9D9",
           fg="#000716",
           highlightthickness=0,
           font=15
       )
       self.entEVd.place(
           x=697.0,
           y=455.0,
           width=554.0,
           height=57.0
       )
       self.entEVd.bind("<FocusIn>", self.showdate)
       windowCal = Toplevel()
       windowCal.geometry("400x700")
       windowCal.title("Select the date and time")


       today = date.today()
       d = today.strftime("%d/%m/%Y").split('/')
       cal = Calendar(windowCal, selectmode='day',date_pattern="yyyy-mm-dd")

       cal.pack(pady=50)
       time_picker = AnalogPicker(windowCal)
       time_picker.configure()
       time_picker.pack(expand=False, fill="both")
       self.timee = time_picker.time()
       self.dt = cal.get_date()




       button = Button(windowCal, text="Done", command=lambda: self.grad_date(windowCal, cal.get_date(),time_picker.time()))
       button.pack(pady=20)


       windowCal.grab_set()



    def grad_date(self, windowCal, d,a):
       windowCal.update()
       windowCal.destroy()
       self.hour = a[0]
       if a[2] == 'PM' and self.hour != 12:
         self.hour = self.hour + 12
       elif a[2] == 'AM' and self.hour == 12:
         self.hour = "00"
       self.min = a[1]
       if self.min == 0:
          self.min = "00"
       self.dt = d
       self.entEVd.insert(0,f"{d} -- {self.hour}:{self.min}")

    def clcsub(self):
       isWork = True
       if not self.entEVd.get() or self.entEVd.get() == "Select the date and time" or not self.entEN.get() or not self.entEVc.get() or not self.entEVl.get():
          isWork = False
          messagebox.showerror("Error", "You must fill all the entry fields!")

       capp = re.search("^[0-9]{1,}$", self.entEVc.get())
       if not capp and self.entEVc.get() != "":

          self.entEVc.destroy()
          self.entEVc = Entry(
              bd=0,
              bg="#D9D9D9",
              fg="#000716",
              highlightthickness=0,
              font=15,
              foreground="red"
          )
          self.entEVc.place(
              x=26.0,
              y=455.0,
              width=554.0,
              height=57.0
          )
          self.entEVc.insert(0, "You must enter just numbers!")
          self.entEVc.bind("<FocusIn>", self.cleanCAP)
          isWork = False

       evn = re.search("^[0-9!@#$%^&*()]", self.entEN.get())
       if evn:
          self.entEN.destroy()
          self.entEN = Entry(
              bd=0,
              bg="#D9D9D9",
              fg="#000716",
              highlightthickness=0,
              font=15,
              foreground="red"
          )
          self.entEN.place(
              x=26.0,
              y=276.0,
              width=554.0,
              height=56.0
          )
          isWork = False
          self.entEN.insert(0, "This field must started by letters")
          self.entEN.bind("<FocusIn>", self.cleanEN)
          isWork = False
       evl = re.search("^[0-9!@#$%^&*()]", self.entEVl.get())
       if evl:
          self.entEVl.destroy()
          self.entEVl = Entry(
              bd=0,
              bg="#D9D9D9",
              fg="#000716",
              highlightthickness=0,
              font=15,
              foreground="red"
          )
          self.entEVl.place(
              x=697.0,
              y=276.0,
              width=554.0,
              height=57.0
          )
          self.entEVl.insert(0, "This field must started by letters")
          self.entEVl.bind("<FocusIn>", self.cleanEL)
          isWork = False
       if isWork:

          con = sqlite3.connect("CentralDataBase.db")

          cur = con.cursor()
          g = cur.execute("SELECT EventNumber from Events").fetchall()
          flag = True
          o = random.randint(10000,99999)
          while flag:
             t = o
             for i in g:
                if i[0] == str(g):
                   o = random.randint(10000,99999)
             if t == o:
                flag =False

          u = f"{self.dt} {self.hour}:{self.min}"
          cur.execute("""INSERT INTO Events(EventNumber, EventName, EventLocation,EventCapacity,EventDate,EventAttendance) VALUES (?,?,?,?,?,?);""",(o, self.entEN.get(), self.entEVl.get(), self.entEVc.get(), u, 0))

          messagebox.showinfo("Nice!", "Event Created")
          con.commit()
          con.close()
          self.cleanCAP(None)
          self.cleanEN(None)
          self.cleanEL(None)
          self.entEVd.delete(0,"end")
          self.entEVd.configure(fg="grey")
          self.entEVd.insert(0, "Select date and time")

    def cleanCAP(self,d):
       self.entEVc.destroy()
       self.entEVc = Entry(
           bd=0,
           bg="#D9D9D9",
           fg="#000716",
           highlightthickness=0,
           font=15
       )
       self.entEVc.place(
           x=26.0,
           y=455.0,
           width=554.0,
           height=57.0
       )
    def cleanEN(self,d):
       self.entEN.destroy()
       self.entEN = Entry(
           bd=0,
           bg="#D9D9D9",
           fg="#000716",
           highlightthickness=0,
           font=15
       )
       self.entEN.place(
           x=26.0,
           y=276.0,
           width=554.0,
           height=56.0
       )
    def cleanEL(self,d):
       self.entEVl.destroy()
       self.entEVl = Entry(
           bd=0,
           bg="#D9D9D9",
           fg="#000716",
           highlightthickness=0,
           font=15
       )
       self.entEVl.place(
           x=697.0,
           y=276.0,
           width=554.0,
           height=57.0
       )

    def lgout(self):
       self.window.destroy()
       import Signup
       Signup.Signup()

    def bcup(self):
        try:
           con = sqlite3.connect("CentralDataBase.db")
           with open('BackupDatabase.csv', 'w') as fin:
              fin.writelines(str(con.execute("SELECT * FROM USERS").fetchall()))
              fin.writelines("\n")
              fin.writelines("\n")
              fin.writelines(str(con.execute("SELECT * FROM Events").fetchall()))
              fin.writelines("\n")
              fin.writelines("\n")
              fin.writelines(str(con.execute("SELECT * FROM Reg").fetchall()))
              con.close()
        except sqlite3.OperationalError:
            print("Create the data base please!!")




if __name__ == "__main__":
    Admin()