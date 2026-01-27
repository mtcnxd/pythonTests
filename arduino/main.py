from tkinter import *
from serial import Serial

class MainWindow(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)
		self.array_data = ""
		self.temp_value = StringVar()

		try:
			self.arduino = Serial(port="/dev/ttyUSB0", baudrate=9600, timeout=5)
			self.func_get_temp()

		except:
			print("Error al abrir el puerto")
			return None

		self.createWidgets()

	def __del__(self):
		self.arduino.close()


	def createWidgets(self):
		Label(text="Temperatura:").grid(row=0, column=0, sticky="w", padx=20, pady=10)

		self.entryTemperature = Entry(font=("Arial", 40, "bold"), borderwidth=1, width=13, textvariable=self.temp_value).grid(row=1, column=0, padx=20, pady=10)
	
		Button(text="Save", command=self.func_store_data, padx=40, pady=10).grid(row=2, column=0, sticky="w", padx=20, pady=10)

	def func_get_temp(self):
		if self.arduino.in_waiting > 0:
			bytes_received = self.arduino.readline()
			decoded_data = bytes_received.decode().rstrip('\r\n')
			self.array_data = decoded_data.split(',')

			self.temp_value.set(f"Read value: {self.array_data[0]}")

		self.after(1000, self.func_get_temp)

	def func_store_data(self):
		print(f"Data: {self.array_data[0]} | Stored successfully")


if __name__ == "__main__":
	frame = Tk()
	frame.title("Arduino Serial")
	frame.geometry('430x200')
	frame.resizable(False, False)

	MainWindow(frame)
	frame.mainloop()
