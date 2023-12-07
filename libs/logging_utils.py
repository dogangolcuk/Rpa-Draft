# import logging
# import os
from common_imports import os, logging

logs_directory = 'logs'

if not os.path.exists(logs_directory):
    os.makedirs(logs_directory)

log_file_path = os.path.join(logs_directory, 'rpa_agent.log')

logging.basicConfig(filename=log_file_path, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def log_message(message):
    logging.info(message)
    print(message)
