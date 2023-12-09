import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
libs_path = os.path.join(current_dir, 'libs')
utils_path = os.path.join(libs_path, 'utils')

sys.path.append(libs_path)
sys.path.append(utils_path)

# Dont take this line to line 1 because of import from libs and utils
from libs.socket_operations import start_socket_listener

def main():
    start_socket_listener()


if __name__ == "__main__":
    main()
