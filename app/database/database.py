import sqlite3
import logging
from app.database import queries
from app import Config
from app.config import resource_path

def get_connection():
    return sqlite3.connect(resource_path(Config.DB_PATH))

def create_driver_table():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(queries.CREATE_DRIVERS_TABLE)
        conn.commit()
    except sqlite3.Error as e:
        logging.error("Database error: %s", e)
        raise
    finally:
        cursor.close()
        conn.close()
