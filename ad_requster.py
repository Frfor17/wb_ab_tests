import requests

user_id = 123456789  # случайная хуйня
block_id = 12345     # случайная хуйня

url = f"https://api.adsgram.ai/advbot?tgid={user_id}&blockid={block_id}"
response = requests.get(url)

print("Status:", response.status_code)
print("Ответ:", response.text)