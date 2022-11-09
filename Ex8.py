import requests

URL = "https://playground.learnqa.ru/ajax/api/longtime_job"

initial_resp = requests.get(URL)
token_data = initial_resp.json()
print(token_data)
seconds = token_data["seconds"]
print(seconds)

status = requests.get(URL, params=token_data)
print(status.text)

time.sleep(seconds)
final_resp = requests.get(URL, params=token_data)
print(final_resp.text)