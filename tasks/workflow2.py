import socket
import json

commands = [
    {
        "command": "findImage",
        "imagePath": "4.png",
        "action": "doubleClick"
    },
    {
        "command": "stopServerAgent",
    }
]

commands_json = json.dumps(commands)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 12345))
client_socket.sendall(bytes(commands_json, 'utf-8'))
client_socket.close()
