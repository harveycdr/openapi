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

