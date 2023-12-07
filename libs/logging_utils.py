import logging

logging.basicConfig(filename='rpa_agent.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def log_message(message):
    logging.info(message)
    print(message)
