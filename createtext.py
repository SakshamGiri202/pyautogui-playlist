import pyautogui
import time


def createText(text):
    pyautogui.typewrite(text, interval=0.05)


def type_until_word_count(target_word_count, text):
    word_count = 0
    words_per_iteration = len(text.split())

    time.sleep(2)  # Give time to focus the target input field

    while word_count < target_word_count:
        createText(text + " ")  # Add space after to separate words
        word_count += words_per_iteration
        # time.sleep(0.5)  # Optional delay between iterations
        pyautogui.press("enter")


# Example usage with any string:
input_string = "hello honey"
type_until_word_count(1000000000000000, input_string)
