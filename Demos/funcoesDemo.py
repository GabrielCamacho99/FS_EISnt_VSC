import json
import os
import csv



# Funções para mostrar e devolver a opção escolhida
def menu():
    print("\nMenu:")
    print("1- Registar o utilizador")
    print("2- Listar utilizadores")
    print("3- Exportar Relatorio utilizadores")
    print("4- Exportar Relatorio utilizadores em CSV")
    print("0- Sair")
    return input("Escolha uma opção:")

# Função para registar um novo utilizador e devolver o dicionário criado
def registar_utilizador():
    print("\n--- Registo de Utilizador ---")
    nome = input("Nome: ")
    try:
        idade = int(input("Idade: "))
    except ValueError:
        print("Valor Introduzido inválido, tente novamente") 
        idade = int(input("Idade: "))   
    email = input("Email: ")
    
    return {
        "nome": nome,
        "idade": idade,
        "email": email
    }

# Função para listar todos os utilizadores registados
def listar_utilizadores(lista):
    if not lista:
        print("Nenhum utilizador registado ainda.")
        return
    
    print("\n--- Lista de Utilizadores ---")
    for i, u in enumerate(lista, start=1):
        print(f"{i}. Nome: {u['nome']}, Idade: {u['idade']}, Email: {u['email']}")

# 

def guardar(lista):
    with open("utilizadores.json", "w") as file:
        json.dump(lista, file, indent=4)
        
        
def carregar():
    if os.path.exists("utilizadores.json"):
        with open("utilizadores.json", "r") as file:
            return  json.load(file)
    return[]           


from datetime import datetime

def exportar_relatorio(lista):
    nomeFile = f"Relatorio_{datetime.now().strftime('%Y%m%d_%H%M')}.txt"
    
    with open(nomeFile, "w") as file:
        file.write("RELATORIO DE UTILIZADORES\n\n")
        
        for user in lista:
            file.write(f"{user['nome']} | {user['idade']} | {user['email']}\n")
            
    print("Relatorio Criado:", nomeFile)        
    
    
    
def exportar_relatorio_csv(lista):
    if not lista:
        print("Sem dados a exportar.")
        return
    
    nomeFile = f"Relatorio_utilizadores_CSV.csv"
    
    if os.path.exists(nomeFile):
        print("Ficheiro ja existe -> irá ser reescrito")
    
    
    with open(nomeFile, "w", newline="", encoding= "utf-8") as file:
                   
        writer = csv.writer(file)
        
        # Cabeçalho
        writer.writerow(["NOME", "IDADE", "EMAIL"])
        
        # Dados
        for user in lista:
            writer.writerow([user['nome'], user['idade'], user['email']])
            
    print("Relatorio Criado:", nomeFile)            