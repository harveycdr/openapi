from openai import OpenAI
from PIL import Image
from io import BytesIO
from downloadImg import download_image

f = open("dallekey.txt", mode="r")
key = f.read().split()
secretkey = key[0]
orgkey = key[1]
print(secretkey, orgkey)
client = OpenAI(
    api_key=secretkey,
    organization=orgkey
)

img_path = "lambeauty6.png"

response = client.images.edit(
  model="dall-e-2",
  image=open("lambeauty6.png", "rb"),
  mask=open("mask.png", "rb"),
  prompt="replace cahr 'S O M L G I A G E' thành từ 'cosmetic'",
  n=1,
  size="1024x1024"
)

image_url = response.data[0].url
download_image(image_url, 'edit_'+img_path)