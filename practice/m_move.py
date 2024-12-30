import pyautogui
from datetime import datetime
import random, time

# pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org pyautogui
# Disale failsafe to prevent accidental termination
pyautogui.FAILSAFE = False

# get the screen size
screen_witdh, screen_height = pyautogui.size()
print("Screen size {}x{}".format(screen_witdh, screen_height))

# Set the total duration in munites
total_minutes = 70
print("Start time:", datetime.now().strftime("%H:%M:%S"))

try:
    for remaining_minutes in reversed(range(total_minutes)):
        # Randomly move the mouse to a new location
        x = random.randint(300, screen_witdh - 1)
        pyautogui.moveTo(x, 500, 2, pyautogui.easeOutQuad)
        # Perform a click at the current position
        pyautogui.click()
        print("Time remaining: ", remaining_minutes, " mins")
        time.sleep(60*3)
except KeyboardInterrupt:
    print("Process terminated by user")
