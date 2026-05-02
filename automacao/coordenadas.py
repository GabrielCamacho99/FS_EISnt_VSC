import pyautogui
import time

print("Posicione o cursor do mouse sobre o local a sacar as coordenadas...")

time.sleep(5)  # Dê alguns segundos para posicionar o cursor

# Obter e imprimir as coordenadas atuais do mouse
current_mouse_position = pyautogui.position()

print("Coordenadas da barra de pesquisa:", current_mouse_position)