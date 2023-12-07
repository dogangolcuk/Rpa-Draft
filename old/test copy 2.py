import cv2
import pyautogui
import numpy as np

# Path to the icon image you want to locate
icon_path = 'C:\\Users\\dogan\\Desktop\\test\\1.png'

# Load the icon image and the screenshot
icon = cv2.imread(icon_path, cv2.IMREAD_GRAYSCALE)
screenshot = pyautogui.screenshot()
screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

# Apply thresholding to convert images into binary format
_, icon_threshold = cv2.threshold(icon, 127, 255, cv2.THRESH_BINARY)
_, screenshot_threshold = cv2.threshold(screenshot, 127, 255, cv2.THRESH_BINARY)

# Find contours in the screenshot
contours, _ = cv2.findContours(screenshot_threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Loop through contours to find the closest matching contour to the icon
closest_contour = None
min_diff = float('inf')

for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    if w > 10 and h > 10:  # Filter small contours
        cropped_screenshot = screenshot_threshold[y:y+h, x:x+w]
        resized_icon = cv2.resize(icon_threshold, (w, h))
        diff = cv2.matchTemplate(cropped_screenshot, resized_icon, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(diff)
        if max_val < min_diff:
            min_diff = max_val
            closest_contour = contour

# If a contour resembling the icon is found, move the mouse and double click
if closest_contour is not None:
    x, y, w, h = cv2.boundingRect(closest_contour)
    icon_center = (x + w // 2, y + h // 2)
    pyautogui.moveTo(icon_center)
    pyautogui.doubleClick()
else:
    print("Icon not found on the screen.")
