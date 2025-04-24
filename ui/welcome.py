import logging
import tkinter as tk
from tkinter import ttk, messagebox
from ui.widgets import populate_application_image

class WelcomePage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, style="Green.TFrame")
        logging.info("Initialising welcome page...")

        self.controller = controller
        
        # Configure grid layout
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=0) # Welcome header
        self.rowconfigure(1, weight=1) # Company Logo
        self.rowconfigure(2, weight=0) # Navigation buttons

        # Welcome header
        header_frame = ttk.Frame(self, style="Blue.TFrame")   
        header_frame.grid(row=0, column=0, sticky='nsew', padx=10, pady=(10,5))
        header_frame.grid_columnconfigure(0, weight=1)
        header_frame.grid_rowconfigure(0, weight=1)

        header_label = tk.Label(header_frame,text="Welcome to Cardiff Racing Club Manager")
        header_label.grid(row=0, column=0, sticky="ns", padx=10, pady=10)

        # Company logo
        image_frame = ttk.Frame(self, style="Green.TFrame")   
        image_frame.grid(row=1, column=0, sticky='nsew', padx=10, pady=(5,5))
        image_frame.grid_columnconfigure(0, weight=1)
        image_frame.grid_rowconfigure(0, weight=1)

        populate_application_image(image_frame)

        # Navigation buttons
        button_frame = ttk.Frame(self, style="Red.TFrame")   
        button_frame.grid(row=2, column=0, sticky='nsew', padx=10, pady=(5,10))
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_rowconfigure(0, weight=1)

        start_button = tk.Button(button_frame, text="Start", command=self.on_start)
        start_button.grid(row=0, column=0, sticky='ns', pady=10, padx=10)

    def on_start(self):
        logging.info("Calculator page navigation selected")
        self.controller.show_frame("CalculatorPage")

    def show(self):
        self.tkraise()
        logging.info("Welcome page loaded")

