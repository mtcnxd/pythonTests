from tkinter import *
import requests
import json
import api_client

class Window(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.listbox = None
        self.clients = []
        self.create_widgets()
        self.show_listbox()

    def create_widgets(self):
        clients_list_button = Button(self)
        clients_list_button["text"] = "Get Clients"
        clients_list_button["command"] = self.show_listbox
        clients_list_button.pack(side="top")

    def show_listbox(self):
        json_response = api_client.HttpClient().get_clients()
        self.clients = json_response['data']


        scrollbar = Scrollbar(self.master)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.listbox = Listbox(self.master, height=20, width=100, yscrollcommand=scrollbar.set)

        for client in json_response['data']:
            self.listbox.insert(END, client['name'])

        self.listbox.pack()
        self.listbox.bind("<<ListboxSelect>>", self.on_select)

    def on_select(self, event):
        selected_index = self.listbox.curselection()

        if selected_index:
            index = selected_index[0]
            selected_client = self.clients[index]
            
            print(f"ID: {selected_client['id']} Name: {selected_client['name']}")

            json_response = api_client.HttpClient().get_client_info(str(selected_client['id']))
            print(json_response['data'])


# Main code starts here

container = Tk()
container.title("Clients")
container.geometry("400x400")

Window(container)

container.mainloop()
