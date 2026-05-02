import requests
from bs4 import BeautifulSoup
import csv

# Fazer requisição à página
url = "https://www.lusa.pt/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extrair os títulos das notícias
titulos = soup.find_all("a")
print(len(titulos))
for titulo in titulos:
    print(titulo.text) #imprime o texto do titulo
    
with open ('noticias.csv', 'a', newline='') as file:
    writer= csv.writer(file)
    writer.writerow(['Titulo'])
    for titulo in titulos:
        writer.writerow    