import logging
import tkinter as tk
from tkinter import ttk, messagebox
from ui.widgets import populate_application_image

class CalculatorPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, style="Green.TFrame")
        logging.info("Initialising calculator page...")

        self.controller = controller
        
        # Configure grid layout
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=0) 

    def show(self):
        self.tkraise()
        logging.info("Calculator page loaded")

