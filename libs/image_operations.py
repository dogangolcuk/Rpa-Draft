import cv2
import time
import os
from libs.screen_operations import find_and_double_click
from libs.logging_utils import log_message


def process_image_commands(cmd):
    # if cmd["command"] == "findImage":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    snaps_path = os.path.join(parent_dir, 'snaps')
    iconPath = os.path.join(snaps_path, cmd["imagePath"])
    iconGray = cv2.imread(iconPath, cv2.IMREAD_GRAYSCALE)
    iconColor = cv2.imread(iconPath)
    time.sleep(1)
    if cmd["action"] == "doubleClick":
        if not find_and_double_click(iconGray, iconColor, threshold=0.8):
            log_message(f"Icon '{iconPath}' not found on the screen.")
