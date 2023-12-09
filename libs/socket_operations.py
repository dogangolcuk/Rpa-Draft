# from common_imports import socket, json
import socket
import json
from libs.data_operations import manipulate_and_write_data
from libs.excel_operations import excel_to_pandas
from libs.screen_operations import handle_screen_record, stop_screen_record
from libs.image_operations import process_image_commands
from libs.logging_utils import log_message
# from libs.stop_agent import stop_listener_flag as stop_agent_stop_listener_flag


stop_listener = False  # Define as global variable


def stop_listener_flag(cmd):
    global stop_listener
    stop_listener = True
    return stop_listener

# Command dispatcher mapping commands to functions
COMMAND_DISPATCHER = {
    "none": lambda cmd: None,
    "findImage": process_image_commands,
    "startScreenRecord": handle_screen_record,
    "stopScreenRecord": stop_screen_record,
    "stopServerAgent": stop_listener_flag,  # Stop the listener
    "excelToPandas": excel_to_pandas,
    "manipulateData": manipulate_and_write_data,
}

# Additional function to expose stop_listener modification




def start_socket_listener():
    # from libs.stop_agent import stop_listener_flag as stop_agent_stop_listener_flag
    # COMMAND_DISPATCHER["stopServerAgent"] = stop_agent_stop_listener_flag

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(5)

    # stop_listener = False

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

                # Retrieve the corresponding function from the command dispatcher
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
