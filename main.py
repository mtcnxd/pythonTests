import os
import time
from openai import OpenAI

timer = 0

client = OpenAI(
	api_key = "sk-proj-JxWaI0TKsmPdygN4iW2yT3BlbkFJ3zCENhJvCYyQVq80Ddya"
)

def blink(timer):
	if (timer > 10):
		try:
			input_text = "Hola, como te encuentras el dia de hoy?"
			chat_completion = client.chat.completions.create(
				messages=[
					{
						"role": "user",
						"content": input_text,
					}
				],
				model="gpt-3.5-turbo",
			)
		except(error):
			print (error)

		return True


while (True):
	print ("Counter: ", timer)
	time.sleep(0.5)
	timer = timer +1
	if (blink(timer)):
		timer = 0
