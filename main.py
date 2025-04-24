import logging
from app.config import setup_logging
from app.database import create_driver_table
from ui.main_window import App

def main():
    setup_logging()
    logging.info("Application started")
    create_driver_table()
    
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()