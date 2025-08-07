import pyautogui as pa
import time
import keyboard

pa.PAUSE = 1


while True:
    if keyboard.is_pressed('esc'):
        print("Encerrando script com ESC...")
        break
    time.sleep(2)
    pa.click(x=974, y=1007)
    pa.click(x=1015, y=1013)