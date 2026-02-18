import requests

class Telegram:
    def __init__(self):
        self.url = "https://api.telegram.org/bot8373335422:AAHcXOLPxVUZHMg5gQW1Zb_FZ7itqeuIm6I/sendMessage"

    def send_message(self, message):
        try:
            response = requests.post(
                self.url,
                data={'chat_id':'-5014845636', 'text':message}
            )
            
            return response.json()
        
        except Exception as e:
            print(f"Telegram message error: {e}")
            return None