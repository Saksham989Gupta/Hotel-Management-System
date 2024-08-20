from tkinter import*
import tkinter
from tkinter import ttk
from tkinter import messagebox
import datetime
from PIL import Image,ImageTk
from time import strftime
from datetime import datetime
import mysql.connector
import random

class DetailsAdd:
    def __init__(self,root): 
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")


        # ==================================Title and logo=============================================================
        title_lbl=Label(self.root,text="Room Adding depatment",font=("times new roman",18,"bold"),bg="midnight blue",fg="white",bd=3,relief=RIDGE)
        title_lbl.place(x=0,y=0,width=1300,height=40)

        img4=Image.open(r"images\logo10.png")
        img4=img4.resize((100,32),Image.ANTIALIAS)
        self.photoimage4=ImageTk.PhotoImage(img4)
        lblimg4=Label(self.root,image=self.photoimage4,borderwidth=0)
        # lblimg2.place(x=690,y=0,width=220,height=140)
        lblimg4.place(x=5,y=2,width=100,height=32)

        # ===============================LeftFrame-RoomAdd Frame =======================================================

        DataFrameRight=LabelFrame(self.root,bd=4,padx=2,relief=RIDGE,fg="black",font=("arial",12,"bold"),text="Add New Rooms")
        DataFrameRight.place(x=0,y=50,width=540,height=350)

        # =======Room Images==========

        img1 = Image.open("images/room1.jpg")
        img1 = img1.resize((170,75), Image.ANTIALIAS)
        self.photoImg1 =  ImageTk.PhotoImage(img1)
        l1 =Label(DataFrameRight,image=self.photoImg1,borderwidth=0)
        l1.place(x=0,y=0)

        img2 = Image.open("images/room2.jpg")
        img2 = img2.resize((170,75), Image.ANTIALIAS)
        self.photoImg2 =  ImageTk.PhotoImage(img2)
        l2 =Label(DataFrameRight,image=self.photoImg2,borderwidth=0)
        l2.place(x=170,y=0)

        img3 = Image.open("images/room3.jpg")
        img3 = img3.resize((170,75), Image.ANTIALIAS)
        self.photoImg3 =  ImageTk.PhotoImage(img3)
        l1 =Label(DataFrameRight,image=self.photoImg3,borderwidth=0)
        l1.place(x=340,y=0)

        # ========labels & entry==========
        # Floor
        l_floor=Label(DataFrameRight,text="Floor",fg="black",font=("times new roman",15))
        l_floor.place(x=0,y=80)
        
        self.floor_add_var=StringVar()
        entry_Floor=ttk.Entry(DataFrameRight,textvariable=self.floor_add_var,width=15,font=("times new roman",15))
        entry_Floor.place(x=135,y=80)

        # Room No
        l_roomNo=Label(DataFrameRight,text="Room No",fg="black",font=("times new roman",15))
        l_roomNo.place(x=0,y=110)
        
        self.room_add_var=StringVar()
        entry_Medicine=ttk.Entry(DataFrameRight,textvariable=self.room_add_var,width=15,font=("times new roman",15))
        entry_Medicine.place(x=135,y=110)

        # Room Type
        l_roomType=Label(DataFrameRight,text="Room Type",fg="black",font=("times new roman",15))
        l_roomType.place(x=0,y=140)

        self.type_room=StringVar()  
        roomType_combo=ttk.Combobox(DataFrameRight,width=13,textvariable=self.type_room,font=("times new roman",15),state="readonly")
        roomType_combo['values']=("Select Option","Single","Double","Luxury")
        roomType_combo.place(x=135,y=140)
        roomType_combo.current(0)

        # ===========Buttons Frame============

        down_frame = Frame(DataFrameRight, bd=4, relief=RIDGE)
        down_frame.place(x=0, y=200, width=412, height=40)

        add_btn = Button(down_frame, text="ADD", command=self.add_room, font=("arial", 11, "bold"), width=10, fg="white",bg="green")
        add_btn.grid(row=0, column=0, padx=1)

        update_btn = Button(down_frame, text="UPDATE", command=self.room_update, font=("arial", 11, "bold"), width=10,fg="white", bg="green")
        update_btn.grid(row=0, column=1, padx=1)

        delete_btn = Button(down_frame, text="DELETE", command=self.roomDelete, font=("arial", 11, "bold"), width=10,fg="white", bg="green")
        delete_btn.grid(row=0, column=2, padx=1)

        clear_btn = Button(down_frame, text="CLEAR", command=self.clear_room, font=("arial", 11, "bold"), width=10,fg="white", bg="green")
        clear_btn.grid(row=0, column=3, padx=1)

        # ================================RightFrame-Room Details=======================================================
        side_frame=LabelFrame(self.root,bd=4,text="Rooms Details",relief=RIDGE,bg="white",font=("times new roman",15))
        side_frame.place(x=600,y=55,width=600,height=350)

        sc_x=ttk.Scrollbar(side_frame,orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y=ttk.Scrollbar(side_frame,orient=VERTICAL)
        sc_y.pack(side=RIGHT,fill=Y)

        self.room_table=ttk.Treeview(side_frame,column=("floor","roomno","type"),xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)

        sc_x.config(command=self.room_table.xview)
        sc_y.config(command=self.room_table.yview)

        self.room_table.heading("floor",text="Floor")
        self.room_table.heading("roomno",text="Room No")
        self.room_table.heading("type",text="Room Type")
        self.room_table["show"]="headings"
        self.room_table.column("floor",width=20)
        self.room_table.column("roomno",width=50)
        self.room_table.column("type",width=50)
        self.room_table.pack(fill=BOTH,expand=1)
        self.fetch_Room_data()
        self.room_table.bind("<ButtonRelease>",self.get_cursor_med)

    # =====================Button Functions=============================================================================

    # Add Button
    def add_room(self):
        if self.floor_add_var.get()=="" or self.room_add_var.get()=="":
            messagebox.showerror("Error","Please enter necessary details",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Saksham123##",database="hotel_management_system")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into details(floor,RoomNo,RoomType) values(%s,%s,%s)",(                                                        
                                                                                self.floor_add_var.get(),
                                                                                self.room_add_var.get(),
                                                                                self.type_room.get()
                                                                            ))
            conn.commit()
            self.fetch_Room_data()
            # self.catchdata()
            self.clear_room()
            
            conn.close()
            messagebox.showinfo("Success","Room Added!!",parent=self.root)


    
    # to fetch room details from database to right-table

    def fetch_Room_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password="Saksham123##",database="hotel_management_system")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()  

    # clear button

    def clear_room(self):
        self.floor_add_var.set("")
        self.room_add_var.set("")
        self.type_room.set("Select Option")

    # for selecting data from table and showing on data fields

    def get_cursor_med(self,event=" "):
        cursor_rows=self.room_table.focus()
        content=self.room_table.item(cursor_rows)
        row=content["values"]
        self.floor_add_var.set(row[0])
        self.room_add_var.set(row[1])
        self.type_room.set(row[2])

    # Delete button

    def roomDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you delete this Room",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Saksham123##",database="hotel_management_system")
            my_cursor=conn.cursor()
            sql="delete from details where RoomNo=%s"
            val=(self.room_add_var.get(),)
            my_cursor.execute(sql,val)
        else:
            if not mDelete:
                return 
         
        conn.commit()
        self.fetch_Room_data()
        self.clear_room()
        conn.close()

    # Update button

    def room_update(self):
            if self.floor_add_var.get()=="" or self.room_add_var.get()=="":
                messagebox.showwarning("Warning","All fields are required",parent=self.root)
            else:
                try:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Saksham123##",database="hotel_management_system")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update details set floor=%s,RoomType=%s where RoomNo=%s",(
                                                                                            self.floor_add_var.get(),
                                                                                            self.type_room.get(),
                                                                                            self.room_add_var.get()                                                                                                                               
                                                                                                                            
                                                                                         ))
                    conn.commit()
                    self.fetch_Room_data()
                    self.clear_room()
                    conn.close()
                    messagebox.showinfo("Success","Data Successfully updated",parent=self.root)

                except Exception as es:
                    messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


if __name__ == "__main__":
    root=Tk()
    obj=DetailsAdd(root)
    root.mainloop()
        
        
        

