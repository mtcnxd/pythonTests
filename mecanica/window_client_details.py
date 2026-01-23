from tkinter import *
import api_client

class Window(Frame):
    def __init__(self, master=None, client_id=None):
        super().__init__(master)
        self.master = master
        self.client_id = client_id
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        try:
            client_info = self.show_client_details(self.client_id)
            print(client_info)

        except Exception as e:
            print(f"Error: {e}")

        Label(self, text="Client name: ").pack(side=LEFT)
        name_var = StringVar()
        name_var.set(client_info['name'])
        Entry(self, textvariable=name_var).pack(side=RIGHT)

        Label(self, text="Client phone: ").pack(side=LEFT)
        phone_var = StringVar()
        phone_var.set(client_info['phone'])
        Entry(self, textvariable=phone_var).pack(side=RIGHT)

        Label(self, text="Client email: ").pack(side=LEFT)
        email_var = StringVar()
        email_var.set(client_info['email'])
        Entry(self, textvariable=email_var).pack(side=RIGHT)

    def show_client_details(self, client_id):
        try:
            json_response = api_client.HttpClient().get_client_info(client_id)
            return json_response['data']
        except Exception as e:
            print(f"Error: {e}")
            