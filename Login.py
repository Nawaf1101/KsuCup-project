import sys
import tkinter
from tkinter import *
from tkinter import ttk
import re
import sqlite3
import hashlib
from tkinter import messagebox
import Student
from pathlib import Path




class Login:
    def __init__(self):
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame1")
        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        self.window = Tk()
        self.window.title("Login")

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
            file=relative_to_assets("image_11.png"))
        image_1 = canvas.create_image(
            639.0,
            453.0,
            image=image_image_1
        )

        canvas.create_text(
            145.0,
            469.0,
            anchor="nw",
            text="Password",
            fill="#FFFFFF",
            font=("Inter", 30 * -1)
        )

        canvas.create_text(
            143.0,
            353.0,
            anchor="nw",
            text="StudentID",
            fill="#FFFFFF",
            font=("Inter", 30 * -1)
        )

        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_11.png"))
        entry_bg_1 = canvas.create_image(
            639.0,
            368.0,
            image=entry_image_1
        )
        self.entIdD = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=20
        )
        self.entIdD.place(
            x=362.0,
            y=339.0,
            width=554.0,
            height=56.0
        )

        entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_22.png"))
        entry_bg_2 = canvas.create_image(
            639.0,
            483.5,
            image=entry_image_2
        )
        self.entPa = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=20,
            show="*"
        )
        self.entPa.place(
            x=362.0,
            y=454.0,
            width=554.0,
            height=57.0
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets("image_22.png"))
        image_2 = canvas.create_image(
            639.0,
            93.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_11.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.clcLogin(),
            relief="flat",
            background="black"
        )
        self.button_1.place(
            x=486.0,
            y=701.0,
            width=306.0,
            height=75.0
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_22.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.go_signup(),
            relief="flat"
        )
        button_2.place(
            x=528.0,
            y=776.0,
            width=223.0,
            height=53.0
        )
        self.lblSA = tkinter.LabelFrame(self.window, text="Type of login", background="#226969")
        depts = ('Student', 'Admin')

        selected_dept = tkinter.StringVar()
        self.lblSA.place(x=810.0, y=265.0)
        self.cb = ttk.Combobox(self.lblSA, textvariable=selected_dept, background="#226969")
        self.cb['values'] = depts
        self.cb.current(0)

        self.cb.grid(row=0,column=0)

        self.window.resizable(False, False)
        self.window.mainloop()





        self.window.mainloop()

    def go_signup(self):
        self.window.destroy()
        import Signup
        Signup.Signup()

    def clcLogin(self):
        isWork = True
        if not self.entIdD.get() or self.entIdD.get() == "you must enter just 10 number" or self.entIdD.get() == "you must enter up to 10 number" or self.entIdD.get() == "ID is empty!":
            self.entIdD.delete(0,"end")
            self.entIdD.configure(fg="red")
            self.button_1.focus_set()
            self.entIdD.insert(0, "ID is empty!")
            self.entIdD.bind("<FocusIn>", self.cleanID)
            isWork = False
        elif len(list(self.entIdD.get())) > 10:
            self.entIdD.delete(0,"end")
            self.entIdD.configure(fg="red")
            self.button_1.focus_set()
            self.entIdD.insert(0, "you must enter just 10 number")
            self.entIdD.bind("<FocusIn>", self.cleanID)
            isWork = False
        elif len(list(self.entIdD.get())) < 10:
            self.entIdD.delete(0, "end")
            self.button_1.focus_set()
            self.entIdD.configure(fg="red")
            self.entIdD.insert(0, "you must enter up to 10 number")
            self.entIdD.bind("<FocusIn>", self.cleanID)
            isWork = False
        if not self.entPa.get() or self.entPa.get() == "Password is empty!":
            self.entPa = Entry(
                bd=0,
                bg="#D9D9D9",
                fg="#000716",
                highlightthickness=0,
                font=20,
                foreground="red"
            )
            self.entPa.place(
                x=362.0,
                y=454.0,
                width=554.0,
                height=57.0
            )
            self.entPa.insert(0, "Password is empty!")
            self.entPa.bind("<FocusIn>", self.cleanPas)
            isWork = False


        if isWork:
            ps = False
            con = sqlite3.connect("CentralDataBase.db")
            g = con.execute(f"SELECT StudentID, Password FROM Users Where StudentID = '{self.entIdD.get()}'").fetchall()
            if g == [ ]:
                messagebox.showerror("Error", "You didn't signup before")
            else:
                p = hashlib.sha256(self.entPa.get().encode()).hexdigest()
                if self.cb.get() == "Admin":
                    if g[0][0] != "0123456789":
                        messagebox.showerror("Error", "You are not an admin!")
                    else:
                        if p == g[0][1]:
                            self.window.destroy()
                            import Admin
                            Admin.Admin()

                        else:
                            ps = True

                elif self.cb.get() == "Student":
                    if self.entIdD.get() == "0123456789":
                        messagebox.showerror("Error", "You Can't login as student")
                    else:
                        if p == g[0][1]:
                            gg = self.entIdD.get()
                            self.window.destroy()
                            Student.Student(gg)

                        else:
                            ps = True

                if ps:
                    messagebox.showerror("Error", "Your ID or Password are invalid")

    def cleanID(self,d):
        self.entIdD.destroy()
        self.entIdD = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=20
        )
        self.entIdD.place(
            x=362.0,
            y=339.0,
            width=554.0,
            height=56.0
        )
    def cleanPas(self,d):
        self.entPa.destroy()
        self.entPa = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=20,
            show="*"
        )
        self.entPa.place(
            x=362.0,
            y=454.0,
            width=554.0,
            height=57.0
        )


if __name__ == "__main__":
    Login()