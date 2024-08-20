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
from customer import Cust_Win
from room import Booking_Room
from details import DetailsAdd

class Dev:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x580+230+220")

        # background image- Tiles
        self.bg = ImageTk.PhotoImage(file=r"images\Hotel6.jpg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # ========================Title nad logo====================
        title_lbl = Label(self.root, text="ABOUT DEVELOPER", font=("times new roman", 18, "bold"), bg="midnight blue",fg="white", bd=3, relief=RIDGE)
        title_lbl.place(x=0, y=0, width=1300, height=40)

        img4 = Image.open(r"images\logo10.png")
        img4 = img4.resize((100, 32))
        self.photoimage4 = ImageTk.PhotoImage(img4)
        lblimg4 = Label(self.root, image=self.photoimage4, borderwidth=0)
        lblimg4.place(x=5, y=2, width=100, height=32)

        # ========================Main Frame===============================
        frame = Frame(self.root, bg="midnight blue", bd=7, relief=RIDGE)
        frame.place(x=330, y=90, width=600, height=430)

        # Pic
        img5 = Image.open(r"images\pic.jpeg")
        img5 = img5.resize((200, 200))
        self.photoimage5 = ImageTk.PhotoImage(img5)
        lblimg5 = Label(frame, image=self.photoimage5, borderwidth=0)
        lblimg5.place(x=180, y=20, width=200, height=200)

        # Name
        name = Label(frame, text="SAKSHAM  GUPTA", font=("times new roman", 18, "bold"), bg="white",fg="midnight blue", bd=3, relief=RIDGE)
        name.place(x=0, y=280, width=588, height=40)
