import requests

url = "http://api.openweathermap.org/data/2.5/weather?q=merida&appid=192dbed2ac66d17d5f75780635e474fa"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

