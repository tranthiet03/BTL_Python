from tkinter import *
from tkinter import ttk
from time import strftime
from datetime import datetime
import mysql.connector      #pip install mysql-connector-python
from tkinter import messagebox

class DetailsRoom:
    def __init__(self, root, user_type):
        self.root = root
        self.user_type = user_type
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        #Title
        lbl_title = Label(self.root, text="ADDING NEW ROOM", font=("arial",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        #labelframe
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",font=("arial",12,"bold"),padx=2,)
        labelframeleft.place(x=5,y=50,width=540,height=350)

        #Floor
        self.var_floor=StringVar()
        lbl_floor=Label(labelframeleft,text="Floor:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W,padx=20)

        entry_floor=ttk.Entry(labelframeleft,textvariable=self.var_floor,width=20,font=("arial",13,"bold"))
        entry_floor.grid(row=0,column=1,sticky=W)

        #Room No
        self.var_roomNo=StringVar()
        lbl_RoomNo=Label(labelframeleft,text="Room No:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_RoomNo.grid(row=1,column=0,sticky=W,padx=20)
        
        entry_RoomNo=ttk.Entry(labelframeleft,textvariable=self.var_roomNo,width=20,font=("arial",13,"bold"))
        entry_RoomNo.grid(row=1,column=1,sticky=W)

        #Room Type
        self.var_roomType=StringVar()
        lbl_roomType=Label(labelframeleft,text="Room Type:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_roomType.grid(row=2,column=0,sticky=W,padx=20)

        combo_roomtype=ttk.Combobox(labelframeleft,textvariable=self.var_roomType,font=("arial",12,"bold"),width=20,state="readonly")
        combo_roomtype["value"]=("Single","Double","Luxury")
        combo_roomtype.current(0)
        combo_roomtype.grid(row=2,column=1,sticky=W)

        # ==========Button================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=412,height=35)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)
        
        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.delete,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnReset.grid(row=0,column=3,padx=1)

        # ==============table frame============
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details",font=("arial",12,"bold"),padx=2,)
        Table_Frame.place(x=600,y=50,width=600,height=350)

        scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)

        self.room_table=ttk.Treeview(Table_Frame,columns=("floor","roomno","roomtype"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("floor",text="Floor")
        self.room_table.heading("roomno",text="Room No")
        self.room_table.heading("roomtype",text="Room Type")

        self.room_table["show"]="headings"

        self.room_table.column("floor",width=100)
        self.room_table.column("roomno",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.pack(fill=BOTH,expand=1)

        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_floor.get()=="" or self.var_roomType.get()=="":
            messagebox.showerror("Error","All fields are requaired",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host='localhost',user='root',password='',database='hotelmanagement')
                my_cursor=conn.cursor()
                my_cursor.execute("insert into detail values(%s,%s,%s)",(
                                                                        self.var_floor.get(),
                                                                        self.var_roomNo.get(),
                                                                        self.var_roomType.get(),
                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","New Room Added Successfuly",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)
    
    #fetch_data
    def fetch_data(self):
        conn = mysql.connector.connect(host='localhost',user='root',password='',database='hotelmanagement')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from detail")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #get cursor
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_floor.set(row[0])
        self.var_roomNo.set(row[1])
        self.var_roomType.set(row[2])

    #update
    def update(self):
        if self.var_floor.get()=="":
            messagebox.showerror("Error","Please enter floor number",parent=self.root)
        else:
            conn = mysql.connector.connect(host='localhost',user='root',password='',database='hotelmanagement')
            my_cursor=conn.cursor()
            my_cursor.execute("update detail set Floor=%s,RoomType=%s where RoomNo=%s",(
                                                                                self.var_floor.get(),
                                                                                self.var_roomType.get(),
                                                                                self.var_roomNo.get()
                                                                                ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room details has been updated successfully",parent=self.root)

    def delete(self):
        delete=messagebox.askyesno("Hotel Management System","Do you want delete this room",parent=self.root)
        if delete>0:
            conn = mysql.connector.connect(host='localhost',user='root',password='',database='hotelmanagement')
            my_cursor=conn.cursor()
            query="delete from detail where RoomNo=%s"
            value=(self.var_roomNo.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    #reset
    def reset(self):
        self.var_floor.set(""),
        self.var_roomNo.set(""),
        self.var_roomType.set(""),
















if __name__ == "__main__":
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop()