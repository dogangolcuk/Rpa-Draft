import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
libs_path = os.path.join(current_dir, 'libs')
utils_path = os.path.join(libs_path, 'utils')

sys.path.append(libs_path)
sys.path.append(utils_path)

from libs.socket_operations import start_socket_listener

if __name__ == "__main__":
    start_socket_listener()
