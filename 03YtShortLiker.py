import pyautogui as py
import time


# yt shorts liker example
time.sleep(3)

py.click()

for i in range(10):
    py.moveTo(2141, 949)
    time.sleep(1)
    py.doubleClick()
    time.sleep(1)
    py.moveTo(2995, 1040)
    time.sleep(1)
    py.leftClick()
#
# print(py.position())
