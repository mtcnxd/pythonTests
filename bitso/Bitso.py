import requests
import json

class Bitso:
    def __init__(self):
        self.url = "https://api-stage.bitso.com/api/v3/ticker"

    def get_ticker(self):
        try:
            url = "https://api-stage.bitso.com/api/v3/ticker"
            response = requests.get(url)
            return response.json()

        except Exception as e:
            print(f"Error: {e}")
            return None

    def get_formated_ticker(self):
        response = self.get_ticker()

        values = []
        for books in response['payload']:
            values.append(books)
        
        return values

    def get_book_info(self, book):
        response = self.get_ticker()

        for books in response['payload']:
            if books['book'] == book:
                return books
