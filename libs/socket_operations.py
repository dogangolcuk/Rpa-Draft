import socket
import json
from libs.data_operations import manipulate_and_write_data
from libs.excel_operations import excel_to_pandas
from libs.screen_operations import handle_screen_record, stop_screen_record
from libs.image_operations import process_image_commands
from libs.logging_utils import log_message

stop_listener = False


def stop_listener_flag(cmd):
    global stop_listener
    stop_listener = True
    return stop_listener


COMMAND_DISPATCHER = {
    "none": lambda cmd: None,
    "findImage": process_image_commands,
    "startScreenRecord": handle_screen_record,
    "stopScreenRecord": stop_screen_record,
    "stopServerAgent": stop_listener_flag,
    "excelToPandas": excel_to_pandas,
    "manipulateData": manipulate_and_write_data,
}


def start_socket_listener():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(5)

    while not stop_listener:
        print("Listening for commands...")
        client_socket, address = server_socket.accept()
        print(f"Connection from {address} established.")
        log_message(f"Connection from {address} established.")

        try:
            commands = json.loads(client_socket.recv(1024).decode())
            for cmd in commands:
                log_message(f"Received command: {cmd['command']}")
                command_function = COMMAND_DISPATCHER.get(cmd["command"])
                if command_function:
                    command_function(cmd)
                    log_message(f"Executed command: {cmd['command']}")
                else:
                    log_message(f"Command '{cmd['command']}' not supported.")
        except json.JSONDecodeError as e:
            log_message(f"Error decoding JSON: {e}")
        except Exception as ex:
            log_message(f"Error processing commands: {ex}")

        client_socket.close()

    server_socket.close()
