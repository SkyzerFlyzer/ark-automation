import time

import pyautogui

with open('commands.txt', 'r') as f:
    commands = f.readlines()


def enter_command(command: str):
    # press the ` key
    pyautogui.press('`')
    time.sleep(0.1)
    # type the command
    pyautogui.typewrite(command)
    time.sleep(0.1)
    # press enter
    pyautogui.press('enter')
    time.sleep(0.1)


def main():
    for command in commands:
        enter_command(command)
    pyautogui.alert('Done')
