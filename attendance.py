from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter import filedialog
import mysql.connector
import cv2
import os
import csv
import numpy as np
from time import strftime
from datetime import datetime
from requests import delete


datai = []
class Attendence1:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendence system")

        self.var_name = StringVar()
        self.var_dep = StringVar()
        self.var_roll = StringVar()
        self.var_id = StringVar()
        self.var_tech = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_status = StringVar()


        image = Image.open(r"C:\Users\nandhini chityala\OneDrive\Pictures\Camera Roll\image7.webp")
        image = image.resize((1430, 700),Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(image)
        label1 = Label(self.root, image = self.photoimage)
        label1.pack()

        title_label = Label(label1, text = "Attendence", font = ("Bookman Old Style", 30, "bold"), fg = "black")
        title_label.place(x = 250, y = 0,width = 800, height = 100)

        la1 = Label(label1, text = "Name", font = ("Bookman Old Style", 10, "bold"), bg = "white")
        la1.place(x = 40, y = 145)
        entry1 = ttk.Entry(label1, textvariable = self.var_name, font = ("Bookman Old Style", 10, "bold"), width = 22)
        entry1.place(x = 140, y = 145)

        la2 = Label(label1, text = "Department", font = ("Bookman Old Style", 10, "bold"), bg = "white")
        la2.place(x = 40, y = 195)
        entry2 = ttk.Entry(label1, textvariable = self.var_dep, font = ("Bookman Old Style", 10, "bold"), width = 22)
        entry2.place(x = 140, y = 195)

        la3 = Label(label1, text = "roll_num", font = ("Bookman Old Style", 10, "bold"), bg = "white")
        la3.place(x = 40, y = 245)
        entry3 = ttk.Entry(label1, textvariable = self.var_roll, font = ("Bookman Old Style", 10, "bold"), width = 22)
        entry3.place(x = 140, y = 245)

        la4 = Label(label1, text = "ID", font = ("Bookman Old Style", 10, "bold"), bg = "white")
        la4.place(x = 40, y = 295)
        entry4 = ttk.Entry(label1, textvariable = self.var_id, font = ("Bookman Old Style", 10, "bold"), width = 22)
        entry4.place(x = 140, y = 295)

        la5 = Label(label1, text = "Teacher", font = ("Bookman Old Style", 10, "bold"), bg = "white")
        la5.place(x = 40, y = 345)
        entry5 = ttk.Entry(label1, textvariable = self.var_tech, font = ("Bookman Old Style", 10, "bold"), width = 22)
        entry5.place(x = 140, y = 345)

        la5 = Label(label1, text = "Time", font = ("Bookman Old Style", 10, "bold"), bg = "white")
        la5.place(x = 40, y = 395)
        entry5 = ttk.Entry(label1, textvariable = self.var_time, font = ("Bookman Old Style", 10, "bold"), width = 22)
        entry5.place(x = 140, y = 395)

        la5 = Label(label1, text = "Date", font = ("Bookman Old Style", 10, "bold"), bg = "white")
        la5.place(x = 40, y = 445)
        entry5 = ttk.Entry(label1, textvariable = self.var_date, font = ("Bookman Old Style", 10, "bold"), width = 22)
        entry5.place(x = 140, y = 445)

        la6 = Label(label1, text = "status", font = ("Bookman Old Style", 10, "bold"), bg = "white")
        la6.place(x = 40, y = 495)
        co3 = ttk.Combobox(label1, textvariable = self.var_status, font = ("Bookman Old Style", 10, "bold"), width = 20, state = "read only")
        co3["values"] = ("select", "present", "absent")
        co3.current(0)
        co3.place(x = 140, y = 495)

        bu1 = Button(label1, text = "get.csv", command = self.get, font = ("Bookman Old Style", 10, "bold"), width = 20, bg = "purple")
        bu1.place(x = 5, y = 545)

        bu2 = Button(label1, text = "remove.csv", command = self.remove, font = ("Bookman Old Style", 10, "bold"), width = 20, bg = "purple")
        bu2.place(x = 200, y = 545)

        bu4 = Button(label1, text = "reset", command = self.reset, font = ("Bookman Old Style", 10, "bold"), width = 20, bg = "purple")
        bu4.place(x = 125, y = 595)

        frame1 = Frame(label1, bd = 2, bg = "white", relief = RIDGE)
        frame1.place(x = 500, y = 145, width = 650, height = 450)

        up_down1 = ttk.Scrollbar(frame1, orient = HORIZONTAL)
        up_down2 = ttk.Scrollbar(frame1, orient = VERTICAL)
        self.Attendence1 = ttk.Treeview(frame1, columns = ("Name", "Department", "roll_num", "ID", "Teacher", "Time", "Date", "status"), xscrollcommand = up_down1.set, yscrollcommand = up_down2.set)
        up_down1.pack(side = BOTTOM, fill = X)
        up_down2.pack(side = RIGHT, fill = Y)

        up_down1.config(command = self.Attendence1.xview)
        up_down2.config(command = self.Attendence1.yview)

        self.Attendence1.heading("Name", text = "Name")
        self.Attendence1.heading("Department", text = "Department")
        self.Attendence1.heading("roll_num", text = "roll_num")
        self.Attendence1.heading("ID", text = "ID")
        self.Attendence1.heading("Teacher", text = "Teacher")
        self.Attendence1.heading("Time", text = "Time")
        self.Attendence1.heading("Date", text = "Date")
        self.Attendence1.heading("status", text = "status")

        self.Attendence1["show"] = "headings"

        self.Attendence1.column("Name", width = 70)
        self.Attendence1.column("Department", width = 70)
        self.Attendence1.column("roll_num", width = 70)
        self.Attendence1.column("ID", width = 70)
        self.Attendence1.column("Teacher", width = 70)
        self.Attendence1.column("Time", width = 70)
        self.Attendence1.column("Date", width = 70)
        self.Attendence1.column("status", width = 70)


        self.Attendence1.pack(fill = BOTH, expand = 1)
        self.Attendence1.bind("<ButtonRelease>", self.update)

    def display(self, row):
        self.Attendence1.delete(*self.Attendence1.get_children())
        for i in row:
            self.Attendence1.insert("", END, values = i)

    def get(self):
        global datai
        datai.clear()
        filename = filedialog.askopenfilename(initialdir = os.getcwd(), title = "CSV", filetypes = (("CSV File", ".csv"), ("ALL File", "*.*")), parent = self.root)
        with open(filename) as mfile:
            read1 = csv.reader(mfile, delimiter = ",")
            for i in read1:
                datai.append(i)
            self.display(datai)
    

    def remove(self):
        try:
            if len(datai) < 1:
                messagebox.showerror("ERROR", "Has no info", parent = self.root)
                return False
            filename = filedialog.asksaveasfilename(initialdir = os.getcwd(), title = "CSV", filetypes = (("CSV File", ".csv"), ("ALL File", "*.*")), parent = self.root)
            with open(filename, mode = "w", newline = "") as mfile:
                read2 = csv.writer(mfile, delimiter = ",")
                for i in datai:
                    read2.writerow(i)
                messagebox.showinfo("INFO", "EXPORTED SUCCESSFULLY TO  " +os.path.basename(filename), parent = self.root)
        except Exception as e:
            messagebox.showerror("Error", f"Due To : {str(e)}", parent = self.root)

    def update(self, event = ""):
        connect2 = self.Attendence1.focus()
        detail = self.Attendence1.item(connect2)
        content1 = detail["values"]
        self.var_name.set(content1[0])
        self.var_dep.set(content1[1])
        self.var_roll.set(content1[2])
        self.var_id.set(content1[3])
        self.var_tech.set(content1[4])
        self.var_time.set(content1[5])
        self.var_date.set(content1[6])
        self.var_status.set(content1[7])

    def reset(self):
        self.var_name.set("")
        self.var_dep.set("")
        self.var_roll.set("")
        self.var_id.set("")
        self.var_tech.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_status.set("select")
        





if __name__ == "__main__":
    root = Tk()
    obj = Attendence1(root)
    root.mainloop()