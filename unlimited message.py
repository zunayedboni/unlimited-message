import pyautogui
import time
message = 3
while message>0:
    time.sleep(2)
    pyautogui.typewrite('I am a good boy')
    time.sleep(1)
    pyautogui.press('enter')
    message = message - 1