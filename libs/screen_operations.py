import pyautogui
import cv2
import numpy as np
import time
import os
import datetime
import threading
from .logging_utils import log_message

is_recording = False


def find_and_double_click(icon_gray, icon_color, threshold):
    try:
        screenshot = pyautogui.screenshot()
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

        result_gray = cv2.matchTemplate(
            screenshot_gray, icon_gray, cv2.TM_CCOEFF_NORMED)
        result_color = cv2.matchTemplate(
            screenshot, icon_color, cv2.TM_CCOEFF_NORMED)

        y_gray, x_gray = np.where(result_gray >= threshold)
        y_color, x_color = np.where(result_color >= threshold)

        if len(x_gray) > 0 and len(y_gray) > 0:
            icon_center_gray = (
                x_gray[0] + icon_gray.shape[1] // 2, y_gray[0] + icon_gray.shape[0] // 2)
            pyautogui.moveTo(icon_center_gray)
            pyautogui.doubleClick()
            log_message("Found and double-clicked the icon.")
            return True

        elif len(x_color) > 0 and len(y_color) > 0:
            icon_center_color = (
                x_color[0] + icon_color.shape[1] // 2, y_color[0] + icon_color.shape[0] // 2)
            pyautogui.moveTo(icon_center_color)
            pyautogui.doubleClick()
            log_message("Found and double-clicked the colored icon.")
            return True

        log_message("Icon not found on the screen.")
        return False
    except Exception as e:
        log_message(f"Error finding and double-clicking icon: {e}")
        return False


def start_screen_record():
    current_directory = os.path.dirname(os.path.realpath(__file__))
    parent_directory = os.path.dirname(current_directory)

    recordings_dir = os.path.join(parent_directory, "recordings")
    os.makedirs(recordings_dir, exist_ok=True)

    global is_recording
    try:
        screen_width, screen_height = pyautogui.size()
        codec = cv2.VideoWriter_fourcc(*"XVID")

        current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        output_file = os.path.join(
            recordings_dir, f"screen_record_{current_time}.avi")

        output = cv2.VideoWriter(
            output_file, codec, 20.0, (screen_width, screen_height))

        log_message(f"Started screen recording to {output_file}...")
        is_recording = True
        while is_recording:
            screenshot = pyautogui.screenshot()
            frame = np.array(screenshot)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            output.write(frame)

            time.sleep(0.05)

        output.release()
        log_message(f"Stopped screen recording.")
    except Exception as e:
        log_message(f"Error during screen recording: {e}")


def stop_screen_record():
    time.sleep(3.0)
    global is_recording
    is_recording = False


def handle_screen_record():
    global is_recording
    if is_recording:
        return
    is_recording = True
    threading.Thread(target=start_screen_record, daemon=True).start()
