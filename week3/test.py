from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv("APP_ENV"))
print(os.getenv("LOG_LEVEL"))
print(os.getenv("DEBUG"))