from tkinter import *
import tkinter
from tkinter import ttk
from tkinter import messagebox
import datetime
from PIL import Image, ImageTk
from time import strftime
from datetime import datetime
import mysql.connector
import random
from customer import Cust_Win
from room import Booking_Room
from details import DetailsAdd
from Developer import Dev


def main_window():
    win = Tk()
    obj = HotelManagementSystem(win)
    win.mainloop()


class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")
        # self.root.wm_iconbitmap("") - For adding icon at window title bar

        # ======Top Candle Image=============
        img1 = Image.open(r"images\Hotel8.jpg")
        img1 = img1.resize((1550, 155))
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(self.root, image=self.photoimage1, bg="black", bd=5, relief=RIDGE)
        lblimg1.place(x=0, y=-5, width=1550, height=155)

        # ===========Logo=======================
        img2 = Image.open(r"images\logo10.png")
        img2 = img2.resize((230, 140))
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(self.root, image=self.photoimage2)
        lblimg2.place(x=3, y=1.5, width=230, height=140)

        # =================MainFrame====================================================================================
        main_frame = Frame(self.root, bd=3, relief=RIDGE)
        main_frame.place(x=0, y=180, width=1550, height=620)

        # main title
        title_lbl = Label(self.root, text="HOTEL MANAGEMENT SYSTEM", font=("times new roman", 40, "bold"), bg="midnight blue",fg="white", bd=3, relief=RIDGE)
        title_lbl.place(x=0, y=140, width=1550, height=49)

        # time display
        def time():
            string = strftime('%I:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(title_lbl, font=('times new roman', 17, 'bold'), background='midnight blue', foreground='white')
        lbl.place(x=50, y=5, width=140)
        time()

        # main frame centre image
        img3 = Image.open(r"images\main7.jpg")
        img3 = img3.resize((1320, 630))
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg1 = Label(main_frame, image=self.photoimage3, bd=5, relief=RIDGE)
        lblimg1.place(x=225, y=-9, width=1320, height=630)

        # Menu Label
        menu_lbl = Label(main_frame, text="MENU", font=("times new roman", 20, "bold"), bg="midnight blue", fg="white")
        menu_lbl.place(x=0, y=0, width=230)

        # =================== Menu buttons frame=========================

        btn_frame = Frame(main_frame, bd=1, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=228, height=190)

        add_cust = Button(btn_frame, text="CUSTOMER", bd=0, width=22, command=self.cust_details_win,font=("times new roman", 14, "bold"), bg="midnight blue", fg="white", cursor="hand2")
        add_cust.grid(row=0, column=0, pady=1)

        add_cust = Button(btn_frame, text="BOOKING", bd=0, relief=RIDGE, width=22, command=self.booking_room,font=("times new roman", 14, "bold"), bg="midnight blue", fg="white", cursor="hand2")
        add_cust.grid(row=1, column=0, pady=1)

        add_cust = Button(btn_frame, text="DETAILS", bd=0, relief=RIDGE, width=22, command=self.details_add,font=("times new roman", 14, "bold"), bg="midnight blue", fg="white", cursor="hand2")
        add_cust.grid(row=2, column=0, pady=1)

        add_cust = Button(btn_frame, text="DEVELOPER", bd=0, relief=RIDGE, width=22, command=self.developer,font=("times new roman", 14, "bold"),bg="midnight blue", fg="white", cursor="hand2")
        add_cust.grid(row=3, column=0, pady=1)

        add_cust = Button(btn_frame, text="LOGOUT ", command=self.return_login, bd=0, relief=RIDGE, width=22,font=("times new roman", 14, "bold"), bg="midnight blue", fg="white", cursor="hand2")
        add_cust.grid(row=4, column=0, pady=1)

        # Side Bar Images
        img5 = Image.open(r"images\side11.jpg")
        img5 = img5.resize((230, 210))
        self.photoimage6 = ImageTk.PhotoImage(img5)
        lblimg1 = Label(main_frame, image=self.photoimage6, bd=5, relief=RIDGE)
        lblimg1.place(x=0, y=225, width=230, height=210)

        img6 = Image.open(r"images\side22.jpg")
        img6 = img6.resize((230, 190))
        self.photoimage8 = ImageTk.PhotoImage(img6)
        lblimg1 = Label(main_frame, image=self.photoimage8, bd=5, relief=RIDGE)
        lblimg1.place(x=0, y=420, width=230, height=190)

    # ===============================Functions Definitions =============================================================
    def cust_details_win(self):
        self.new_window = Toplevel(self.root)
        self.app = Cust_Win(self.new_window)

    def booking_room(self):
        self.new_window = Toplevel(self.root)
        self.app = Booking_Room(self.new_window)

    def details_add(self):
        self.new_window = Toplevel(self.root)
        self.app = DetailsAdd(self.new_window)

    def developer(self):
        self.new_window = Toplevel(self.root)
        self.app = Dev(self.new_window)

    def return_login(self):
        self.root.destroy()


if __name__ == "__main__":
    main_window()