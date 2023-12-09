import sys
import os
import pystray
from PIL import Image
import subprocess
import threading

current_dir = os.path.dirname(os.path.abspath(__file__))
libs_path = os.path.join(current_dir, 'libs')
utils_path = os.path.join(libs_path, 'utils')

sys.path.append(libs_path)
sys.path.append(utils_path)

from libs.socket_operations import start_socket_listener

def main():
    # Start socket listener in a separate thread
    socket_thread = threading.Thread(target=start_socket_listener)
    socket_thread.daemon = True  # Daemonize the thread
    socket_thread.start()

def on_exit(icon, item):
    print("Exiting...")
    # Execute the script on exit
    subprocess.run(["python", "sendflow.py", os.path.join("tasks", "stopAgent.json")])
    # Any cleanup code you want before exiting
    icon.stop()  # Stop the system tray icon
    sys.exit(0)

def on_about(icon, item):
    print("About this app...")
    # Show information about the application

# Create the tray icon and menu
icon_path = "icons8-automation-32.png"  # Replace with your icon path
icon = pystray.Icon("MyApp", Image.open(icon_path), "MyApp")
icon.menu = (pystray.MenuItem("Exit", on_exit), pystray.MenuItem("About", on_about))

# Start the application
main()

# Start the system tray loop
icon.run()
