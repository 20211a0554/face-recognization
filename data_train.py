from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Data1:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendence system")

        image = Image.open(r"C:\Users\nandhini chityala\OneDrive\Pictures\Camera Roll\image7.webp")
        image = image.resize((1430, 700),Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(image)
        label1 = Label(self.root, image = self.photoimage)
        label1.pack()
        title_label = Label(label1, text = "DATA TRANING", font = ("Bookman Old Style", 30, "bold"), fg = "purple")
        title_label.place(x = 250, y = 0,width = 800, height = 100)

        bu1 = Button(label1, text = "Train data", command = self.Train1, font = ("Bookman Old Style", 20, "bold"), width = 70, bg = "light blue")
        bu1.place(x = 250, y = 300, width = 800, height = 100)

    def Train1(self):
        data = ("data1")
        path = [os.path.join(data, file) for file in os.listdir(data)]

        image = []
        fid = []
        for i in path:
            image1 = Image.open(i).convert('L')
            imnp = np.array(image1, 'uint8')
            id = int(os.path.split(i)[1].split('.')[1])

            image.append(imnp)
            fid.append(id)
            cv2.imshow("TRAINING DATA", imnp)
            cv2.waitKey(1) == 13
        fid = np.array(fid)

        cla = cv2.face.LBPHFaceRecognizer_create()
        cla.train(image, fid)
        cla.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("OUTPUT", "Traning data completed")



if __name__ == "__main__":
    root = Tk()
    obj = Data1(root)
    root.mainloop()