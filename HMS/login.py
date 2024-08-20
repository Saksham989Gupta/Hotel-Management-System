from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import random
import time
import datetime
import mysql.connector
from home import HotelManagementSystem

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        self.root.configure(bg="light blue")

        # background image- Tiles
        self.bg=ImageTk.PhotoImage(file=r"images\Hotel6.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        # ==================Title Bar with Logo=========================================================================

        title_lbl=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="midnight blue",fg="white",bd=3,relief=RIDGE)
        title_lbl.place(x=0,y=0,width=1550,height=80)

        img4 = Image.open(r"images\logo10.png")
        img4 = img4.resize((105, 74))
        self.photoimage4 = ImageTk.PhotoImage(img4)
        lblimg4 = Label(self.root, image=self.photoimage4, borderwidth=0)
        lblimg4.place(x=5, y=2, width=105, height=74)

        # =======================Login-MainFrame========================================================================

        # Frame
        frame=Frame(self.root,bg="midnight blue",bd=7,relief=RIDGE)
        frame.place(x=610,y=170,width=340,height=430)

        # Logo on Frame
        img1=Image.open(r"images\logo10.png")
        img1=img1.resize((90,90))
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=181,width=90,height=80)

        # Labels and Entry fields
        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="midnight blue")
        get_str.place(x=95,y=85)

        username=lbl=Label(frame,text="Username",font=("times new roman",12,"bold"),fg="white",bg="midnight blue")
        username.place(x=70,y=125)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=150,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",12,"bold"),fg="white",bg="midnight blue")
        password.place(x=70,y=195)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"),show="*")
        self.txtpass.place(x=40,y=220,width=270)

        # Icon Images
        img2=Image.open(r"images\LoginIconAppl.png")
        img2=img2.resize((25,25))
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="midnight blue",borderwidth=0)
        lblimg1.place(x=650,y=293,width=25,height=25)


        img3=Image.open(r"images\lock-512.png")
        img3=img3.resize((25,25))
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimage3,bg="midnight blue",borderwidth=0)
        lblimg1.place(x=650,y=365,width=25,height=25)

        # LoginButton
        btn_login=Button(frame,text="Login",borderwidth=3,relief=RAISED,command=self.login,cursor="hand2",font=("times new roman",16,"bold"),fg="white",bg="red" ,activebackground="#B00857")
        btn_login.place(x=110,y=270,width=120,height=35)

        # Register Button
        registerbtn=Button(frame,text="Admin Register",command=self.rigister_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="midnight blue",activeforeground="white",activebackground="midnight blue")
        registerbtn.place(x=8,y=320,width=160)

        # Forget Password Button
        registerbtn=Button(frame,text="Forget Password",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="midnight blue",activeforeground="white",activebackground="midnight blue")
        registerbtn.place(x=10,y=340,width=160)

        # Delete Current Admin Button
        registerbtn = Button(frame, text="Delete Current Admin", command=self.del_admin,font=("times new roman", 10, "bold"), borderwidth=0, fg="white", bg="midnight blue",activeforeground="white", activebackground="midnight blue")
        registerbtn.place(x=24, y=360, width=160)

    # ======================================Button Functions============================================================

    # Login Button
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields are required")
        elif self.txtuser.get()=="saksham" and self.txtpass.get()=="saksham":
            self.txtuser.delete(0,END)
            self.txtpass.delete(0,END)
            self.new_window = Toplevel(self.root)
            self.app = HotelManagementSystem(self.new_window)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Saksham123##",database="hotel_management_system")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                    self.txtuser.get(),
                                                                                    self.txtpass.get()
                                                                            ))

            row=my_cursor.fetchone()
            # print(row)
            if row==None:
                messagebox.showerror("Error","Inavalid Username & password")
            else:
                self.txtuser.delete(0, END)
                self.txtpass.delete(0, END)
                self.new_window = Toplevel(self.root)
                self.app = HotelManagementSystem(self.new_window)

            conn.commit()
            conn.close()

    # Register Button( Register window code at bottom)
    def rigister_window(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="Saksham123##",database="hotel_management_system")
        my_cursor = conn.cursor()
        query = ("select * from register")
        my_cursor.execute(query,)
        row = my_cursor.fetchone()
        if row == None:
            self.new_window = Toplevel(self.root)
            self.app = Register(self.new_window)
        else:
            messagebox.showerror("Error", "Admin already exist")

    # Delete Current Admin Button
    def del_admin(self):
        if self.txtuser.get() == "" or self.txtpass.get()=="":
            messagebox.showerror("Error", "Please Enter the Username and Password")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Saksham123##",database="hotel_management_system")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s", (
                                                                                            self.txtuser.get(),
                                                                                            self.txtpass.get()
                                                                                       ))
            row = my_cursor.fetchone()
            # print(row)
            if row == None:
                messagebox.showerror("Error", "Invalid Username or password")
            else:
                my_cursor.execute("delete from register")
                self.txtuser.delete(0, END)
                self.txtpass.delete(0, END)
                messagebox.showinfo("Success", "Current Admin Deleted")
            conn.commit()
            conn.close()
    # ==================================Forget Password Button and window function======================================

    # Forget Password Button
    def forgot_password_window(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error", "Please Enter the Username to reset password")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Saksham123##", database="hotel_management_system")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s")
            value = (self.txtuser.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            # print(row)

            if row == None:
                messagebox.showerror("Error", "Please enter the valid username")
            else:
                self.root2 = Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")
                self.root2.configure(bg="midnight blue")

                l = Label(self.root2, text="Forget Password", font=("times new roman", 20, "bold"), fg="white",bg="midnight blue")
                l.place(x=0, y=10, relwidth=1)

                security_Q = Label(self.root2, text="Select a Security Question", font=("times new roman", 15, "bold"),bg="midnight blue", fg="white")
                security_Q.place(x=50, y=80)

                self.combo_securiy_Q = ttk.Combobox(self.root2, font=("times new roman", 15, "bold"), state="readonly")
                self.combo_securiy_Q["values"] = ("Select", "Your Birth Place", "Your Grandmother name", "Your Pet Name")
                self.combo_securiy_Q.place(x=50, y=110, width=250)
                self.combo_securiy_Q.current(0)

                security_A = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), bg="midnight blue",fg="white")
                security_A.place(x=50, y=150)

                self.txt_security = ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
                self.txt_security.place(x=50, y=180, width=250)

                new_password = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="midnight blue",fg="white")
                new_password.place(x=50, y=220)

                self.txt_newpass = ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
                self.txt_newpass.place(x=50, y=250, width=250)

                btn = Button(self.root2, text="Reset",borderwidth=3,relief=RAISED, command=self.reset_pass, font=("times new roman", 15, "bold"),fg="White", bg="red",activebackground="#B00857")
                btn.place(x=120, y=290, width=100)

            conn.close()

    # Reset Password Button in Forget Password Window
    def reset_pass(self):
        if self.combo_securiy_Q.get()=="Select" or self.txt_security.get()=="" or self.txt_newpass=="":
            messagebox.showerror("Error","All fields are required",parent=self.root2)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root", password="Saksham123##", database="hotel_management_system")
                cur=conn.cursor()
                query=("select * from register where email=%s and securityQ=%s and securityA=%s")
                value=(self.txtuser.get(),self.combo_securiy_Q.get(),self.txt_security.get(),)
                cur.execute(query,value)
                row=cur.fetchone()
                # print(row)
                if row==None:
                    messagebox.showerror("Error","Incorrect security Question/Answer",parent=self.root2)
                else:
                    query=("update register set password=%s where email=%s")
                    value=(self.txt_newpass.get(),self.txtuser.get())
                    cur.execute(query,value)
                    conn.commit() 
                    conn.close()
                    messagebox.showinfo("Success","Your password has been reset,Please login with new password",parent=self.root2)
                    self.root2.destroy()
                    self.txtpass.delete(0, END)
                    self.txtuser.focus()

            except Exception as es:
                messagebox.showerror("Error",f"Error Due To:{str(es)}",parent=self.root2)

