from fastapi import FastAPI
import requests
from my_secrets import WB_API_TOKEN

app = FastAPI()

def update_wb_images(vendor_code: str, image_url: str):
    """Самая простая функция для обновления картинки"""
    url = "https://suppliers-api.wildberries.ru/content/v1/media/save"
    
    headers = {
        "Authorization": WB_API_TOKEN,
        "Content-Type": "application/json"
    }
    
    data = {
        "vendorCode": vendor_code,
        "data": [image_url]  # передаем одну картинку
    }
    
    response = requests.post(url, json=data, headers=headers)
    return response.json()

@app.post("/update-image/")
def update_image(vendor_code: str, image_url: str):
    """Простая ручка для обновления картинки"""
    result = update_wb_images(vendor_code, image_url)
    return {"status": "ok", "result": result}

@app.get("/")
def root():
    return {"message": "WB API работает! Используй /update-image/"}