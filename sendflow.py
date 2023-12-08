import socket
import json
import argparse

def send_commands_to_socket(file_path, host, port):
    try:
        with open(file_path, 'r') as file:
            commands_json = file.read()

            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((host, port))
            client_socket.sendall(bytes(commands_json, 'utf-8'))
            client_socket.close()

            print("Commands sent to the socket.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Send commands from a JSON file to a socket')
    parser.add_argument('file', metavar='file', type=str, help='Path to the JSON file')
    parser.add_argument('--host', default='127.0.0.1', help='Host IP for the socket (default: 127.0.0.1)')
    parser.add_argument('--port', type=int, default=12345, help='Port for the socket (default: 12345)')

    args = parser.parse_args()

    send_commands_to_socket(args.file, args.host, args.port)
