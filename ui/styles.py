from tkinter import ttk
from app import Config
import logging

def init_styles():
    style = ttk.Style()

    # Use built-in default theme
    style.theme_use("default")

    if Config.DEV_UI:
        # Dev container styles
        style.configure("Red.TFrame", background="#FF6666")
        style.configure("Green.TFrame", background="#66FF66")
        style.configure("Blue.TFrame", background="#66B2FF")

        # Dev label styles
        style.configure("Yellow.TLabel", background="#FFFFCC", foreground="#333")

    logging.info("UI styles initialized")
