from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  #pip install pillow
from tkinter import messagebox
import mysql.connector
from hotel import HotelManagementSystem
from register import Register_Window

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        # Background Image
        self.bg = ImageTk.PhotoImage(file=r"D:\Python\BT_Lab\BTL\Image\bglogin.jpg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # Frame for login
        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)

        # Login image
        img1 = Image.open(r"D:\Python\BT_Lab\BTL\Image\bg.png")
        img1 = img1.resize((100, 100), Image.Resampling.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg="black", borderwidth=0)
        lblimg1.place(x=730, y=175, width=100, height=100)

        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=90, y=100)

        # Username label and entry
        username = Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="white", bg="black")
        username.place(x=60, y=155)
        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        # Password label and entry
        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=60, y=225)
        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"), show="*")
        self.txtpass.place(x=40, y=250, width=270)

        # Login Button
        loginbtn = Button(frame, text="Login", font=("times new roman", 15, "bold"), command=self.login, bd=3, relief=RIDGE,
                          fg="white", bg="red", activeforeground="white", activebackground="red")
        loginbtn.place(x=110, y=300, width=120, height=35)

        # Register and forget buttons
        registerbtn = Button(frame, text="New User Register", font=("times new roman", 10, "bold"), command=self.register, borderwidth=0, 
                             fg="white", bg="black", activeforeground="white", activebackground="black")
        registerbtn.place(x=15, y=350, width=160)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(host='localhost', user='root', password='', database='hotelmanagement')
                my_cursor = conn.cursor()

                my_cursor.execute("SELECT * FROM account WHERE Username=%s AND Password=%s",
                                  (self.txtuser.get(), self.txtpass.get()))
                result = my_cursor.fetchone()
                conn.close()

                if result:
                    messagebox.showinfo("Success", "Login Successful!")
                    self.root.destroy()
                    root = Tk()
                    HotelManagementSystem(root)
                    root.mainloop()
                else:
                    messagebox.showerror("Error", "Invalid Username or Password")

            except Exception as ex:
                messagebox.showerror("Error", f"Error due to {str(ex)}")

    def register(self):
        self.open_window(Register_Window)

    def open_window(self, window_class):
        if not hasattr(self, 'new_window') or not self.new_window.winfo_exists():
            self.new_window = Toplevel(self.root)
            self.app = window_class(self.new_window)

if __name__ == "__main__":
    root = Tk()
    app = Login_Window(root)
    root.mainloop()
