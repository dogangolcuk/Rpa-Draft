import pyautogui
import cv2
import numpy as np
import time
import json
from openpyxl import Workbook
import socket


def open_excel_and_write():
    workbook = Workbook()
    sheet = workbook.active
    sheet['E5'] = "Data written from RPA script WITH PYTHON"
    workbook.save('output.xlsx')


def find_and_double_click(icon_gray, icon_color, threshold):
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
        return True

    elif len(x_color) > 0 and len(y_color) > 0:
        icon_center_color = (
            x_color[0] + icon_color.shape[1] // 2, y_color[0] + icon_color.shape[0] // 2)
        pyautogui.moveTo(icon_center_color)
        pyautogui.doubleClick()
        return True

    return False


def start_socket_listener():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(5)

    while True:
        print("Listening for commands...")
        client_socket, address = server_socket.accept()
        print(f"Connection from {address} established.")

        try:
            commands = json.loads(client_socket.recv(1024).decode())
            for cmd in commands:
                print("cmd", cmd["command"])
                if cmd["command"] == "findImage":
                    iconPath = cmd["imagePath"]
                    iconGray = cv2.imread(iconPath, cv2.IMREAD_GRAYSCALE)
                    iconColor = cv2.imread(iconPath)
                    time.sleep(1)
                    if cmd["action"] == "doubleClick":
                        if not find_and_double_click(iconGray, iconColor, threshold=0.8):
                            print(
                                f"Icon '{iconPath}' not found on the screen.")
                elif cmd["command"] == "openExcelAndWrite":
                    open_excel_and_write()
        except json.JSONDecodeError as e:
            print("Error decoding JSON:", e)
        except Exception as ex:
            print("Error processing commands:", ex)

        client_socket.close()


start_socket_listener()
