from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter
from tkinter import messagebox
from Student1 import Student
from data_train import Data1
from detector import Detector1
from attendance import Attendence1
import os


class attendence:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendence system")

        image = Image.open(r"C:\Users\nandhini chityala\OneDrive\Pictures\Camera Roll\image6.jpg")
        image = image.resize((1530, 790),Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(image)
        label1 = Label(self.root, image = self.photoimage)
        label1.pack()

        title_label = Label(label1, text = "Attendance Management System Using Face Recognition", font = ("Bookman Old Style", 30, "bold"), fg = "black")
        title_label.place(x = 0, y = 0)

        b1 = Button(label1, text = "STUDENTS DETAILS", command = self.student, fg = "black")
        b1.place(x = 300, y = 150, width = 250, height = 100)

        b2 = Button(label1, text = "ATTENDANCE", command = self.attend, fg = "black")
        b2.place(x = 300, y = 300, width = 250, height = 100)

        b3 = Button(label1, text = "DATA TRANING", command = self.traindata, fg = "black")
        b3.place(x = 300, y = 450, width = 250, height = 100)

        b4 = Button(label1, text = "FACE IDENTIFIER",command = self.facedetector, fg = "black")
        b4.place(x = 700, y = 150, width = 250, height = 100)

        b5 = Button(label1, text = "DETECTED PHOTOS",command = self.detected_photos, fg = "black")
        b5.place(x = 700, y = 300, width = 250, height = 100)

        b6 = Button(label1, text = "EXIT", command = self.mexit, fg = "black")
        b6.place(x = 700, y = 450, width = 250, height = 100)

      

    
    def detected_photos(self):
        os.startfile("data1")

    def mexit(self):
        self.mexit = messagebox.askyesno("ATTENDENC SYSTEM", "DO YOU WANT TO EXIT", parent = self.root)
        if self.mexit > 0:
            self.root.destroy()
        else:
            return

    def student(self):
        self.new_page = Toplevel(self.root)
        self.app = Student(self.new_page)

    def traindata(self):
        self.new_page = Toplevel(self.root)
        self.app = Data1(self.new_page)

    def facedetector(self):
        self.new_page = Toplevel(self.root)
        self.app = Detector1(self.new_page)

    def attend(self):
        self.new_page = Toplevel(self.root)
        self.app = Attendence1(self.new_page)

        

if __name__ == "__main__":
    root = Tk()
    obj = attendence(root)
    root.mainloop()