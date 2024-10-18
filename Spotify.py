import requests
import json

url = "https://api.spotify.com/v1/me/player/currently-playing"

payload={}
headers = {
  'Authorization': 'Bearer BQD2nZfSGQ54hQTdPTcxo8izsaFHC3vFdbcQlxYlzScpLWIID7khQQ9NCgqKkxrMDoZqi5x0w4hL_TFpFRJnTH6bV7BLySJzZQxpSs-9MkXowTv4n7HIZswy7qcRE2_d9FJhgeYP2rwXjtvPgeWGLBC4lyoZ3eyyXEVrotA3CpM'
}

response = requests.request("GET", url, headers=headers, data=payload)

#print(response.text)

y = json.loads(response.text)


print("Track: ", y["item"]["name"])
print("Album: ", y["item"]["album"]["name"])
print("Artist: ", y["item"]["artists"][0]["name"])