from tkinter import*
import tkinter
from tkinter import ttk                     # for entry field, combobox, scrollbar
from tkinter import messagebox
import datetime
from PIL import Image,ImageTk
from time import strftime
from datetime import datetime
import mysql.connector
import random

class Cust_Win():
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        # ========================Title nad logo====================
        title_lbl = Label(self.root, text="ADD CUSTOMER DETAILS", font=("times new roman", 18, "bold"), bg="midnight blue",fg="white", bd=3, relief=RIDGE)
        title_lbl.place(x=0, y=0, width=1300, height=40)

        img4 = Image.open(r"images\logo10.png")
        img4 = img4.resize((100, 32))
        self.photoimage4 = ImageTk.PhotoImage(img4)
        lblimg4 = Label(self.root, image=self.photoimage4, borderwidth=0)
        lblimg4.place(x=5, y=2, width=100, height=32)

        # ====================Variabls========================
        self.var_ref = StringVar()
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_adderss=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()

        # =======Left_LabelFrame_details===================================================================================
        
        DataFrameLeft=LabelFrame(self.root,bd=2,padx=2,relief=RIDGE,font=("arial",12,"bold"),text="Customer Details")
        DataFrameLeft.place(x=5,y=50,width=425,height=490)
 
        lblcusref=Label(DataFrameLeft,font=("arial",12,"bold"),text="Customer Ref",padx=2,pady=6)
        lblcusref.grid(row=0,column=0,sticky=W)
        cust_ref=ttk.Entry(DataFrameLeft,textvariable=self.var_ref,font=("arial",13,"bold"),width=29,state=DISABLED)
        cust_ref.grid(row=0,column=1)

        cname=Label(DataFrameLeft,font=("arial",12,"bold"),text="Customer Name:",padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)
        txtcname=ttk.Entry(DataFrameLeft,textvariable=self.var_cust_name,font=("arial",13,"bold"),width=29)
        txtcname.grid(row=1,column=1)

        lblmname=Label(DataFrameLeft,font=("arial",12,"bold"),text="Mother Name:",padx=2,pady=6)
        lblmname.grid(row=2,column=0,sticky=W)
        txtmname=ttk.Entry(DataFrameLeft,textvariable=self.var_mother,font=("arial",13,"bold"),width=29)
        txtmname.grid(row=2,column=1)

        label_gender=Label(DataFrameLeft,font=("arial",12,"bold"),text="Gender:",padx=2,pady=6)
        label_gender.grid(row=3,column=0,sticky=W)
        comgender=ttk.Combobox(DataFrameLeft,state="readonly",textvariable=self.var_gender,
                                                        font=("arial",12,"bold"),width=27)
        comgender['value']=("Male","Female","Other")
        comgender.current(0)
        comgender.grid(row=3,column=1)

        lblPostCode=Label(DataFrameLeft,font=("arial",12,"bold"),text="PostCode:",padx=2,pady=6)
        lblPostCode.grid(row=4,column=0,sticky=W)
        txtPostCode=ttk.Entry(DataFrameLeft,textvariable=self.var_post,font=("arial",13,"bold"),width=29)
        txtPostCode.grid(row=4,column=1)

        lblMobile=Label(DataFrameLeft,font=("arial",12,"bold"),text="Mobile:",padx=2,pady=6)
        lblMobile.grid(row=5,column=0,sticky=W)
        txtMobile=ttk.Entry(DataFrameLeft,textvariable=self.var_mobile,font=("arial",13,"bold"),width=29)
        txtMobile.grid(row=5,column=1)

        lblEmail=Label(DataFrameLeft,font=("arial",12,"bold"),text="Email:",padx=2,pady=6)
        lblEmail.grid(row=6,column=0,sticky=W)
        txtEmail=ttk.Entry(DataFrameLeft,textvariable=self.var_email,font=("arial",13,"bold"),width=29)
        txtEmail.grid(row=6,column=1)

        lblNationality=Label(DataFrameLeft,font=("arial",12,"bold"),text="Nationality:",padx=2,pady=6)
        lblNationality.grid(row=7,column=0,sticky=W)
        comNationality=ttk.Combobox(DataFrameLeft,state="readonly",textvariable=self.var_nationality,font=("arial",12,"bold"),width=27)
        comNationality['value']=("Indian","British","American","chinese","Other")
        comNationality.current(0)
        comNationality.grid(row=7,column=1)

        lblIdProof=Label(DataFrameLeft,font=("arial",12,"bold"),text="Id Proof Type:",padx=2,pady=6)
        lblIdProof.grid(row=8,column=0,sticky=W)
        comIdProof=ttk.Combobox(DataFrameLeft,state="readonly",textvariable=self.var_id_proof,font=("arial",12,"bold"),width=27)
        comIdProof['value']=("AadharCard","PanCard","DrivingLicence")
        comIdProof.current(0)
        comIdProof.grid(row=8,column=1)

        lblIdNumber=Label(DataFrameLeft,font=("arial",12,"bold"),text="Id Number:",padx=2,pady=6)
        lblIdNumber.grid(row=9,column=0,sticky=W)
        txtIdNumber=ttk.Entry(DataFrameLeft,textvariable=self.var_id_number,font=("arial",13,"bold"),width=29)
        txtIdNumber.grid(row=9,column=1)

        lblAddress=Label(DataFrameLeft,font=("arial",12,"bold"),text="Address:",padx=2,pady=6)
        lblAddress.grid(row=10,column=0,sticky=W)
        txtAddress=ttk.Entry(DataFrameLeft,textvariable=self.var_adderss,font=("arial",13,"bold"),width=29)
        txtAddress.grid(row=10,column=1)

        # ===========Buttonframe and its Buttons on LeftDataFrame=======================================================
        ButtonFrame=Frame(DataFrameLeft,bd=3,relief=RIDGE)
        ButtonFrame.place(x=0,y=400,width=412,height=40)

        btnAddData=Button(ButtonFrame,text="Add",command=self.add_data,font=("arial",11,"bold"),width=10,bg="green",fg="white")
        btnAddData.grid(row=0,column=0,padx=1)

        btnUpdate=Button(ButtonFrame,text="Update",command=self.update_data,font=("arial",11,"bold"),width=10,bg="green",fg="white")
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(ButtonFrame,text="Delete",command=self.mDelete,font=("arial",11,"bold"),width=10,bg="green",fg="white")
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(ButtonFrame,text="Reset",command=self.reset,font=("arial",11,"bold"),width=10,bg="green",fg="white")
        btnReset.grid(row=0,column=3,padx=1)

        # ===========================RightDataFrame-Database Table&Scrollbar============================================
        Table_frame=LabelFrame(self.root,text="View Customer Details & Search",font=("arial",11,"bold"),bd=3,relief=RIDGE)
        Table_frame.place(x=435,y=50,width=860,height=490)

        lblSearch=Label(Table_frame,font=("arial",15,"bold"),text="Search By",padx=2,bg="red",fg="white")
        lblSearch.grid(row=0,column=2,sticky=W,padx=5)

        self.serch_var=StringVar()
        search_combo=ttk.Combobox(Table_frame,width=12,textvariable=self.serch_var,font=("times new roman",15),state="readonly")
        search_combo['values']=("Select Option","Ref","Mobile","Email")
        search_combo.current(0)
        search_combo.grid(row=0,column=3,sticky=W,padx=5)

        self.serchTxt_var=StringVar()
        txtSearch=ttk.Entry(Table_frame,width=12,textvariable=self.serchTxt_var,font=("times new roman",15))
        txtSearch.grid(row=0,column=4,padx=5)

        btn_search=Button(Table_frame,text="SEARCH",command=self.search_data,font=("arial",12,"bold"),width=14,bg="darkgreen",fg="white")
        btn_search.grid(row=0,column=5,padx=5)

        btn_show=Button(Table_frame,text="SHOW ALL",command=self.fatch_data,font=("arial",12,"bold"),width=13,bg="darkgreen",fg="white")
        btn_show.grid(row=0,column=6,padx=5)

                                 # ===============Table&Scrollbar==================
        details_table=Frame(Table_frame,bd=6,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=350)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        self.Cust_Details_Table=ttk.Treeview(details_table,column=("ref","name","mother","gender","post","mobile",
                                                                   "email","nationality","idproof","idnumber","address")
                                                                    ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
       
        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref",text="Refer No")
        self.Cust_Details_Table.heading("name",text="Name")
        self.Cust_Details_Table.heading("mother",text="Mother Name")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("post",text="PostCode")
        self.Cust_Details_Table.heading("mobile",text="Mobile")
        self.Cust_Details_Table.heading("email",text="Email")
        self.Cust_Details_Table.heading("nationality",text="Nationality")
        self.Cust_Details_Table.heading("idproof",text="Id Proof")
        self.Cust_Details_Table.heading("idnumber",text="Id Number")
        self.Cust_Details_Table.heading("address",text="Address")
        
        
        self.Cust_Details_Table["show"]="headings"
   
        self.Cust_Details_Table.column("ref",width=100)
        self.Cust_Details_Table.column("name",width=100)
        self.Cust_Details_Table.column("mother",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("post",width=100)
        self.Cust_Details_Table.column("mobile",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("nationality",width=100)
        self.Cust_Details_Table.column("idproof",width=100)
        self.Cust_Details_Table.column("idnumber",width=100)
        self.Cust_Details_Table.column("address",width=100)

        self.Cust_Details_Table.pack(fill=BOTH,expand=1)

        self.fatch_data()
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)

    # =======================Function Declaration==================================================
    #==========Add_data to add data to database==============
    def add_data(self):
        if self.var_ref.get()=="" or self.var_mobile.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Saksham123##",database="hotel_management_system")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                
                                                                                self.var_ref.get(),
                                                                                self.var_cust_name.get(),
                                                                                self.var_mother.get(),
                                                                                self.var_gender.get(),
                                                                                self.var_post.get(),
                                                                                self.var_mobile.get(),
                                                                                self.var_email.get(),
                                                                                self.var_nationality.get(),
                                                                                self.var_id_proof.get(),
                                                                                self.var_id_number.get(),
                                                                                self.var_adderss.get()
                                                                                ))
                conn.commit()
                self.fatch_data()
                self.reset()
                conn.close()
                messagebox.showinfo("Success","Customer has been inserted",parent=self.root)
             
            except Exception as es:
                messagebox.showerror("Error",f" Must be enter Integer number, is Primery Key :{str(es)}",parent=self.root)

    # =========Fetch data- to fetch data from database and show on table===================================

    def fatch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root",password="Saksham123##",database="hotel_management_system")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # ===========getcursor- to show data from table to entry field for updation==================================
    def get_cursor(self, event=""):
        cursor_row = self.Cust_Details_Table.focus()
        content = self.Cust_Details_Table.item(cursor_row)
        row = content["values"]

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_adderss.set(row[10])

    # =========Update Data- to update data=================================
    def update_data(self):
        if self.var_ref.get()=="" or self.var_mobile.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password="Saksham123##",database="hotel_management_system")
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set  Name=%s,Mother=%s,Gender=%s,PostCode=%s,Mobile=%s,Email=%s,Nationality=%s,Idproof=%s,Idnumber=%s,Address=%s where Ref=%s",(
                                                                               
                                                                                self.var_cust_name.get(),
                                                                                self.var_mother.get(),
                                                                                self.var_gender.get(),
                                                                                self.var_post.get(),
                                                                                self.var_mobile.get(),
                                                                                self.var_email.get(),
                                                                                self.var_nationality.get(),
                                                                                self.var_id_proof.get(),
                                                                                self.var_id_number.get(),
                                                                                self.var_adderss.get(),
                                                                                self.var_ref.get()
                                                                             ))
                                                                                                    
            conn.commit()
            self.fatch_data()
            self.reset()
            conn.close()
            messagebox.showinfo("UPDATE","Record has been updated successfully",parent=self.root)

    # ========Reset data===================
    def reset(self):
        # self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_mother.set(""),
        # self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        # self.var_nationality.set(""),
        # self.var_id_proof.get(),
        self.var_id_number.set(""),
        self.var_adderss.set("")
    
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

    # =============DealeteData===============
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you delete this Room",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Saksham123##",database="hotel_management_system")
            my_cursor=conn.cursor()
            sql="delete from customer where Ref=%s"
            val=(self.var_ref.get(),)
            my_cursor.execute(sql,val)
            conn.commit()
            self.fatch_data()
            conn.close()
        else:
            if not mDelete:
                return 

    def search_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password="Saksham123##",database="hotel_management_system")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer where " +str(self.serch_var.get())+" LIKE '%"+str(self.serchTxt_var.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()
    

if __name__ == "__main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()