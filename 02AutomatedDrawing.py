import pyautogui
import time

time.sleep(3)                   # Time for you to focus the browser and position the mouse
pyautogui.click()               # Click to start drawing at the current mouse position
distance = 300
while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.2, button="left")
    distance = distance - 20
    pyautogui.dragRel(0, distance, duration=0.2, button="left")
    pyautogui.dragRel(-distance, 0, duration=0.2, button="left")
    distance = distance - 20
    pyautogui.dragRel(0, -distance, duration=0.2, button="left")
