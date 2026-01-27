from tkinter import *
from serial import Serial

class Pycalc(Frame):
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

		
		self.entryTemperature = Entry(font=("Arial", 40), borderwidth=1, textvariable=self.temp_value, width=10).place(x=10, y=30)
		self.createWidgets()

	def __del__(self):
		self.arduino.close()


	def createWidgets(self):
		Label(text="Temperatura:").place(x=10, y=10)

	def func_get_temp(self):
		if self.arduino.in_waiting > 0:
			bytes_received = self.arduino.readline()
			decoded_data = bytes_received.decode().rstrip('\r\n')
			self.array_data = decoded_data.split(',')

			self.temp_value.set(self.array_data[0])
			print(self.temp_value.get())

		self.after(1000, self.func_get_temp)


Termometer = Tk()
Termometer.title("Sensor BMP180")
Termometer.geometry('350x250')

root = Pycalc(Termometer)
Termometer.mainloop()
