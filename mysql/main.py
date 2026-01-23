import pymysql.cursors # type: ignore
import tkinter.messagebox
from tkinter import *

class Window(Frame):
    def __init__(self, master):
        self.connection = pymysql.connect(
            host="127.0.0.1",
            user="marcos",
            password="Tucm+1985",
            db="mecanica_rubio"
        )
        self.carId = StringVar()
        self.loadInterface()

    def loadInterface(self):
        LblId = Entry(textvariable=self.carId)
        LblId.place(x=10, y=10)

        btnLoad = Button(text="Search", command=self.executeQuery)
        btnLoad.place(x=10, y=40)

        self.LblBrand = Entry()
        self.LblBrand.place(x=10, y=90)

        self.LblModel = Entry()
        self.LblModel.place(x=10, y=120)

        btnInsert = Button(text="Save", command=self.insertData)
        btnInsert.place(x=10, y=150)

    def executeQuery(self):
        id = self.carId.get()
        
        if id == '':
            tkinter.messagebox.showerror(title="Input error", message="You must type some carID")
            return

        try:
            cursor = self.connection.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT * FROM autos WHERE id = %s", id)
            records = cursor.fetchall()

            for row in records:
                print(row)
                self.LblBrand.delete(0, END)
                self.LblBrand.insert(0, row['brand'])

                self.LblModel.delete(0, END)
                self.LblModel.insert(0, row['model'])

            self.connection.commit()

        except Exception as e:
            print (f"Execute error: {e}")

    def insertData(self):
        query = "INSERT INTO models (brand, model) VALUES (%s, %s)"
        values = ('marcos', 'tzuc')
        
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, values)
            self.connection.commit()
            tkinter.messagebox.showinfo(title="Insert successfully", message="Your data has been insert successfully")
        
        except:
            tkinter.messagebox.showerror(title="insert error", message="There is some error")

main = Tk()
main.title("MySQL")
main.geometry("400x400")

Window(main)

main.mainloop()