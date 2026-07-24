import json


class Config:
    def __init__(self):
        with open("config/settings.json", "r") as file:
            settings = json.load(file)

        self.application_name = settings["application"]["name"]
        self.application_subtitle = settings["application"]["subtitle"]
        self.application_version = settings["application"]["version"]

        self.bank_name = settings["bank"]["name"]
        self.currency = settings["bank"]["currency"]
        self.minimum_deposit = settings["bank"]["minimum_deposit"]


def load_settings():
    return Config()