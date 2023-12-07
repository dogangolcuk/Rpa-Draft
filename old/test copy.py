import cv2
import pyautogui
import numpy as np

# Path to the icon image you want to locate
icon_path = 'C:\\Users\\dogan\\Desktop\\test\\1.png'

# Load the icon image
icon = cv2.imread(icon_path, cv2.IMREAD_GRAYSCALE)

# Take a screenshot
screenshot = pyautogui.screenshot()
screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

# Perform template matching
result = cv2.matchTemplate(screenshot, icon, cv2.TM_CCOEFF_NORMED)

# Define a threshold for similarity
threshold = 0.8
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# If a match above the threshold is found, move the mouse and double click
if max_val >= threshold:
    # Get the center of the matched icon
    icon_width, icon_height = icon.shape[::-1]
    icon_center = (max_loc[0] + icon_width // 2, max_loc[1] + icon_height // 2)

    # Move the mouse to the center of the found icon and double click
    pyautogui.moveTo(icon_center)
    pyautogui.doubleClick()
else:
    print("Icon not found on the screen.")
