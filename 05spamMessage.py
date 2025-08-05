import pyautogui
import time


def spamMessage():
    time.sleep(4)
    text = open("msg.txt")
    for eachLine in text:
        pyautogui.typewrite(eachLine)
        pyautogui.press("enter")


spamMessage()
