import os
import sys
import logging

class Config():
    VERSION = "1.0.1"
    DB_PATH = os.path.join("data", "cardiff_racing_club.db")
    LOG_PATH = os.path.join("data", "app.log")
    LOGO_PATH = os.path.join("assets", "cardiff_racing_club_logo.png")
    APP_USER_ID = 1
    APP_USER_NAME = "TestUsername"
    DEV_UI = False

def resource_path(relative_path):
    try: # Utilising PyInstaller created temp folder
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def setup_logging():
    # Ensure data folder exists
    if not os.path.exists(resource_path("data")):
        os.makedirs(resource_path("data"))

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(resource_path(Config.LOG_PATH)),
            logging.StreamHandler()
        ]
    )


