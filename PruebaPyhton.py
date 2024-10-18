import requests
import json
import time
import board
import busio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont

i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3c)
image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)

def getTrackInfo():
	payload={}
	url = "https://api.spotify.com/v1/me/player/currently-playing"
	headers = {
  	'Authorization': 'Bearer BQBQdNpv8GAG-RPzO2yDNUd9Uf6vuLfqFre6DmQziu-9o0HhLQGPktPeNiW1ddazf7N687_d3boGkxxeIeoWXGfPilRTGYlRtTT4vXlX9brp0nw9lYssA9JDJcyMHntu46E75passTCnvVH8nQ0xYXS_0B3uxHbSaIU8ushitY8'
	}

	response = requests.request("GET", url, headers=headers, data=payload)
	trackInfo = json.loads(response.text)
	return trackInfo


def setScreenData(trackInfo):
	track_name = trackInfo["item"]["name"]
	track_album = trackInfo["item"]["album"]["name"]
	track_artist = trackInfo["item"]["artists"][0]["name"]
	track_time = str(trackInfo["progress_ms"])

	font = ImageFont.load_default()
	#font = ImageFont.truetype('Sans.ttf', 8)

	draw.text((0, 0), track_name, font=font, fill=100,)
	draw.text((0, 15), track_artist, font=font, fill=100,)
	draw.text((0, 30), track_album, font=font, fill=100,)
	draw.text((0, 45), track_time, font=font, fill=100,)
	
	oled.fill(0)
	oled.image(image)
	oled.show()	
	
	print("Track: ", track_name)
	print("Album: ", track_album)
	print("Artist: ", track_artist)


while True:
	trackInfo = getTrackInfo()
	setScreenData(trackInfo)

	time.sleep(5)



#oled.pixel(120, 41, 1)
#oled.invert(True)
