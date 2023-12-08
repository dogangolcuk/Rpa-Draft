from common_imports import socket, json
from libs.data_operations import manipulate_and_write_data
from libs.excel_operations import  excel_to_pandas
from libs.screen_operations import handle_screen_record, stop_screen_record
from libs.image_operations import process_image_commands
from libs.logging_utils import log_message


def start_socket_listener():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(5)

    stop_listener = False

    while not stop_listener:
        print("Listening for commands...")
        client_socket, address = server_socket.accept()
        print(f"Connection from {address} established.")
        log_message(f"Connection from {address} established.")

        try:
            commands = json.loads(client_socket.recv(1024).decode())
            for cmd in commands:
                print("cmd", cmd["command"])
                log_message(f"Received command: {cmd['command']}")
                # process_image_commands(cmd)
                if cmd["command"] == "none":
                    pass
                elif cmd["command"] == "findImage":
                    process_image_commands(cmd)
                    log_message(f'Received command to click on {
                                cmd["imagePath"]} image on the screen.')
                elif cmd["command"] == "startScreenRecord":
                    handle_screen_record()
                    log_message("Received command to start screen recording.")
                elif cmd["command"] == "stopScreenRecord":
                    stop_screen_record()
                    log_message("Received command to stop screen recording.")
                elif cmd["command"] == "stopServerAgent":
                    stop_listener = True
                    log_message("Received command to stop the listener.")
                elif cmd["command"] == "excelToPandas":
                    excel_to_pandas(cmd)
                    log_message(f'Received command to convert {
                                cmd['filePath']} to Pandas DataFrame.')
                elif cmd["command"] == "manipulateData":
                    manipulate_and_write_data(cmd)
                    log_message(f'Received command to manipulate data with ID: {cmd["getDataId"]}.')
        except json.JSONDecodeError as e:
            log_message(f"Error decoding JSON: {e}")
        except Exception as ex:
            log_message(f"Error processing commands: {ex}")

        client_socket.close()

    server_socket.close()
