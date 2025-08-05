import pyautogui as py
import time


# yt shorts liker example
time.sleep(3)
py.moveTo(988, 580)
py.doubleClick()


for i in range(100):
    py.moveTo(1329, 469)
    time.sleep(1)
    py.click()
    time.sleep(1)
    py.moveTo(1852, 704)
    time.sleep(1)
    py.leftClick()

# print(py.position())
