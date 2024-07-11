from io import BytesIO
from PIL import Image
from openai import OpenAI
import requests

def download_image(url, file_path):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(file_path, 'wb') as file:
                file.write(response.content)
                
            print(f"Ảnh là: '{file_path}'")
        else:
            print("Không thể tải xuống ảnh. Mã trạng thái:", response.status_code)
    except requests.RequestException as e:
        print("Lỗi khi thực hiện yêu cầu:", e)

f = open("dallekey.txt", mode="r")
key = f.read().split()
secretkey = key[0]
orgkey = key[1]
print(secretkey, orgkey)

client = OpenAI(
    api_key=secretkey,
    organization=orgkey
)

prompt = input("Nhập mô tả hình ảnh: ")

print("Đang sử lý")

response = client.images.generate(
  model = "dall-e-3",
  prompt = prompt,
  size = "1792x1024",
  quality = "standard",
  n=1,
)
print(response)
image_url = response.data[0].url
path = input("Nhập tên ảnh: ")
download_image(image_url, path + ".png")