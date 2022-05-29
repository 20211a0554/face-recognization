from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendence system")

        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_section = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        
        image = Image.open(r"C:\Users\nandhini chityala\OneDrive\Pictures\Camera Roll\image7.webp")
        image = image.resize((1530, 790),Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(image)
        label1 = Label(self.root, image = self.photoimage)
        label1.pack()

        lframe = LabelFrame(label1, relief = RIDGE, text = "ENTER DETAILS", font = ("Bookman Old Style", 16, "bold"))
        lframe.place(x = 20, y = 20, width = 600, height = 600)

        l1 = Label(lframe, text = "Department", font = ("Bookman Old Style", 10, "bold"), bg = "white")
        l1.grid(row = 0, column = 0, padx = 40)
        co1 = ttk.Combobox(lframe, textvariable = self.var_dep,font = ("Bookman Old Style", 10, "bold"), width = 20, state = "read only")
        co1["values"] = ("Select department", "CSE", "ECE", "EEE", "IT", "MECH", "CIVIL", "CHEM")
        co1.current(0)
        co1.grid(row = 0, column = 1, padx = 20, pady = 4, sticky = W)

        l2 = Label(lframe, text = "Course", font = ("Bookman Old Style", 10, "bold"), bg = "white")
        l2.grid(row = 1, column = 0, padx = 40)
        co2 = ttk.Combobox(lframe, textvariable = self.var_course, font = ("Bookman Old Style", 10, "bold"), width = 20, state = "read only")
        co2["values"] = ("Select course", "class 1", "class 2", "class 3", "class 4", "class 5", "class 6", "class 7")
        co2.current(0)
        co2.grid(row = 1, column = 1, padx = 20, pady = 4, sticky = W)

        l3 = Label(lframe, text = "year", font = ("Bookman Old Style", 10, "bold"), bg = "white")
        l3.grid(row = 2, column = 0, padx = 40)
        co3 = ttk.Combobox(lframe, textvariable = self.var_year, font = ("Bookman Old Style", 10, "bold"), width = 20, state = "read only")
        co3["values"] = ("Select year", "I", "II", "III", "IV")
        co3.current(0)
        co3.grid(row = 2, column = 1, padx = 20, pady = 4, sticky = W)

        l4 = Label(lframe, text = "semester", font = ("Bookman Old Style", 10, "bold"), bg = "white")
        l4.grid(row = 3, column = 0, padx = 40)
        co4 = ttk.Combobox(lframe, textvariable = self.var_sem, font = ("Bookman Old Style", 10, "bold"), width = 20, state = "read only")
        co4["values"] = ("Select semester", "sem 1", "sem 2")
        co4.current(0)
        co4.grid(row = 3, column = 1, padx = 20, pady = 4, sticky = W)

        l5 = Label(lframe, text = "ID", font = ("Bookman Old Style", 10, "bold"), bg = "white")
        l5.grid(row = 4, column = 0, padx = 40)
        entry1 = ttk.Entry(lframe, textvariable = self.var_id, font = ("Bookman Old Style", 10, "bold"), width = 22)
        entry1.grid(row = 4, column = 1, padx = 20, pady = 4, sticky = W)

        
        l6 = Label(lframe, text = "Name", font = ("Bookman Old Style", 10, "bold"), bg = "white")
        l6.grid(row = 5, column = 0, padx = 40)
        entry2 = ttk.Entry(lframe, textvariable = self.var_name, font = ("Bookman Old Style", 10, "bold"), width = 22)
        entry2.grid(row = 5, column = 1, padx = 20, pady = 4, sticky = W)

        l7 = Label(lframe, text = "section", font = ("Bookman Old Style", 10, "bold"), bg = "white")
        l7.grid(row = 6, column = 0, padx = 40)
        entry3 = ttk.Entry(lframe, textvariable = self.var_section, font = ("Bookman Old Style", 10, "bold"), width = 22)
        entry3.grid(row = 6, column = 1, padx = 20, pady = 4, sticky = W)

        l8 = Label(lframe, text = "roll_num", font = ("Bookman Old Style", 10, "bold"), bg = "white")
        l8.grid(row = 7, column = 0, padx = 40)
        entry4 = ttk.Entry(lframe, textvariable = self.var_roll, font = ("Bookman Old Style", 10, "bold"), width = 22)
        entry4.grid(row = 7, column = 1, padx = 20, pady = 4, sticky = W)

        l9 = Label(lframe, text = "gender", font = ("Bookman Old Style", 10, "bold"), bg = "white")
        l9.grid(row = 8, column = 0, padx = 40)
        entry4 = ttk.Entry(lframe, textvariable = self.var_gender, font = ("Bookman Old Style", 10, "bold"), width = 22)
        entry4.grid(row = 8, column = 1, padx = 20, pady = 4, sticky = W)

        l10 = Label(lframe, text = "phone", font = ("Bookman Old Style", 10, "bold"), bg = "white")
        l10.grid(row = 9, column = 0, padx = 40)
        entry5 = ttk.Entry(lframe, textvariable = self.var_phone, font = ("Bookman Old Style", 10, "bold"), width = 22)
        entry5.grid(row = 9, column = 1, padx = 20, pady = 4, sticky = W)

        l11 = Label(lframe, text = "Email", font = ("Bookman Old Style", 10, "bold"), bg = "white")
        l11.grid(row = 10, column = 0, padx = 40)
        entry6 = ttk.Entry(lframe, textvariable = self.var_email, font = ("Bookman Old Style", 10, "bold"), width = 22)
        entry6.grid(row = 10, column = 1, padx = 20, pady = 4, sticky = W)

        l12 = Label(lframe, text = "DOB", font = ("Bookman Old Style", 10, "bold"), bg = "white")
        l12.grid(row = 11, column = 0, padx = 40)
        entry7 = ttk.Entry(lframe, textvariable = self.var_dob, font = ("Bookman Old Style", 10, "bold"), width = 22)
        entry7.grid(row = 11, column = 1, padx = 20, pady = 4, sticky = W)

        l13 = Label(lframe, text = "Teacher", font = ("Bookman Old Style", 10, "bold"), bg = "white")
        l13.grid(row = 12, column = 0, padx = 40)
        entry8 = ttk.Entry(lframe, textvariable = self.var_teacher, font = ("Bookman Old Style", 10, "bold"), width = 22)
        entry8.grid(row = 12, column = 1, padx = 20, pady = 4, sticky = W)

        l14 = Label(lframe, text = "Address", font = ("Bookman Old Style", 10, "bold"), bg = "white")
        l14.grid(row = 13, column = 0, padx = 40)
        entry9 = ttk.Entry(lframe, textvariable = self.var_address, font = ("Bookman Old Style", 10, "bold"), width = 22)
        entry9.grid(row = 13, column = 1, padx = 20, pady = 4, sticky = W)

        self.var_radio1 = StringVar()
        radiobut1 = ttk.Radiobutton(lframe, variable = self.var_radio1, text = "Sample", value = "Yes")
        radiobut1.grid(row = 14, column = 0, padx = 40, pady = 4, sticky = W)
        radiobut2 = ttk.Radiobutton(lframe, variable = self.var_radio1, text = "No Sample", value = "No")
        radiobut2.grid(row = 14, column = 1, padx = 40, pady = 4, sticky = W)

        bu1 = Button(lframe, text = "SAVE", command = self.storing_data, font = ("Bookman Old Style", 10, "bold"), width = 20, bg = "purple")
        bu1.grid(row = 15, column = 0, padx = 30, pady = 3)

        bu2 = Button(lframe, text = "Delete", command = self.do_delete, font = ("Bookman Old Style", 10, "bold"), width = 20, bg = "purple")
        bu2.grid(row = 15, column = 1, padx = 30, pady = 3)

        bu3 = Button(lframe, text = "Update", command = self.update1, font = ("Bookman Old Style", 10, "bold"), width = 20, bg = "purple")
        bu3.grid(row = 16, column = 0, padx = 30, pady = 3)

        bu4 = Button(lframe, text = "Reset", command = self.reset, font = ("Bookman Old Style", 10, "bold"), width = 20, bg = "purple")
        bu4.grid(row = 16, column = 1, padx = 30, pady = 3)

        bu5 = Button(lframe, text = "Capture Image", command = self.take_photo, font = ("Bookman Old Style", 10, "bold"), width = 20, bg = "purple")
        bu5.grid(row = 17, column = 0, padx = 30, pady = 3)

        bu6 = Button(lframe, text = "Update Image", font = ("Bookman Old Style", 10, "bold"), width = 20, bg = "purple")
        bu6.grid(row = 17, column = 1, padx = 30, pady = 3)




        rframe = LabelFrame(label1, relief = RIDGE, text = "SEARCH DETAILS", font = ("Bookman Old Style", 16, "bold"))
        rframe.place(x = 640, y = 20, width = 600, height = 600)

      
        frame1 = Frame(rframe, bd = 2, bg = "white", relief = RIDGE)
        frame1.place(x = 20, y = 50, width = 550, height = 450)

        up_down1 = ttk.Scrollbar(frame1, orient = HORIZONTAL)
        up_down2 = ttk.Scrollbar(frame1, orient = VERTICAL)
        self.student1 = ttk.Treeview(frame1, columns = ("Department", "Course", "year", "semester", "ID", "Name", "section", "roll_num", "gender", "phone", "Email", "DOB", "Teacher", "Address", "image"), xscrollcommand = up_down1.set, yscrollcommand = up_down2.set)
        up_down1.pack(side = BOTTOM, fill = X)
        up_down2.pack(side = RIGHT, fill = Y)

        up_down1.config(command = self.student1.xview)
        up_down2.config(command = self.student1.yview)

        self.student1.heading("Department", text = "Department")
        self.student1.heading("Course", text = "Course")
        self.student1.heading("year", text = "year")
        self.student1.heading("semester", text = "semester")
        self.student1.heading("ID", text = "ID")
        self.student1.heading("Name", text = "Name")
        self.student1.heading("section", text = "section")
        self.student1.heading("roll_num", text = "roll_num")
        self.student1.heading("gender", text = "gender")
        self.student1.heading("phone", text = "phone")
        self.student1.heading("Email", text = "Email")
        self.student1.heading("DOB", text = "DOB")
        self.student1.heading("Teacher", text = "Teacher")
        self.student1.heading("Address", text = "Address")
        self.student1.heading("image", text = "image")

        self.student1["show"] = "headings"

        self.student1.column("Department", width = 70)
        self.student1.column("Course", width = 70)
        self.student1.column("year", width = 70)
        self.student1.column("semester", width = 70)
        self.student1.column("ID", width = 70)
        self.student1.column("Name", width = 70)
        self.student1.column("section", width = 70)
        self.student1.column("roll_num", width = 70)
        self.student1.column("gender", width = 70)
        self.student1.column("phone", width = 70)
        self.student1.column("Email", width = 70)
        self.student1.column("DOB", width = 70)
        self.student1.column("Teacher", width = 70)
        self.student1.column("Address", width = 70)
        self.student1.column("image", width = 70)

        self.student1.pack(fill = BOTH, expand = 1)
        self.student1.bind("<ButtonRelease>", self.update)
        self.display_data()
        

    def storing_data(self):
        if self.var_dep.get() == "Select department" or self.var_name.get() == "":
            messagebox.showerror("Error", "ALL FIELDS ARE REQUIRED", parent = self.root)
        else:
            try:
                connect1 = mysql.connector.connect(host = "localhost", username = "root", password = "SPR@nandhin1", database = "attendence_system")
                con = connect1.cursor()
                con.execute('insert into student_details values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_sem.get(),
                                                                                                                self.var_id.get(),
                                                                                                                self.var_name.get(),
                                                                                                                self.var_section.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_radio1.get(),
                                                                                                         ))
                connect1.commit()
                self.display_data()
                connect1.close()
                messagebox.showinfo("Success", "Recorded Successfully", parent = self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Due To : {str(e)}", parent = self.root)


    def display_data(self):
        connect1 = mysql.connector.connect(host = "localhost", username = "root", password = "SPR@nandhin1", database = "attendence_system")
        con = connect1.cursor()
        con.execute("select * from student_details")
        details = con.fetchall()

        if len(details) != 0:
            self.student1.delete(*self.student1.get_children())
            for i in details:
                self.student1.insert("", END, values = i)
            connect1.commit()
        connect1.close()


    def update(self, occur = ""):
        connect2 = self.student1.focus()
        detail = self.student1.item(connect2)
        content1 = detail["values"]

        self.var_dep.set(content1[0])
        self.var_course.set(content1[1])
        self.var_year.set(content1[2])
        self.var_sem.set(content1[3])
        self.var_id.set(content1[4])
        self.var_name.set(content1[5])
        self.var_section.set(content1[6])
        self.var_roll.set(content1[7])
        self.var_gender.set(content1[8])
        self.var_phone.set(content1[9])
        self.var_email.set(content1[10])
        self.var_dob.set(content1[11])
        self.var_teacher.set(content1[12])
        self.var_address.set(content1[13])
        self.var_radio1.set(content1[14])

    
    def update1(self):
        if self.var_dep.get() == "Select department" or self.var_name.get() == "":
            messagebox.showerror("Error", "ALL FIELDS ARE REQUIRED", parent = self.root)

        else:
            try:
                do_update = messagebox.askyesno("UPDATE", "DO U WANT TO UPDATE DETAILS", parent = self.root)
                if do_update > 0:
                    connect1 = mysql.connector.connect(host = "localhost", username = "root", password = "SPR@nandhin1", database = "attendence_system")
                    con = connect1.cursor()
                    con.execute('update student_details set Department = %s, Course = %s, year = %s, semester = %s, Name = %s, section = %s, roll_num = %s, gender = %s, phone = %s, Email = %s, DOB = %s, Teacher = %s, Address = %s, image = %s where ID = %s', (
                                                                                                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                                                                                                    self.var_sem.get(),
                                                                                                                                                                                                                                                                    self.var_name.get(),
                                                                                                                                                                                                                                                                    self.var_section.get(),
                                                                                                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                                                                                                    self.var_id.get(),
                                                                                                                                                                                                                                                        ))
                else:
                    if not do_update:
                        return
                messagebox.showinfo("SUCCESS", "UPDATED SUCCESSFULLY", parent = self.root)
                connect1.commit()
                self.display_data()
                connect1.close()
            except Exception as e:
                messagebox.showerror("ERROR", f"DUE TO : {str(e)}", parent = self.root)


    def do_delete(self):
        if self.var_id.get() == "":
            messagebox.showerror("ERROR", "ID should be given", parent = self.root)
        else:
            try:
                del1 = messagebox.askyesno("DELETE", "DO U WANT TO DELETE DETAILS", parent = self.root)
                if del1 > 0:
                    connect1 = mysql.connector.connect(host = "localhost", username = "root", password = "SPR@nandhin1", database = "attendence_system")
                    con = connect1.cursor()
                    con.execute("DELETE FROM student_details WHERE ID = %s", (self.var_id.get(),))
                else:
                    if not del1:
                        return
                connect1.commit()
                self.display_data()
                connect1.close()
                messagebox.showinfo("DELETE", "deleted sucessfilly", parent = self.root)
            except Exception as e:
                messagebox.showerror("ERROR", f"DUE TO : {str(e)}", parent = self.root)


    def reset(self):
        self.var_dep.set("Select department")
        self.var_course.set("Select course")
        self.var_year.set("Select year")
        self.var_sem.set("Select semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_section.set("")
        self.var_roll.set("")
        self.var_gender.set("")
        self.var_phone.set("")
        self.var_email.set("")
        self.var_dob.set("")
        self.var_teacher.set("")
        self.var_address.set("")
        self.var_radio1.set("")

    
    def take_photo(self):
        if self.var_dep.get() == "Select department" or self.var_name.get() == "":
            messagebox.showerror("Error", "ALL FIELDS ARE REQUIRED", parent = self.root)

        else:
            try:
                connect1 = mysql.connector.connect(host = "localhost", username = "root", password = "SPR@nandhin1", database = "attendence_system")
                con = connect1.cursor()
                con.execute("select * from student_details")
                result1 = con.fetchall()
                fid = 0
                for i in result1:
                    fid += 1
                con.execute('update student_details set Department = %s, Course = %s, year = %s, semester = %s, Name = %s, section = %s, roll_num = %s, gender = %s, phone = %s, Email = %s, DOB = %s, Teacher = %s, Address = %s, image = %s where ID = %s;', (
                                                                                                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                                                                                                    self.var_sem.get(),
                                                                                                                                                                                                                                                                    self.var_name.get(),
                                                                                                                                                                                                                                                                    self.var_section.get(),
                                                                                                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                                                                                                    self.var_id.get() == fid + 1,
                                                                                                                                                                                                                                                        ))
                connect1.commit()
                self.display_data()
                self.reset()
                connect1.close()
                image_det = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def imagef(img):
                    colour = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    im = image_det.detectMultiScale(colour, 1.3, 5)   
                    for (x, y, w, h) in im:
                        imagef = img[y : y + h, x : x + w]     
                        return imagef

                cam = cv2.VideoCapture(0)
                image_count =  0
                while True:
                    re, mframe = cam.read()
                    if imagef(mframe) is not None:
                        image_count += 1
                        z = cv2.resize(imagef(mframe), (300, 300))                                                                                                                                                                                                                          
                        z = cv2.cvtColor(z, cv2.COLOR_BGR2GRAY)
                        fname = "data1/person." + str(fid) + "." +str(image_count) + ".jpg"
                        cv2.imwrite(fname, z)
                        cv2.putText(z, str(image_count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("IMAGE", z)
                    if cv2.waitKey(1) == 13 or int(image_count) == 100:
                        break
                cam.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("OUTPUT", "dataset created")
            except Exception as e:
                messagebox.showerror("ERROR", f"DUE TO : {str(e)}", parent = self.root)





if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()