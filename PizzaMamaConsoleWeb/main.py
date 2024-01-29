import requests
import json


url = "https://deddy.pythonanywhere.com/api/GetPizza"

data = requests.get(url)

#print(data.text)
pizzas = json.loads(data.text)

for pizzaModel in pizzas:
    pizza = pizzaModel['fields']
    print(pizza['name'] + ": " + str(pizza['price']) + "$")