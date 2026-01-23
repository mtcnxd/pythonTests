import pymysql.cursors
import tkinter.messagebox
from tkinter import *
from DataBase import *
from QueryManager import QueryManager

class MainFrame(Frame):
    def __init__(self, container):
        super().__init__(container)
        # Initialize the container
        self.master = container
        self.master.title("MySQL Client")
        self.master.geometry("550x400")

        # Initialize the database connection
        # self.dataBase = DataBase()
        self.carId = StringVar()
        self.create_widgets()

    def create_widgets(self):
        Label(text="ID:").grid(row=0, column=0, padx=10, pady=10)
        Entry(textvariable=self.carId, width=30).grid(row=0, column=1, pady=10)
        Button(text="Search", command=QueryManager.searchClient).grid(row=1, column=1, sticky=W)

        Label(text="Brand:").grid(row=2, column=0, padx=10)
        Entry(width=30).grid(row=2, column=1, padx=10)

        Label(text="Model:").grid(row=3, column=0, padx=10)
        Entry(width=30).grid(row=3, column=1, padx=10)

        Button(text="Save", command=QueryManager.insertClient).grid(row=4, column=1, sticky=W)

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


if __name__ == "__main__":
    container = Tk()
    MainFrame(container)
    container.mainloop()