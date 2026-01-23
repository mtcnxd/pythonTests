from tkinter import *
from tkinter import messagebox
import api_client
import window_client_details

class Window(Frame):
    def __init__(self, container=None):
        super().__init__(container)
        self.master = container
        self.clients = []
        self.listbox = Listbox(self.master, width=40)
        self.id_string_var = StringVar()
        self.name_string_var = StringVar()
        self.phone_string_var = StringVar()
        self.email_string_var = StringVar()
        self.create_widgets()

    def create_widgets(self):
        try:
            json_response = api_client.HttpClient().get_clients()
            self.clients = json_response['data']
        
        except Exception as e:
            print(f"Error: {e}")

        Label(self.master, text="Clients").grid(row=0, column=0, sticky="n", padx=10, pady=10)

        for client in json_response['data']:
            self.listbox.insert(END, f"{client['id']} - {client['name']}")

        scrollbar = Scrollbar(self.master)
        scrollbar.grid(row=0, column=2, sticky="ns", pady=10)
        scrollbar.config(command=self.listbox.yview)

        self.listbox.grid(row=0, column=1, padx=10, pady=10)
        self.listbox.config(yscrollcommand=scrollbar.set)
        self.listbox.bind("<<ListboxSelect>>", self.func_on_select)

        Label(self.master, text="Client ID").grid(row=1, column=0, sticky="w", padx=10, pady=10)
        Entry(self.master, width=40, textvariable=self.id_string_var).grid(row=1, column=1, padx=10, pady=10)
        
        Button(self.master, text="Search client", command=self.func_get_details).grid(row=2, column=1, padx=10, pady=10, sticky="w")

        Label(self.master, text="Name").grid(row=3, column=0, sticky="w", padx=10, pady=10)
        Entry(self.master, width=40, textvariable=self.name_string_var).grid(row=3, column=1, padx=10, pady=10)

        Label(self.master, text="Phone").grid(row=4, column=0, sticky="w", padx=10, pady=10)
        Entry(self.master, width=40, textvariable=self.phone_string_var).grid(row=4, column=1, padx=10, pady=10)

        Label(self.master, text="Email").grid(row=5, column=0, sticky="w", padx=10, pady=10)
        Entry(self.master, width=40, textvariable=self.email_string_var).grid(row=5, column=1, padx=10, pady=10)

    def func_get_details(self):
        new_window = Toplevel()
        new_window.title("Client Details")
        new_window.geometry("400x400")
        # window_client_details.Window(new_window, client_id=self.client_id_string_var.get())

    def func_on_select(self, event):
        selected_index = self.listbox.curselection()

        if selected_index:
            index = selected_index[0]
            selected_client = self.clients[index]
            print(f"ID: {selected_client['id']} Name: {selected_client['name']}")
            self.func_get_services(selected_client)
            self.func_show_client_details(selected_client)

    def func_show_client_details(self, client_data):
        try:
            json_response = api_client.HttpClient().get_client_info(client_id=client_data['id'])
            self.name_string_var.set(json_response['data']['name'])
            self.phone_string_var.set(json_response['data']['phone'])
            self.email_string_var.set(json_response['data']['email'])
            
        except Exception as e:
            print(f"Error: {e}")

    def func_get_services(self, client_data):
        try:
            json_response = api_client.HttpClient().get_services(client_id=client_data['id'])
            count = len(json_response['data'])

            if count == 0:
                messagebox.showinfo("Services", "No services found")
                return

            for service in json_response['data']:
                print(f"ID: {service['id']} - Name: {service['car']} - Status: {service['status']}")
        
        except Exception as e:
            print(f"Error: {e}")
            messagebox.showinfo("Error", f"Error: {e}")
