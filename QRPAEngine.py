import sys
import os
import pystray
import threading
from PIL import Image



CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
LIBS_PATH = os.path.join(CURRENT_DIR, 'libs')
UTILS_PATH = os.path.join(LIBS_PATH, 'utils')

sys.path.append(LIBS_PATH)
sys.path.append(UTILS_PATH)

# Custom imports
from libs.socket_operations import start_listener_flag, stop_listener_flag

socket_thread = None

def start_socket(icon, item):
    global socket_thread
    if not socket_thread or not socket_thread.is_alive():
        socket_thread = threading.Thread(target=start_listener_flag)
        socket_thread.daemon = True
        socket_thread.start()
        icon.menu = update_menu()
    else:
        print("Socket already running.")

def stop_socket(icon, item):
    global socket_thread
    if socket_thread and socket_thread.is_alive():
        stop_listener_flag(None)
        socket_thread = None
        icon.menu = update_menu()
        print("Socket stopped.")
    else:
        print("Socket is not running.")

def on_exit(icon, item):
    stop_listener_flag(None)
    icon.stop()
    sys.exit(0)

def on_about(icon, item):
    print("POC of QRPA Engine app...")

def update_menu():
    global socket_thread
    menu_items = [
        pystray.MenuItem("Start Socket", start_socket),
        pystray.MenuItem("Stop Socket", stop_socket),
        pystray.MenuItem("About", on_about),
        pystray.MenuItem("Exit", on_exit)
        
    ]

    start_socket_text = "Start Socket (Running)" if socket_thread and socket_thread.is_alive() else "Start Socket"
    stop_socket_text = "Stop Socket (Not Running)" if not start_socket_text == "Start Socket (Running)" else "Stop Socket"
    
    menu_items[0] = pystray.MenuItem(start_socket_text, start_socket)
    menu_items[1] = pystray.MenuItem(stop_socket_text, stop_socket)

    return tuple(menu_items)

def main(icon):
    start_socket(icon, None)  # Start the socket listener
    icon.menu = update_menu()
    icon.visible = True

if __name__ == "__main__":
    ICON_PATH = "icons8-robot-94.png"
    icon = pystray.Icon("QRPA Engine", Image.open(ICON_PATH), "QRPA Engine")
    icon.menu = update_menu()
    icon.title = "QRPA Engine"
    
    icon.run(main)
