import sqlite3
import Signup


con = sqlite3.connect("CentralDataBase.db")
if __name__ == "__main__":
    try:

        con.execute("select * from users")
        con.close()
        Signup.Signup()
    except sqlite3.OperationalError:
        import centralDB
        Signup.Signup()