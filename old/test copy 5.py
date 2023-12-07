import pyautogui
import cv2
import numpy as np
import time

def find_and_double_click(icon_gray, icon_color, threshold):
    # Take a screenshot
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

    # Apply template matching with both color and grayscale images
    result_gray = cv2.matchTemplate(screenshot_gray, icon_gray, cv2.TM_CCOEFF_NORMED)
    result_color = cv2.matchTemplate(screenshot, icon_color, cv2.TM_CCOEFF_NORMED)

    # Find locations where the matches are above the thresholds
    y_gray, x_gray = np.where(result_gray >= threshold)
    y_color, x_color = np.where(result_color >= threshold)

    # If matches above the thresholds are found, perform the action
    if len(x_gray) > 0 and len(y_gray) > 0:
        # Calculate the center of the matched icon in grayscale
        icon_center_gray = (x_gray[0] + icon_gray.shape[1] // 2, y_gray[0] + icon_gray.shape[0] // 2)
        pyautogui.moveTo(icon_center_gray)
        pyautogui.doubleClick()
        return True
    
    elif len(x_color) > 0 and len(y_color) > 0:
        # Calculate the center of the matched icon in color
        icon_center_color = (x_color[0] + icon_color.shape[1] // 2, y_color[0] + icon_color.shape[0] // 2)
        pyautogui.moveTo(icon_center_color)
        pyautogui.doubleClick()
        return True
    
    return False

# Path to the icon images
icon_path = 'C:\\Users\\dogan\\Desktop\\test\\images\\1.png'
icon_path2 = 'C:\\Users\\dogan\\Desktop\\test\\images\\2.png'

# Load the icon images in both grayscale and color
icon_gray = cv2.imread(icon_path, cv2.IMREAD_GRAYSCALE)
icon_color = cv2.imread(icon_path)

icon_gray2 = cv2.imread(icon_path2, cv2.IMREAD_GRAYSCALE)
icon_color2 = cv2.imread(icon_path2)

# Set thresholds for similarity
threshold = 0.8

# Find and double-click on the first icon
if find_and_double_click(icon_gray, icon_color, threshold):
    time.sleep(1.0)
    # Find and double-click on the second icon
    find_and_double_click(icon_gray2, icon_color2, threshold)
else:
    print("Icon not found on the screen.")
