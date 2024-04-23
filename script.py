import pyautogui
from PIL import Image
import datetime
import os

def get_last_folder_number(folder_name):
    folder_numbers = []
    for folder in os.listdir():
        if folder.startswith(folder_name):
            try:
                folder_numbers.append(int(folder.split('_')[-1]))
            except ValueError:
                pass
    if folder_numbers:
        return max(folder_numbers)
    else:
        return 0

def create_folder(folder_name):
    last_folder_number = get_last_folder_number(folder_name)
    next_folder_number = last_folder_number + 1
    folder_path = f"{folder_name}_{next_folder_number}"
    os.makedirs(folder_path)
    return folder_path

def take_screenshot_and_save(folder_path, label):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{label}_{timestamp}.png"
    filepath = os.path.join(folder_path, filename)
    
    screenshot = pyautogui.screenshot()
    screenshot.save(filepath)
    print("Screenshot saved to", filepath)

# Especifica la región de la pantalla que deseas capturar
width = 1920
height = 1080

input("Press Enter to start capturing screenshots...")

folder_name = "Screenshots"
folder_path = create_folder(folder_name)

for i in range(3):
    input(f"Press Enter to capture {['Pregunta', 'Incorrecta', 'Correcta'][i]} screenshot...")
    take_screenshot_and_save(folder_path, ['Pregunta', 'Incorrecta', 'Correcta'][i])

print("Screenshots captured. Program will exit now.")
