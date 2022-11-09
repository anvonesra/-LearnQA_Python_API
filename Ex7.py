import time
import requests
import json

URL = "https://playground.learnqa.ru/ajax/api/compare_query_type"

# 1. Делает http-запрос любого типа без параметра method, описать что будет выводиться в этом случае.

response = requests.get(URL)
print(response.text)

# 2. Делает http-запрос не из списка. Например, HEAD. Описать что будет выводиться в этом случае.

response = requests.head(URL)
print(response.content)
print(response.text)
print(response)

# 3. Делает запрос с правильным значением method. Описать что будет выводиться в этом случае.

response = requests.get(URL, params={"method": "GET"})
print(response)
print(response.text)

# 4. С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method. Например с GET-запросом передает значения параметра method равное ‘GET’, затем ‘POST’, ‘PUT’, ‘DELETE’ и так далее. И так для всех типов запроса. Найти такое сочетание, когда реальный тип запроса не совпадает со значением параметра, но сервер отвечает так, словно все ок. Или же наоборот, когда типы совпадают, но сервер считает, что это не так.

URL = "https://playground.learnqa.ru/ajax/api/compare_query_type"
parameters_methods_list = [{"method": "GET"}, {"method": "POST"}, {"method": "PUT"}, {"method": "DELETE"}]

for param in parameters_methods_list:
    get_response = requests.get(URL, params=param)
    print(f"get request with {param} returned response: {get_response.text}")
    post_response = requests.post(URL, data=param)
    print(f"post request with {param} returned response: {post_response.text}")
    put_response = requests.put(URL, data=param)
    print(f"put request with {param} returned response: {put_response.text}")
    delete_response = requests.delete(URL, data=param)
    print(f"delete request with {param} returned response: {delete_response.text}")
