import os

import pyautogui
from datetime import datetime
import time, random
from os import system
import sys



# pip install  --trusted-host pypi.org --trusted-host files.pythonhosted.org pyautogui
pyautogui.FAILSAFE= False
print(str(pyautogui.size()))
print("Start time: " + str(datetime.now()))
mins = 300
for i in reversed(range(mins)):
    #pyautogui.scroll(10)
    x = random.randint(100, 1500)
    #y = random.randint(100, 800)
    time.sleep(60)
    try:
        #pyautogui.move(0, 500)
        pyautogui.moveTo(x, 500, 2, pyautogui.easeOutQuad)
        pyautogui.click()
        #pyautogui.moveTo(100, 200)
        print("Time remains = " + str(i) + " mins")
    except KeyboardInterrupt:
        sys.exit()

print("End time: " + str(datetime.now()))
#os.system("shutdown -l")
