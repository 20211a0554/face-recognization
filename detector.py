from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime

class Detector1:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendence system")

        image = Image.open(r"C:\Users\nandhini chityala\OneDrive\Pictures\Camera Roll\image7.webp")
        image = image.resize((1430, 700),Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(image)
        label1 = Label(self.root, image = self.photoimage)
        label1.pack()

        title_label = Label(label1, text = "Face Recognition", font = ("Bookman Old Style", 30, "bold"), fg = "black")
        title_label.place(x = 250, y = 0,width = 800, height = 100)

        bu1 = Button(label1, text = "RECOGNISER", command = self.fdetector, font = ("Bookman Old Style", 20, "bold"), width = 70, bg = "light blue")
        bu1.place(x = 250, y = 300, width = 800, height = 100)

    def attendence(self, a, b, g, h, i):
        with open("file.csv", "r+", newline = "\n") as f:
            myd = f.readlines()
            list1 = []
            for i in myd:
                ent = i.split((","))
                list1.append(ent[0])
            if((a not in list1) and (b not in list1) and (g not in list1) and (h not in list1) and (i not in list1)):
                n1 = datetime.now()
                d1 = n1.strftime("%d/%m/%Y")
                d2 = n1.strftime("%H:%M:%S")
                f.writelines(f"\n{a}, {b}, {g}, {h}, {i},{d2}, {d1}, present")

    def fdetector(self):
        def Bound(img, classifier, scaleFactor, minNeighbors, color, text, cla):
            gimage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            feat = classifier.detectMultiScale(gimage, scaleFactor, minNeighbors)
            coor = []
            for (x, y, w, h) in feat:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                i1, predict = cla.predict(gimage[y : y + h, x : x + w])
                co = int((100 * (1 - predict/300)))

                connect1 = mysql.connector.connect(host = "localhost", username = "root", password = "SPR@nandhin1", database = "attendence_system")
                con = connect1.cursor()
                con.execute("select Name from student_details where ID = " +str(i1))
                a = con.fetchone()
                a = "+".join(a)

                con.execute("select Department from student_details where ID = " +str(i1))
                b = con.fetchone()
                b = "+".join(b)

                con.execute("select roll_num from student_details where ID = " +str(i1))
                g = con.fetchone()
                g = "+".join(g)

                con.execute("select ID from student_details where ID = " +str(i1))
                h = con.fetchone()
                h = "+".join(h)

                con.execute("select Teacher from student_details where ID = " +str(i1))
                i = con.fetchone()
                i = "+".join(i)

                if co > 80:
                    cv2.putText(img, f"Name:{a}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255255), 2)
                    cv2.putText(img, f"Department:{b}", (x, y - 60), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255255), 2)
                    cv2.putText(img, f"roll_num:{g}", (x, y - 40), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255255), 2)
                    cv2.putText(img, f"id:{h}", (x, y - 20), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255255), 2)
                    cv2.putText(img, f"Teacher:{i}", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255255), 2)
                    self.attendence(a, b, g, h, i)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    cv2.putText(img, "not detected", (x, y - 50), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255255), 2)
                coor = [x, y, w, y]
            return coor

        def recog(img, cla, faceCascade):
            coor = Bound(img, faceCascade, 1.1, 10, (255, 25, 255), "image", cla)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        cla = cv2.face.LBPHFaceRecognizer_create()
        cla.read("classifier.xml")
        vid = cv2.VideoCapture(0)

        while True:
            r, img = vid.read()
            img = recog(img, cla, faceCascade)
            cv2.imshow("WELCOME", img)
            
            if cv2.waitKey(1) == 13:
                break
        vid.release()
        cv2.destroyAllWindows()




if __name__ == "__main__":
    root = Tk()
    obj = Detector1(root)
    root.mainloop()