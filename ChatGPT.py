import openai # type: ignore

client = openai.OpenAI()

try:
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
                {
                    "role": "system", "content": "You are a helpful assistant."
                },{
                    "role": "user",
                    "content": "Write a haiku about recursion in programming."
                }
            ]
    )

    print(completion.choices[0].message)

except openai.OpenAIError as err:
    print(f"Exception: {err}")