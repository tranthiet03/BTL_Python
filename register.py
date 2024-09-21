from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk #pip install pillow
from tkinter import messagebox
import mysql.connector 

class Register_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        # Background Image
        self.bg_img = Image.open(r"D:\Python\BT_Lab\BTL\BTL_Python\images\bgregister.jpg")
        self.bg_img = self.bg_img.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.bg_img)
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)
 
        # Frame for register
        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=500)

        # Register image
        img1 = Image.open(r"D:\Python\BT_Lab\BTL\BTL_Python\images\iconuser.png")
        img1 = img1.resize((100, 100), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(self.root, image=self.photoimage1, bg="black", borderwidth=0)
        lblimg1.place(x=730, y=175, width=100, height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=90,y=100)

        #==========icon===============
        #icon user
        img2 = Image.open(r"D:\Python\BT_Lab\BTL\BTL_Python\images\iconuser.png")
        img2 = img2.resize((25, 25), Image.Resampling.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(image=self.photoimage2, bg="black", borderwidth=0)
        lblimg2.place(x=645, y=323, width=25, height=25)
        
        #icon pass
        img3 = Image.open(r"D:\Python\BT_Lab\BTL\BTL_Python\images\iconpass.png")
        img3 = img3.resize((25, 25), Image.Resampling.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(image=self.photoimage3, bg="black", borderwidth=0)
        lblimg3.place(x=645, y=393, width=25, height=25)
        
        #icon confirm pass
        img4 = Image.open(r"D:\Python\BT_Lab\BTL\BTL_Python\images\iconpass.png")
        img4 = img4.resize((25, 25), Image.Resampling.LANCZOS)
        self.photoimage4 = ImageTk.PhotoImage(img4)
        lblimg4 = Label(image=self.photoimage4, bg="black", borderwidth=0)
        lblimg4.place(x=645, y=463, width=25, height=25)

        #icon confirm pass
        img5 = Image.open(r"D:\Python\BT_Lab\BTL\BTL_Python\images\type.png")
        img5 = img5.resize((25, 25), Image.Resampling.LANCZOS)
        self.photoimage5 = ImageTk.PhotoImage(img5)
        lblimg5 = Label(image=self.photoimage5, bg="black", borderwidth=0)
        lblimg5.place(x=645, y=533, width=25, height=25)

        #username
        new_user=Label(frame,text="Usename",font=("times new roman",15,"bold"),fg="white",bg="black")
        new_user.place(x=60,y=155)
        self.newuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.newuser.place(x=40,y=180,width=270)

        #password
        new_pass=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        new_pass.place(x=60,y=225)
        self.newpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.newpass.place(x=40,y=250,width=270)

        #confirm password
        confirmP=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        confirmP.place(x=60,y=295)
        self.Confirmp=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.Confirmp.place(x=40,y=320,width=270)

        # Type Account (Admin/Staff)
        type_account = Label(frame, text="Type Account", font=("times new roman", 15, "bold"), fg="white", bg="black")
        type_account.place(x=60, y=365)
        self.combo_type = ttk.Combobox(frame, font=("times new roman", 15, "bold"), state="readonly")
        self.combo_type["values"] = ("Admin", "Staff")
        self.combo_type.place(x=40, y=390, width=270)
        self.combo_type.current(0)

        #login Button
        Registerbtn=Button(frame,text="Register",command=self.register,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        Registerbtn.place(x=110,y=460,width=120,height=35)

    def register(self):
        if self.newuser.get() == "" or self.newpass.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.newpass.get() != self.Confirmp.get():
            messagebox.showerror("Error", "Confirm password is incorrect")
        else:
            try:
                conn = mysql.connector.connect(host='localhost', user='root', password='', database='hotelmanagement')
                my_cursor = conn.cursor()
                
                my_cursor.execute("SELECT * FROM account WHERE Username=%s", (self.newuser.get(),))
                result = my_cursor.fetchone()
                if result:
                    messagebox.showerror("Error", "Username already exists")
                else:
                    my_cursor.execute("INSERT INTO account (Username, Password, Type) VALUES (%s, %s, %s)",
                                      (self.newuser.get(), self.newpass.get(), self.combo_type.get()))
                    conn.commit()
                    messagebox.showinfo("Success", "Registration Successful")

                    self.root.destroy()
                    root = Tk()
                    from login import Login_Window
                    Login_Window(root)
                    root.mainloop()

            except Exception as ex:
                messagebox.showerror("Error", f"Error due to {str(ex)}")

if __name__=="__main__":
    root=Tk()
    app=Register_Window(root)
    root.mainloop()
