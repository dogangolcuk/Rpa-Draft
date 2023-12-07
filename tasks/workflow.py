import socket
import json

# Define the commands in the specified JSON format
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
    },
    {
        "command": "openExcelAndWrite"
    }
]

# Convert commands to JSON format
commands_json = json.dumps(commands)

# Create a socket and connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Change IP and port to match server
client_socket.connect(('127.0.0.1', 12345))

# Send the JSON-formatted commands
client_socket.sendall(bytes(commands_json, 'utf-8'))

# Close the socket connection
client_socket.close()
