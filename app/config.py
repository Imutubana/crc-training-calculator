import os
import logging

class Config():
    VERSION = "1.0.0"

    DB_FILENAME = "cardiff_racing_club.db"
    DB_PATH = os.path.join("data", DB_FILENAME)

    LOG_FILENAME = "app.log"
    LOG_PATH = os.path.join("data", LOG_FILENAME)

    LOGO_FILENAME = "logo_revised_coloured.png"
    LOGO_PATH = os.path.join("assets", LOGO_FILENAME)

    APP_USER_ID = 1
    APP_USER_NAME = "TestUsername"
    
    DEV_UI = False

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(Config.LOG_PATH),
            logging.StreamHandler()
        ]
    )
