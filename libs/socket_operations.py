import socket
import json
import cv2
import time
from .excel_operations import open_excel_and_write
from .screen_operations import handle_screen_record, stop_screen_record
from .image_operations import process_image_commands
from .logging_utils import log_message

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
                # if cmd["command"] == "findImage":
                #     iconPath = cmd["imagePath"]
                #     iconGray = cv2.imread(iconPath, cv2.IMREAD_GRAYSCALE)
                #     iconColor = cv2.imread(iconPath)
                #     time.sleep(1)
                #     if cmd["action"] == "doubleClick":
                #         if not find_and_double_click(iconGray, iconColor, threshold=0.8):
                #             log_message(
                #                 f"Icon '{iconPath}' not found on the screen.")
                process_image_commands(cmd)
                if cmd["command"] == "openExcelAndWrite":
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

start_socket_listener()  # To start the socket listener
