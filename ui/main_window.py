import logging
import tkinter as tk
from tkinter import ttk
from ui.styles.styles import init_styles
from ui.pages.welcome_page import WelcomePage
from ui.pages.calculator_page import CalculatorPage
from app import Config

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        logging.info("Launching GUI...")

        self.title(f"Cardiff Racing Club - Training Manager (v{Config.VERSION})")
        self.geometry("500x500")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        init_styles() # Initialise styles

        # Main container to hold all pages
        container = ttk.Frame(self, style="Blue.TFrame")
        container.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Page storage
        self.frames = {}

        # Initialise pages
        welcome_page = WelcomePage(parent=container, controller=self)
        welcome_page.grid(row=0, column=0, sticky="nsew", padx=10, pady=10) 
        self.frames["WelcomePage"] = welcome_page

        calculator_page = CalculatorPage(parent=container, controller=self)
        calculator_page.grid(row=0, column=0, sticky="nsew", padx=10, pady=10) 
        self.frames["CalculatorPage"] = calculator_page

        # Show application welcome page
        self.show_frame("WelcomePage")

    def show_frame(self, name):
        logging.info(f"Loading {name} page...")
        frame = self.frames.get(name)
        if frame:
            frame.show()
