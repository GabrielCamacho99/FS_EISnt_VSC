import csv

with open("dados.csv", newline="") as f:
    leitor = csv.reader(f)
    for linha in leitor:
        if int(linha[1]) > 30:
            print(linha[0])


