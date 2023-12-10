import socket
import json
from libs.data_operations import manipulate_and_write_data
from libs.excel_operations import excel_to_pandas
from libs.screen_operations import handle_screen_record, stop_screen_record
from libs.image_operations import process_image_commands
from libs.logging_utils import log_message

stop_listener = False
listening_message_displayed = False
# should_stop = False  # Add this flag


def start_listener_flag():
    global stop_listener
    # global should_stop
    stop_listener = False
    # should_stop = False
    start_socket_listener()


def stop_listener_flag(cmd):
    # global should_stop
    # should_stop = True
    global stop_listener
    global listening_message_displayed
    listening_message_displayed = False
    stop_listener = True


COMMAND_DISPATCHER = {
    "none": lambda cmd: None,
    "findImage": process_image_commands,
    "startScreenRecord": handle_screen_record,
    "stopScreenRecord": stop_screen_record,
    "stopServerListener": stop_listener_flag,
    "startServerListener": start_listener_flag,
    "excelToPandas": excel_to_pandas,
    "manipulateData": manipulate_and_write_data,
}


def start_socket_listener():
    global stop_listener, listening_message_displayed

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(
        socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Set SO_REUSEADDR

    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(5)
    server_socket.settimeout(2)  # Set a timeout on accept
    listening_message_displayed = False  # Flag to track the message display


    while not stop_listener:
        # if should_stop:
        #     breakc
        

        try:
            # print("Listening for commands...")
            if not listening_message_displayed:
                log_message("Listening for commands...")
                listening_message_displayed = True
                
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
                        listening_message_displayed = False
                    else:
                        log_message(
                            f"Command '{cmd['command']}' not supported.")
                        listening_message_displayed = False
            except json.JSONDecodeError as e:
                log_message(f"Error decoding JSON: {e}")
            except Exception as ex:
                log_message(f"Error processing commands: {ex}")

            client_socket.close()

        except socket.timeout:
            pass

        if stop_listener:
            break

    server_socket.close()
