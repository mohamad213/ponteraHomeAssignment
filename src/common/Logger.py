import logging


class Logger:
    def __init__(self):
        # Create a custom logger
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)  # Set the logging level

        # Create handlers
        c_handler = logging.StreamHandler()  # Console handler
        c_handler.setLevel(logging.INFO)  # Set the level for console handler

        # Create formatters and add them to handlers
        c_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        c_handler.setFormatter(c_format)

        # Add handlers to the logger
        self.logger.addHandler(c_handler)

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)


# Instantiate the Logger class
logger = Logger()
