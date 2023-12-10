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

from libs.socket_operations import start_listener_flag, stop_listener_flag

socket_thread = None

def start_socket(icon, item):
    global socket_thread
    if socket_thread is None or not socket_thread.is_alive():
        socket_thread = threading.Thread(target=start_listener_flag())
        socket_thread.daemon = True
        socket_thread.start()
        icon.menu = update_menu()
    else:
        print("Socket already running.")

def stop_socket(icon, item):
    print("Stopping socket...")
    global socket_thread
    if socket_thread and socket_thread.is_alive():
        print("Stopping socket...2")
        # socket_thread.join()
        stop_listener_flag(None)  # Call the function to stop the socket listener
        print("Stopping socket...3")
        # socket_thread.join()  # Wait for the thread to complete
        print("Stopping socket...4")
        socket_thread = None
        print("Socket stopped.")
        icon.menu = update_menu()
    else:
        print("Socket is not running.")

def on_exit(icon, item):
    print("Exiting...")
    # subprocess.run(["python", "sendflow.py", os.path.join("tasks", "stopAgent.json")])
    stop_listener_flag(None)  # Call the function to stop the socket listener
    
    icon.stop()  # Stop the system tray icon
    sys.exit(0)

def on_about(icon, item):
    print("About this app...")

def update_menu():
    global socket_thread
    menu_items = [
        pystray.MenuItem("Start Socket", start_socket),
        pystray.MenuItem("Stop Socket", stop_socket),
        pystray.MenuItem("Exit", on_exit),
        pystray.MenuItem("About", on_about)
    ]

    if socket_thread and socket_thread.is_alive():
        menu_items[0] = pystray.MenuItem("Start Socket (Running)", start_socket)
    else:
        menu_items[1] = pystray.MenuItem("Stop Socket (Not Running)", stop_socket)

    return tuple(menu_items)

def main(icon):
    icon.menu = update_menu()
    icon.visible = True
    # start_socket(icon,icon.menu)
if __name__ == "__main__":
    icon_path = "icons8-robot-48.png"  # Replace with your icon path
    icon = pystray.Icon("MyApp", Image.open(icon_path), "MyApp")
    icon.menu = update_menu()
    icon.title = "MyApp"
    
    icon.run(main)
