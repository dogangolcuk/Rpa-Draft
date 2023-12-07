import pyautogui
import cv2
import numpy as np
import time
import json
from openpyxl import Workbook
import socket
import logging
import datetime
import os
import threading


logging.basicConfig(filename='rpa_agent.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')



def log_message(message):
    logging.info(message)
    print(message)


def open_excel_and_write():
    try:
        workbook = Workbook()
        sheet = workbook.active
        sheet['E5'] = "Data written from RPA script WITH PYTHON"
        workbook.save('output.xlsx')
        log_message("Opened Excel and wrote data successfully.")
    except Exception as e:
        log_message(f"Error opening Excel and writing data: {e}")


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


is_recording = False



def start_screen_record():
    agent_directory = os.path.dirname(os.path.realpath(__file__))
    recordings_dir = os.path.join(agent_directory, "recordings")
    os.makedirs(recordings_dir, exist_ok=True)

    global is_recording
    try:
        screen_width, screen_height = pyautogui.size()
        codec = cv2.VideoWriter_fourcc(*"XVID")

        current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        output_file = os.path.join(recordings_dir, f"screen_record_{current_time}.avi")


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


def start_socket_listener():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(5)

    while True:
        print("Listening for commands...")
        client_socket, address = server_socket.accept()
        print(f"Connection from {address} established.")
        log_message(f"Connection from {address} established.")

        try:
            commands = json.loads(client_socket.recv(1024).decode())
            for cmd in commands:
                print("cmd", cmd["command"])
                log_message(f"Received command: {cmd['command']}")
                if cmd["command"] == "findImage":
                    iconPath = cmd["imagePath"]
                    iconGray = cv2.imread(iconPath, cv2.IMREAD_GRAYSCALE)
                    iconColor = cv2.imread(iconPath)
                    time.sleep(1)
                    if cmd["action"] == "doubleClick":
                        if not find_and_double_click(iconGray, iconColor, threshold=0.8):
                            log_message(
                                f"Icon '{iconPath}' not found on the screen.")
                elif cmd["command"] == "openExcelAndWrite":
                    open_excel_and_write()
                elif cmd["command"] == "startScreenRecord":
                    handle_screen_record()
                    log_message("Received command to start screen recording.")
                elif cmd["command"] == "stopScreenRecord":
                    stop_screen_record()
                    log_message("Received command to stop screen recording.")
        except json.JSONDecodeError as e:
            log_message(f"Error decoding JSON: {e}")
        except Exception as ex:
            log_message(f"Error processing commands: {ex}")

        client_socket.close()


start_socket_listener()
