import json

with open("config/settings.json", "r") as file:
    SETTINGS = json.load(file)

APPLICATION_NAME = SETTINGS["application_name"]
VERSION = SETTINGS["version"]
DATABASE_NAME = SETTINGS["database_name"]
PAGE_SIZE = SETTINGS["page_size"]