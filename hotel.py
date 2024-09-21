from tkinter import *
from PIL import Image, ImageTk, ImageOps  # pip install pillow
from customer import Cust_Win
from room import Roombooking
from detail import DetailsRoom

class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        # Mở ảnh logo và thay đổi kích thước
        logo_img = Image.open("G:\\Study\\Python Assignment\\BTL_Python\\images\\logo.jpg")
        logo_img = logo_img.resize((230, 140), Image.LANCZOS)  # Resize ảnh logo

        self.photo_logo = ImageTk.PhotoImage(logo_img)

       # Mở ảnh chính và thay đổi kích thước cho phù hợp với phần còn lại
        img1 = Image.open("G:\\Study\\Python Assignment\\BTL_Python\\images\\banner.jpg")
        img1 = img1.resize((1320, 140), Image.LANCZOS)  # Resize ảnh với kích thước còn lại (1550 - 230)

        self.photoimg1 = ImageTk.PhotoImage(img1)

        # Hiển thị ảnh logo bên trái
        lbl_logo = Label(self.root, image=self.photo_logo, bd=4, relief=RIDGE)
        lbl_logo.place(x=0, y=0, width=230, height=140)

        # Hiển thị ảnh chính bên phải
        lbl_img1 = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lbl_img1.place(x=230, y=0, width=1320, height=140)

        # Title
        lbl_title = Label(self.root, text="HOTEL MANAGEMENT SYSTEM", font=("times new roman", 40, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=140, width=1550, height=50)

        # Main Frame
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=190, width=1550, height=620)

        # Menu
        lbl_menu = Label(main_frame, text="MENU", font=("times new roman", 20, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)

        # btn_Frame
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=228, height=152)

        # customer btn
        cust_btn = Button(btn_frame, text="CUSTOMER", command=self.cust_details, width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        cust_btn.grid(row=0, column=0, pady=1)

        room_btn = Button(btn_frame, text="ROOM", command=self.roombooking, width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        room_btn.grid(row=1, column=0, pady=1)

        details_btn = Button(btn_frame, text="DETAILS", command=self.detail_room, width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        details_btn.grid(row=2, column=0, pady=1)

        logout_btn = Button(btn_frame, text="LOGOUT", command=self.logout, width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        logout_btn.grid(row=3, column=0, pady=1)

        # Thêm 3 ảnh dưới nút Logout
        img2 = Image.open("G:\\Study\\Python Assignment\\BTL_Python\\images\\image1.jpg")
        img2 = img2.resize((230, 120), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        img3 = Image.open("G:\\Study\\Python Assignment\\BTL_Python\\images\\image2.jpg")
        img3 = img3.resize((230, 120), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        img4 = Image.open("G:\\Study\\Python Assignment\\BTL_Python\\images\\image3.jpg")
        img4 = img4.resize((230, 120), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        # Hiển thị 3 ảnh liên tiếp dưới nút Logout
        lbl_img2 = Label(main_frame, image=self.photoimg2, bd=4, relief=RIDGE)
        lbl_img2.place(x=0, y=200, width=230, height=120)

        lbl_img3 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lbl_img3.place(x=0, y=320, width=230, height=120)

        lbl_img4 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lbl_img4.place(x=0, y=440, width=230, height=120)

    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Cust_Win(self.new_window)

    def roombooking(self):
        self.new_window = Toplevel(self.root)
        self.app = Roombooking(self.new_window)

    def detail_room(self):
        self.new_window = Toplevel(self.root)
        self.app = DetailsRoom(self.new_window)

    def logout(self):
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()
