""" muda ficheiro de sitio """

import os
import shutil

def organizarArquivos():
    # Diretório de origem (pasta onde os arquivos estão atualmente)
    diretorioOrigem = 'teste2'

    # Diretório de destino (pasta para onde os arquivos serão movidos)
    diretorioDestino = 'teste1'

    # Lista todos os arquivos no diretório de origem
    arquivos = os.listdir(diretorioOrigem)

    # Itera sobre os arquivos e move os arquivos .txt para o diretório de destino
    for arquivo in arquivos:
        if arquivo.endswith('.txt'):
            # Caminho completo do arquivo de origem
            origem = os.path.join(diretorioOrigem, arquivo)

            # Caminho completo do arquivo de destino
            destino = os.path.join(diretorioDestino, arquivo)

            # Move o arquivo para o diretório de destino
            shutil.move(origem, destino)

            print(f'Arquivo {arquivo} movido para {diretorioDestino}')

# Chama a função para organizar os arquivos
organizarArquivos()