# =============================================Register window==========================================================

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        # BG image- Tiles
        self.bg = ImageTk.PhotoImage(file=r"images\Hotel6.jpg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # ==================Title Bar with Logo=========================================================================
        title_lbl = Label(self.root, text="HOTEL MANAGEMENT SYSTEM", font=("times new roman", 40, "bold"),bg="midnight blue", fg="white", bd=3, relief=RIDGE)
        title_lbl.place(x=0, y=0, width=1550, height=90)

        img4 = Image.open(r"images\logo10.png")
        img4 = img4.resize((105, 84))
        self.photoimage4 = ImageTk.PhotoImage(img4)
        lblimg4 = Label(self.root, image=self.photoimage4, borderwidth=0)
        lblimg4.place(x=5, y=2, width=105, height=84)

        # ==================varibles====================================================================================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_SecurityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        # ==============Main Frame- Register======================================================================================
        frame=Frame(self.root,bg="midnight blue",bd=7,relief=RIDGE)
        frame.place(x=370,y=170,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="white",bg="midnight blue")
        register_lbl.place(x=265,y=20)

        # ==============label and entry============================

        # row1
        fname=Label(frame,text="First Name:",font=("times new roman",15,"bold"),bg="midnight blue",fg="white")
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name:",font=("times new roman",15,"bold"),bg="midnight blue",fg="white")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txt_lname.place(x=370,y=130,width=250)

        # row2
        contact=Label(frame,text="Contact No:",font=("times new roman",15,"bold"),bg="midnight blue",fg="white")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Username/Email:",font=("times new roman",15,"bold"),bg="midnight blue",fg="white")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txt_email.place(x=370,y=200,width=250)

        # row3
        security_Q=Label(frame,text="Select Security Question:",font=("times new roman",15,"bold"),bg="midnight blue",fg="white")
        security_Q.place(x=50,y=240)

        self.combo_securiy_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_securiy_Q["values"]=("Select","Your Birth Place","Your Grandmother name","Your Pet Name")
        self.combo_securiy_Q.place(x=50,y=270,width=250)
        self.combo_securiy_Q.current(0)

        security_A=Label(frame,text="Security Answer:",font=("times new roman",15,"bold"),bg="midnight blue",fg="white")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_SecurityA,font=("times new roman",15,"bold"))
        self.txt_security.place(x=370,y=270,width=250)

        # row4
        pswd=Label(frame,text="Password:",font=("times new roman",15,"bold"),bg="midnight blue",fg="white")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password:",font=("times new roman",15,"bold"),bg="midnight blue",fg="white")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

        # =================Buttons========================
        b1=Button(frame,text="Register Now",borderwidth=3,relief=RAISED,command=self.register_data,cursor="hand2",font=("times new roman",16,"bold"),fg="white",bg="red" ,activebackground="#B00857")
        b1.place(x=50,y=420,width=200)

        b1=Button(frame,text="Back",borderwidth=3,relief=RAISED,command=self.return_login,cursor="hand2",font=("times new roman",16,"bold"),fg="white",bg="red" ,activebackground="#B00857")
        b1.place(x=380,y=420,width=200)

    # =================Function declaration=============================================================================

    # Register Now Button
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select" or self.var_SecurityA.get()=="" or self.var_pass.get()=="":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password & confirm password must be same")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Saksham123##",database="hotel_management_system")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist,please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_pass.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_SecurityA.get(),
                                                                                     ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Admin Registered Successfully")
            self.root.destroy()

    # Login Now Button
    def return_login(self):
        self.root.destroy()
           

if __name__ == "__main__":
    main()
