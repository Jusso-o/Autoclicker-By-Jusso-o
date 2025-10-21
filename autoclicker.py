import pyautogui
import keyboard
import time

# Configurações
intervalo = 0.1  # tempo entre cliques em segundos
rodando = False  # estado inicial

print("=== AUTCLICKER PYTHON ===")
print("F8 → Iniciar/Pausar")
print("F9 → Sair")
print(f"Intervalo atual: {intervalo}s")
print("==========================")
print("Você tem 5 segundos para posicionar o mouse...")
time.sleep(5)

while True:
    # Iniciar/Pausar com F8
    if keyboard.is_pressed('f8'):
        rodando = not rodando
        print("🟢 Rodando..." if rodando else "⏸️ Pausado.")
          # evita múltiplos registros do mesmo clique

    # Encerrar com F9
    elif keyboard.is_pressed('f9'):
        print("🚪 Saindo do autoclicker...")
        break


    # Executar cliques enquanto estiver rodando
    elif rodando:
        pyautogui.click()
    time.sleep(intervalo)        
