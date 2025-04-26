import logging
from app.config import setup_logging
from app.database.database import create_driver_table
from ui.main_window import App
from app import Config

def main():
    setup_logging()
    logging.info(f"Application version {Config.VERSION} started")
    create_driver_table()
    
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()