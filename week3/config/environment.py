from dotenv import load_dotenv
import os


class Environment:
    def __init__(self):
        load_dotenv()

        self.app_env = os.getenv("APP_ENV")
        self.log_level = os.getenv("LOG_LEVEL")
        self.debug = os.getenv("DEBUG")


def load_environment():
    return Environment()