import socket
import json

commands = [
    {
        "command": "startScreenRecord",
    },
    {
        "command": "findImage",
        "imagePath": "C:\\Users\\dogan\\Desktop\\test\\snaps\\1.png",
        "action": "doubleClick"
    },
    {
        "command": "findImage",
        "imagePath": "C:\\Users\\dogan\\Desktop\\test\\snaps\\2.png",
        "action": "doubleClick"
    },
    {
        "command": "findImage",
        "imagePath": "C:\\Users\\dogan\\Desktop\\test\\snaps\\3.png",
        "action": "doubleClick"
    },
    {
        "command": "stopScreenRecord",
    }
]

commands_json = json.dumps(commands)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 12345))
client_socket.sendall(bytes(commands_json, 'utf-8'))
client_socket.close()
