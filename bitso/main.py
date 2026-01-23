import json
import requests

def lambda_handler():
	return {
		'statusCode': 200,
		'body': getBitcoinPrice()
	}

def getBitcoinPrice():
	url = "https://api-stage.bitso.com/api/v3/ticker"
	response = requests.get(url)
	results = parsePrice(response.text)

	for key, value in results.items():
		print(f"{key} \t {value}")
		print("-------------------------------------")

def parsePrice(ticker):
	result = {}
	try:
		object = json.loads(str(ticker))
		for crypto in (object['payload']):
			result[crypto['book']] = crypto['last']

		return result

	except Exception as error:
		print(error)

	
	
lambda_handler()
