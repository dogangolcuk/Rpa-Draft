import pyautogui
import cv2
import numpy as np

# Path to the icon image you want to locate
icon_path = 'C:\\Users\\dogan\\Desktop\\test\\1.png'

# Load the icon image and the screenshot
icon = cv2.imread(icon_path, cv2.IMREAD_GRAYSCALE)
screenshot = pyautogui.screenshot()
screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)
cv2.imshow('Icon', icon)
cv2.imshow('Screenshot', screenshot)
cv2.waitKey(0)  # Wait for any key to be pressed
cv2.destroyAllWindows()  # Close all OpenCV windows


# Apply template matching
result = cv2.matchTemplate(screenshot, icon, cv2.TM_CCOEFF_NORMED)

# Set a threshold for similarity
threshold = 0.8

# Find locations where the match is above the threshold
y, x = np.where(result >= threshold)
# cv2.waitKey(0)  # Wait for any key to be pressed
# cv2.destroyAllWindows()  # Close all OpenCV windows
# If a match above the threshold is found, perform the action
if len(x) > 0 and len(y) > 0:
    # Calculate the center of the matched icon
    icon_center = (x[0] + icon.shape[1] // 2, y[0] + icon.shape[0] // 2)

    # Move the mouse to the center of the found icon and perform actions
    pyautogui.moveTo(icon_center)
    pyautogui.doubleClick()
    # Perform other actions here if needed

else:
    print("Icon not found on the screen.")
