"""
"""
import requests 

url = "https://jsonplaceholder.typicode.com/users/"

response = requests.get(url)
dados = response.json()

""" print(dados)


print(dados["name"])
print(dados["email"])

rua = dados["address"]["street"]
suite = dados["address"]["suite"]
city = dados["address"]["city"]
print(f"Endereço: {rua}, {suite}, {city}") """


""" for users in dados:
    if users["address"]["city"] == "South Christy":
        print(users["name"]) """

with open("users.txt", "w") as f:
    for user in dados:
        f.write(f"{user['name']} - {user['email']}\n")