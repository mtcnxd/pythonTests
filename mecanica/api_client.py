import requests
import json

class HttpClient:
    def __init__(self):
        self.url = "https://mecanicarubio.com/api"

    def get_clients(self):
        response = requests.get(self.url +"/clients/all")
        return response.json()

    def get_client_info(self, client_id):
        response = requests.get(self.url + "/clients/info/" + str(client_id))
        return response.json()

    def get_services(self, client_id):
        response = requests.get(self.url + "/clients/services/" + str(client_id))
        return response.json()