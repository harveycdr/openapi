from openai import OpenAI
from openai import OpenAI
f = open("dallekey.txt", mode="r")
key = f.read().split()
secretkey = key[0]
orgkey = key[1]
print(secretkey, orgkey)

client = OpenAI(api_key=secretkey)

response  = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Nói về khủng long đi"}],
    response_format={"type": "text"}
)

print(response.choices[0].message.content)


