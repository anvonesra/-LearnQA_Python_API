import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")

amount_redirect = 0
for request in response.history:
    if request.status_code == 301 or 302:
        amount_redirect += 1
print(f"Количество редиректов: {amount_redirect}")
last_url = response.url
print(f"Итоговый url: {last_url}")