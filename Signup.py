import sys
import tkinter
from tkinter import *
import re
import sqlite3
import hashlib
from tkinter import messagebox
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from pathlib import Path
from time import sleep

class Signup:
    def __init__(self):

        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        self.window = Tk()
        self.window.title("Signup")

        self.window.geometry("1440x900")
        self.window.configure(bg="#226969")

        canvas = Canvas(
            self.window,
            bg="#226969",
            height=900,
            width=1440,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        canvas.place(x=0, y=0)
        canvas.create_text(
            262.0,
            246.0,
            anchor="nw",
            text="First Name",
            fill="#FFFFFF",
            font=("Inter", 30 * -1)
        )

        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(
            698.0,
            485.0,
            image=image_image_1
        )

        canvas.create_text(
            945.0,
            246.0,
            anchor="nw",
            text="Last Name",
            fill="#FFFFFF",
            font=("Inter", 30 * -1)
        )

        canvas.create_text(
            951.0,
            384.0,
            anchor="nw",
            text="Password",
            fill="#FFFFFF",
            font=("Inter", 30 * -1)
        )

        canvas.create_text(
            269.0,
            385.0,
            anchor="nw",
            text="StudentID",
            fill="#FFFFFF",
            font=("Inter", 30 * -1)
        )

        canvas.create_text(
            248.0,
            524.0,
            anchor="nw",
            text="Email Adress",
            fill="#FFFFFF",
            font=("Inter", 30 * -1)
        )

        canvas.create_text(
            915.0,
            524.0,
            anchor="nw",
            text="Phone Number",
            fill="#FFFFFF",
            font=("Inter", 30 * -1)
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.go_Login(),
            relief="flat"
        )
        button_1.place(
            x=575.0,
            y=838.0,
            width=236.0,
            height=43.0
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.clcSub(),
            relief="flat"
        )
        self.button_2.place(
            x=560.0,
            y=775.0,
            width=267.0,
            height=54.0
        )

        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = canvas.create_image(
            346.0,
            323.5,
            image=entry_image_1
        )
        self.entNm = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=15
        )
        self.entNm.place(
            x=73.0,
            y=289.0,
            width=546.0,
            height=67.0
        )

        entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_2 = canvas.create_image(
            1039.0,
            323.5,
            image=entry_image_2
        )
        self.entLN = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=15
        )
        self.entLN.place(
            x=766.0,
            y=289.0,
            width=546.0,
            height=67.0
        )

        entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        entry_bg_3 = canvas.create_image(
            346.0,
            463.5,
            image=entry_image_3
        )
        self.entID = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=15
        )
        self.entID.place(
            x=73.0,
            y=429.0,
            width=546.0,
            height=67.0
        )

        entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_4.png"))
        entry_bg_4 = canvas.create_image(
            1040.0,
            462.5,
            image=entry_image_4
        )
        self.entPASS = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=15,

        )
        self.entPASS.place(
            x=767.0,
            y=428.0,
            width=546.0,
            height=67.0
        )

        entry_image_5 = PhotoImage(
            file=relative_to_assets("entry_5.png"))
        entry_bg_5 = canvas.create_image(
            346.0,
            602.5,
            image=entry_image_5
        )
        self.entEM = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            foreground="grey",
            font=15

        )
        self.entEM.place(
            x=73.0,
            y=568.0,
            width=546.0,
            height=67.0
        )
        self.entEM.insert(0, "example@ksu.edu.sa")
        self.entEM.bind("<FocusIn>", self.clnem)


        entry_image_6 = PhotoImage(
            file=relative_to_assets("entry_6.png"))
        entry_bg_6 = canvas.create_image(
            1039.0,
            601.5,
            image=entry_image_6
        )
        self.entPH = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            foreground="grey",
            font=15
        )
        self.entPH.place(
            x=766.0,
            y=567.0,
            width=546.0,
            height=67.0
        )
        self.entPH.insert(END, '05XXXXXXXX')
        self.entPH.bind("<FocusIn>", self.clnp)

        image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        image_2 = canvas.create_image(
            700.0,
            80.0,
            image=image_image_2
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def go_Login(self):
        self.window.destroy()
        import Login
        Login.Login()

    def clcSub(self):
        iswork = True
        iswork2 = True
        if not self.entNm.get():
            self.entNm.delete(0,"end")
            self.entNm.configure(fg="red")
            self.button_2.focus_set()
            self.entNm.insert(0, "First name is empty!")
            self.entNm.bind("<FocusIn>", self.cleanFN)
            iswork = False

        if not self.entLN.get():
            self.entLN.delete(0,"end")
            self.entLN.configure(fg="red")
            self.button_2.focus_set()
            self.entLN.insert(0, "Last name is empty!")
            self.entLN.bind("<FocusIn>", self.cleanLN)
            iswork = False
        if not self.entID.get():
            self.entID.delete(0,"end")
            self.entID.configure(fg="red")
            self.button_2.focus_set()
            self.entID.insert(0, "ID is empty!")
            self.entID.bind("<FocusIn>", self.cleanID)
            iswork = False

        if not self.entPASS.get():
            self.entPASS.delete(0,"end")
            self.entPASS.configure(fg="red")
            self.button_2.focus_set()
            self.entPASS.insert(0, "Password is empty!")
            self.entPASS.bind("<FocusIn>", self.cleanPAS)
            iswork = False

        if not self.entEM.get() or self.entEM.get() == "example@ksu.edu.sa":
            self.entEM.delete(0,"end")
            self.button_2.focus_set()
            self.entEM.configure(fg="red")
            self.entEM.insert(0, "Email is empty!")
            self.entEM.bind("<FocusIn>", self.clnem)
            iswork = False

        if not self.entPH.get() or self.entPH.get() == "05XXXXXXXX":
            self.entPH.delete(0,"end")
            self.button_2.focus_set()
            self.entPH.configure(fg="red")
            self.entPH.insert(0, "Phone number is empty!")
            self.entPH.bind("<FocusIn>", self.clnp)
            iswork = False

        fn = re.search("[0-9@$!#%*?&]", self.entNm.get())
        if fn and self.entNm.get()!= "First name is empty!" and self.entNm.get().find("you enterd something") == -1:
            entnm = self.entNm.get()
            self.entNm.delete(0,"end")
            self.button_2.focus_set()
            self.entNm.configure(fg="red")
            self.entNm.insert(0, f"**{entnm}** you enterd something that not a String")
            self.entNm.bind("<FocusIn>", self.cleanFN)
            iswork = False
        ln = re.search("[0-9@$!#%*?&]", self.entLN.get())
        if ln and self.entLN.get() != "Last name is empty!" and self.entLN.get().find("you enterd something") == -1:
            entln = self.entLN.get()
            self.entLN.delete(0,"end")
            self.button_2.focus_set()
            self.entLN.configure(fg="red")
            self.entLN.insert(0, f"**{entln}** you enterd something that not a String")
            self.entLN.bind("<FocusIn>", self.cleanLN)
            iswork = False
        id = re.search("[A-Za-z@$!#%*?&]", self.entID.get())
        if id:
            self.entID.delete(0,"end")
            self.button_2.focus_set()
            self.entID.configure(fg="red")
            self.entID.insert(0, "ID is invalid!, contain something that not a number")
            self.entID.bind("<FocusIn>", self.cleanID)
            iswork = False
        if len(list(self.entID.get())) > 10:
            self.entID.delete(0,"end")
            self.button_2.focus_set()
            self.entID.configure(fg="red")
            self.entID.insert(0, "ID is invalid!, you must enter just 10 number")
            self.entID.bind("<FocusIn>", self.cleanID)
            iswork = False
        if len(list(self.entID.get())) < 10:
            self.entID.delete(0,"end")
            self.entID.configure(fg="red")
            self.button_2.focus_set()
            self.entID.insert(0, "ID is invalid!, you must enter up to 10 number")
            self.entID.bind("<FocusIn>", self.cleanID)
            iswork = False

        pas = re.search("^[A-Za-z0-9]{6,}$", self.entPASS.get())
        if not pas:
            self.entPASS.delete(0,"end")
            self.entPASS.configure(fg="red")
            self.button_2.focus_set()
            self.entPASS.insert(0, "Password must contain 6 or more digits and no special chracters")
            self.entPASS.bind("<FocusIn>", self.cleanPAS)
            iswork = False
        eml = re.search("^([a-zA-Z0-9\._-]+)(@ksu.edu.sa)$", self.entEM.get())
        if not eml and self.entEM.get()!="Email is empty!":
            self.entEM.delete(0,"end")
            self.button_2.focus_set()
            self.entEM.configure(fg="red",font=10)
            self.entEM.insert(0, "Email must be : XXXXXX@ksu.edu.sa and dont have special chracters")
            self.entEM.bind("<FocusIn>", self.clnem)
            iswork = False

        pho = re.search("^(05)[0-9]{8}$", self.entPH.get())
        if not pho and self.entPH.get() != "05XXXXXXXX" and self.entPH.get()!="Phone number is empty!":
            self.entPH.delete(0,"end")
            self.button_2.focus_set()
            self.entPH.configure(fg="red",font=8)
            self.entPH.insert(0, "Phone numbers only 10 numbers like: 05XXXXXXXX and no special chracters")
            self.entPH.bind("<FocusIn>", self.clnp)
            iswork = False

        if iswork:
            con = sqlite3.connect("CentralDataBase.db")
            cur = con.cursor()
            cur.execute("SELECT StudentID FROM Users")
            ids = cur.fetchall()

            for i in ids:
                if self.entID.get() == i[0]:
                    messagebox.showerror("Error", "Your student id already exist")
                    iswork2 = False
            if iswork2:
                p = hashlib.sha256(self.entPASS.get().encode()).hexdigest()
                cur.execute(
                    """INSERT INTO Users(FirstName, LastName, StudentID,Password,Email,Phone) VALUES (?,?,?,?,?,?);""",
                    (self.entNm.get(), self.entLN.get(), self.entID.get(), p, self.entEM.get(), self.entPH.get()))
                con.commit()
                con.close()
                self.go_Login()

    def cleanFN(self, d):
        self.entNm.destroy()
        self.entNm = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=15
        )
        self.entNm.place(
            x=73.0,
            y=289.0,
            width=546.0,
            height=67.0
        )


    def cleanLN(self, d):
        self.entLN.destroy()
        self.entLN = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=15
        )
        self.entLN.place(
            x=766.0,
            y=289.0,
            width=546.0,
            height=67.0
        )

    def cleanID(self, d):
        self.entID.destroy()
        self.entID = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=15
        )
        self.entID.place(
            x=73.0,
            y=429.0,
            width=546.0,
            height=67.0
        )



    def cleanPAS(self, d):
        self.entPASS.destroy()
        self.entPASS = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=15,

        )
        self.entPASS.place(
            x=767.0,
            y=428.0,
            width=546.0,
            height=67.0
        )


    def clnp(self,d):
        self.entPH.destroy()
        self.entPH = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=15
        )
        self.entPH.place(
            x=766.0,
            y=567.0,
            width=546.0,
            height=67.0
        )
        self.entPH.insert(0, "05")
    def clnem(self,d):
        self.entEM.destroy()
        self.entEM = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=15

        )
        self.entEM.place(
            x=73.0,
            y=568.0,
            width=546.0,
            height=67.0
        )
        self.entEM.insert(0, "@ksu.edu.sa")







