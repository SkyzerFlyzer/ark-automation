import time

import pyautogui

print(f"Resolution: {pyautogui.size()}")

while True:
    print(pyautogui.position())
    time.sleep(2)
