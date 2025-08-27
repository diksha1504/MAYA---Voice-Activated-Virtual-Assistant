from openai import OpenAI
client = OpenAI(
    api_key="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",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "compose a poem that explains the concepts of recursion and iteration in programming"}
  ]
)

print(completion.choices[0].message.content)