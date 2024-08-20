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

class Booking_Room():
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        # =========================title, logo, image===================================================================
        title_lbl = Label(self.root, text="ROOM BOOKING", font=("times new roman", 18, "bold"), bg="midnight blue", fg="white",bd=3, relief=RIDGE)
        title_lbl.place(x=0, y=0, width=1300, height=40)

        img4 = Image.open(r"images\logo10.png")
        img4 = img4.resize((100, 32), Image.ANTIALIAS)
        self.photoimage4 = ImageTk.PhotoImage(img4)
        lblimg4 = Label(self.root, image=self.photoimage4, borderwidth=0)
        lblimg4.place(x=5, y=2, width=100, height=32)

        # image at right
        img3 = Image.open(r"images\bed.jpg")
        img3 = img3.resize((500, 200), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(self.root, image=self.photoimage3)
        lblimg3.place(x=800, y=55, width=500, height=200)

        # ====================Variabls==================================================================================
        #self.var_ref = StringVar()
        #x = random.randint(1000, 9999)
        #self.var_ref.set(str(x))

        self.var_mobile=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()

        # =======Left Frame details=====================================================================================
        DataFrameLeft=LabelFrame(self.root,bd=4,padx=2,relief=RIDGE,font=("arial",12,"bold"),text="Room Booking Details")
        DataFrameLeft.place(x=5,y=50,width=450,height=490)

        # Customer Phone no
        lblcusPhone=Label(DataFrameLeft,font=("arial",12,"bold"),text="Customer Phone No",padx=2,pady=6)
        lblcusPhone.grid(row=0,column=0,sticky=W)
        cust_Phone=ttk.Entry(DataFrameLeft,textvariable=self.var_mobile,font=("arial",13,"bold"),width=20)
        cust_Phone.grid(row=0,column=1,sticky=W)

        # Fetch BUTTON
        btnfetch=Button(DataFrameLeft,command=self.cont_fetch,text="Fetch Data",font=("arial",9,"bold"),width=8,bg="green",fg="white")
        btnfetch.place(x=350,y=4)

        # Check-in Date
        c_check_inDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Check-in Date:",padx=2,pady=6)
        c_check_inDate.grid(row=1,column=0,sticky=W)
        txtc_check_inDate=ttk.Entry(DataFrameLeft,textvariable=self.var_checkin,font=("arial",13,"bold"),width=29)
        txtc_check_inDate.grid(row=1,column=1)

        # Check-out Date
        lblCheckOutdate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Check-out Date:",padx=2,pady=6)
        lblCheckOutdate.grid(row=2,column=0,sticky=W)
        txtCheckOutdate=ttk.Entry(DataFrameLeft,textvariable=self.var_checkout,font=("arial",13,"bold"),width=29)
        txtCheckOutdate.grid(row=2,column=1)

        # Room Type
        label_RoomType = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Room Type:", padx=2, pady=6)
        label_RoomType.grid(row=3, column=0, sticky=W)

        comRoomType = ttk.Combobox(DataFrameLeft, state="readonly", textvariable=self.var_roomtype,font=("arial", 12, "bold"), width=27)
        comRoomType['value'] = ("Select Option", "Single", "Double", "Luxury")
        comRoomType.current(0)
        comRoomType.grid(row=3, column=1)
        comRoomType.bind("<<ComboboxSelected>>", self.update_available_rooms)

        # Available Room
        lblAvailableRoom = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Available Room:", padx=2, pady=6)
        lblAvailableRoom.grid(row=4, column=0, sticky=W)

        self.comtxtAvailableRoom = ttk.Combobox(DataFrameLeft, textvariable=self.var_roomavailable, state="readonly",font=("arial", 12, "bold"), width=27)
        self.comtxtAvailableRoom.grid(row=4, column=1)

        # Meal
        lblMeal=Label(DataFrameLeft,font=("arial",12,"bold"),text="Meal:",padx=2,pady=6)
        lblMeal.grid(row=5,column=0,sticky=W)
        comMeal=ttk.Combobox(DataFrameLeft,state="readonly",textvariable=self.var_meal,font=("arial",12,"bold"),width=27)
        comMeal['value']=("BreakFast","Lunch","Dinner")
        comMeal.current(0)
        comMeal.grid(row=5,column=1)

        # No of Days
        lblNoOfDays=Label(DataFrameLeft,font=("arial",12,"bold"),text="No Of Days:",padx=2,pady=6)
        lblNoOfDays.grid(row=6,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(DataFrameLeft,textvariable=self.var_noofdays,font=("arial",13,"bold"),width=29)
        txtNoOfDays.grid(row=6,column=1)

        # Paid Tax
        lblPaidtax=Label(DataFrameLeft,font=("arial",12,"bold"),text="Paid Tax:",padx=2,pady=6)
        lblPaidtax.grid(row=7,column=0,sticky=W)
        txtPaidtax=ttk.Entry(DataFrameLeft,textvariable=self.var_paidtax,font=("arial",13,"bold"),width=29)
        txtPaidtax.grid(row=7,column=1)

        # Actual Total
        lblsubtotal=Label(DataFrameLeft,font=("arial",12,"bold"),text="Actual Total:",padx=2,pady=6)
        lblsubtotal.grid(row=8,column=0,sticky=W)
        txtsubtotal=ttk.Entry(DataFrameLeft,textvariable=self.var_actualtotal,font=("arial",13,"bold"),width=29)
        txtsubtotal.grid(row=8,column=1)

        # Total Cost
        lblTotalCost=Label(DataFrameLeft,font=("arial",12,"bold"),text="Total Cost:",padx=2,pady=6)
        lblTotalCost.grid(row=9,column=0,sticky=W)
        txtTotalCost=ttk.Entry(DataFrameLeft,textvariable=self.var_total,font=("arial",13,"bold"),width=29)
        txtTotalCost.grid(row=9,column=1)

        # bill BUTTON
        btnBill=Button(DataFrameLeft,text="Bill",command=self.total,font=("arial",11,"bold"),width=10,bg="green",fg="white")
        btnBill.grid(row=10,column=0,sticky=W)

        # ===========Button frame-LeftDown=================================
        ButtonFrame1=Frame(DataFrameLeft,bd=3,relief=RIDGE)
        ButtonFrame1.place(x=0,y=400,width=412,height=40)

        btnAddData=Button(ButtonFrame1,text="Save",command=self.add_data,font=("arial",11,"bold"),width=10,bg="green",fg="white")
        btnAddData.grid(row=0,column=0,padx=1)

        btnShowData=Button(ButtonFrame1,text="Update",command=self.update_data,font=("arial",11,"bold"),width=10,bg="green",fg="white")
        btnShowData.grid(row=0,column=1,padx=1)

        btnUpdate=Button(ButtonFrame1,text="Delete",command=self.roomDelete,font=("arial",11,"bold"),width=10,bg="green",fg="white")
        btnUpdate.grid(row=0,column=2,padx=1)

        btnDelete=Button(ButtonFrame1,text="Reset",command=self.reset,font=("arial",11,"bold"),width=10,bg="green",fg="white")
        btnDelete.grid(row=0,column=3,padx=1)

        # =======Right Frame- table&search==============================================================================
        Table_frame=LabelFrame(self.root,text="View Customer Booking Details",font=("arial",11,"bold"),bd=3,relief=RIDGE)
        Table_frame.place(x=455,y=240,width=845,height=70)

        # Search By
        lblSearch=Label(Table_frame,font=("arial",15,"bold"),text="Search By",padx=2,bg="red",fg="white")
        lblSearch.grid(row=0,column=2,sticky=W,padx=5)

        self.serch_var=StringVar()
        search_combo=ttk.Combobox(Table_frame,width=12,textvariable=self.serch_var,font=("times new roman",15),state="readonly")
        search_combo['values']=("Select Option","contact","RoomNo")
        search_combo.grid(row=0,column=3,sticky=W,padx=5)
        search_combo.current(0)

        self.serchTxt_var=StringVar()
        txtSearch=ttk.Entry(Table_frame,width=12,textvariable=self.serchTxt_var,font=("times new roman",15))
        txtSearch.grid(row=0,column=4,padx=5)

        # Search BUTTON
        btnExit=Button(Table_frame,text="SEARCH",command=self.search_data,font=("arial",12,"bold"),width=14,bg="darkgreen",fg="white")
        btnExit.grid(row=0,column=5,padx=5)

        btnExit=Button(Table_frame,text="SHOW ALL",command=self.fatch_data,font=("arial",12,"bold"),width=13,bg="darkgreen",fg="white")
        btnExit.grid(row=0,column=6,padx=5)

        # Room_Table Scrollbar=======================
        Table_frame2=Frame(self.root,bd=4,relief=RIDGE)
        Table_frame2.place(x=455,y=290,width=845,height=250)

        scroll_x=ttk.Scrollbar(Table_frame2,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame2,orient=VERTICAL)
        self.room_table=ttk.Treeview(Table_frame2,column=("mobile","checkin","checkout","roomtype","roomavailable","meal","noOfdays",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
       
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("mobile",text="Mobile")
        self.room_table.heading("checkin",text="Check-in ")
        self.room_table.heading("checkout",text="Check-out")
        self.room_table.heading("roomtype",text="Room Type")
        self.room_table.heading("roomavailable",text="Room No")
        self.room_table.heading("meal",text="Meal")
        self.room_table.heading("noOfdays",text="NoOfDays")
        
        self.room_table["show"]="headings"
   
        self.room_table.column("mobile",width=100)
        self.room_table.column("checkin",width=100)
        self.room_table.column("checkout",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("roomavailable",width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("noOfdays",width=100)
        self.room_table.pack(fill=BOTH,expand=1)

        self.fatch_data()
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)

    # =======================Function Declaration=======================================================================

    # for showing rooms based on room_type, function called in rooms_available left frame
    def update_available_rooms(self, event=None):
        room_type = self.var_roomtype.get()
        if room_type == "Select Option":
            self.comtxtAvailableRoom['value'] = []
            return

        conn = mysql.connector.connect(host="localhost", username="root", password="Saksham123##",
                                       database="hotel_management_system")
        my_cursor = conn.cursor()
        query = "SELECT RoomNo FROM details WHERE RoomType = %s"
        my_cursor.execute(query, (room_type,))
        rooms = my_cursor.fetchall()
        conn.close()

        available_rooms = [room[0] for room in rooms]
        self.comtxtAvailableRoom['value'] = available_rooms
        if available_rooms:
            self.comtxtAvailableRoom.current(0)

    # for FETCH button- to fetch customer details from contact number
    def cont_fetch(self):
        if self.var_mobile.get() == "":
            messagebox.showerror("Error", "Please Enter Phone Number", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Saksham123##",database="hotel_management_system")
            my_cursor = conn.cursor()
            query = ("select Name,Gender,Email,Nationality,Address,Mobile from customer where Mobile=%s")
            value = (self.var_mobile.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row == None:
                messagebox.showerror("Error", "This Number Not Found", parent=self.root)
            # print(row)
            else:
                # frame for displaying data
                showDframe = Frame(self.root, bd=4, relief=RIDGE, padx=2)
                showDframe.place(x=455, y=55, width=300, height=185)

                # Customer details show
                lblname = Label(showDframe, text="Name:", font=("arial", 12, "bold"))
                lblname.place(x=0, y=0)

                lbl = Label(showDframe, text=row[0], font=("arial", 12, "bold"))
                lbl.place(x=90, y=0)

                lbladdress = Label(showDframe, text="Gender:", font=("arial", 12, "bold"))
                lbladdress.place(x=0, y=30)

                lbl1 = Label(showDframe, text=row[1], font=("arial", 12, "bold"))
                lbl1.place(x=90, y=30)

                lbladdress = Label(showDframe, text="Email:", font=("arial", 12, "bold"))
                lbladdress.place(x=0, y=60)

                lbl1 = Label(showDframe, text=row[2], font=("arial", 12, "bold"))
                lbl1.place(x=90, y=60)

                lbladdress = Label(showDframe, text="Nationality:", font=("arial", 12, "bold"))
                lbladdress.place(x=0, y=90)

                lbl1 = Label(showDframe, text=row[3], font=("arial", 12, "bold"))
                lbl1.place(x=90, y=90)

                lbladdress = Label(showDframe, text="Address:", font=("arial", 12, "bold"))
                lbladdress.place(x=0, y=120)

                lbl1 = Label(showDframe, text=row[4], font=("arial", 12, "bold"))
                lbl1.place(x=90, y=120)

                lbladdress = Label(showDframe, text="Contact:", font=("arial", 12, "bold"))
                lbladdress.place(x=0, y=150)

                lbl1 = Label(showDframe, text=row[5], font=("arial", 12, "bold"))
                lbl1.place(x=90, y=150)

                messagebox.showinfo("Success", "Customer Found", parent=self.root)

            conn.commit()
            conn.close()

    # for ADD button
    def add_data(self):
        if self.var_mobile.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Saksham123##",database="hotel_management_system")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into booking(contact,check_in,check_out,roomtype,RoomNo,meal,noOfdays) values(%s,%s,%s,%s,%s,%s,%s)",(
                        
                                                                                    self.var_mobile.get(),
                                                                                    self.var_checkin.get(),
                                                                                    self.var_checkout.get(),
                                                                                    self.var_roomtype.get(),
                                                                                    self.var_roomavailable.get(),
                                                                                    self.var_meal.get(),
                                                                                    self.var_noofdays.get()
            
                                                                                ))
                conn.commit()
                self.fatch_data()
                # self.reset()
                self.total()
                conn.close()
                        
                messagebox.showinfo("Success","Room Booked!!",parent=self.root)
                    
            except Exception as es:
                messagebox.showerror("Error",f" This Room has been Already Booked :{str(es)}",parent=self.root)

    # to fetch data from database and show on right-table
    def fatch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Saksham123##", database="hotel_management_system")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from booking")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # for selecting data from table and showing on data fields
    def get_cursor(self, event=""):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content["values"]

        self.var_mobile.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noofdays.set(row[6])

    # Update Data
    def update_data(self):
        if self.var_mobile.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password='Saksham123##',database='hotel_management_system')
            my_cursor=conn.cursor()
            my_cursor.execute("update booking set check_in=%s,check_out=%s,roomtype=%s,RoomNo=%s,meal=%s,noOfdays=%s  where contact=%s",(
                                                                             
                                                                                    self.var_checkin.get(),
                                                                                    self.var_checkout.get(),
                                                                                    self.var_roomtype.get(),
                                                                                    self.var_roomavailable.get(),
                                                                                    self.var_meal.get(),
                                                                                    self.var_noofdays.get(),
                                                                                    self.var_mobile.get()
                                                                             ))                                                                                    
            conn.commit()
            self.fatch_data()
            self.reset()
            conn.close()
            messagebox.showinfo("UPDATE","Record has been updated successfully",parent=self.root)

    # reset button
    def reset(self):
        self.var_mobile.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        # self.var_roomtype.set("")
        self.var_roomavailable.set("")
        # self.var_meal.set("")
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")

    # Delete button
    def roomDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you delete this Room",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Saksham123##",database="hotel_management_system")
            my_cursor=conn.cursor()
            sql="delete from booking where contact=%s"
            val=(self.var_mobile.get(),)
            my_cursor.execute(sql,val)

            conn.commit()
            self.fatch_data()
            # self.clear_room()
            conn.close()
        else:
            if not mDelete:
                return

    # Search button
    def search_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='Saksham123##',database='hotel_management_system')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from booking where " +str(self.serch_var.get())+" LIKE '%"+str(self.serchTxt_var.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    

    def total(self):
        InDate=self.var_checkin.get()
        OutDate=self.var_checkout.get()
        InDate=datetime.strptime(InDate,"%d/%m/%Y")
        OutDate=datetime.strptime(OutDate,"%d/%m/%Y")
        self.var_noofdays.set(abs(OutDate-InDate).days)

        if (self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Single"):
            q1=float(200)
            q2=float(1200)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        
        elif (self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Double"):
            q1=float(200)
            q2=float(1600)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        
        elif (self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Luxury"):
            q1=float(200)
            q2=float(2000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Single"):
            q1=float(250)
            q2=float(1200)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)



        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Double"):
            q1=float(250)
            q2=float(1600)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "Lunch" and self.var_roomtype.get() == "Luxury"):
            q1 = float(250)
            q2 = float(2000)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 * q4)
            Tax = "Rs." + str("%.2f" % ((q5) * 0.09))
            ST = "Rs." + str("%.2f" % ((q5)))
            TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Single"):
            q1=float(250)
            q2=float(1200)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Double"):
            q1=float(250)
            q2=float(1600)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Luxury"):
            q1=float(250)
            q2=float(2000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)


if __name__ == "__main__":
    root=Tk()
    obj=Booking_Room(root)
    root.mainloop()