import logging
import tkinter as tk
from tkinter import ttk, messagebox
from ui.styles import init_styles
from ui.widgets import populate_application_image

def run_app():
    logging.info("Launching GUI...")

    root = tk.Tk()
    root.title("Cardiff Racing Club - Training Manager")
    root.geometry("500x500")

    init_styles()

    # Configure grid layout
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=0) # Welcome header
    root.rowconfigure(1, weight=1) # Company Logo
    root.rowconfigure(2, weight=0) # Navigation buttons

    # Welcome header
    header_frame = ttk.Frame(root, style="Blue.TFrame")   
    header_frame.grid(row=0, column=0, sticky='new', padx=10, pady=10)
    header_frame.grid_columnconfigure(0, weight=1)
    header_frame.grid_rowconfigure(0, weight=0)

    header_label = tk.Label(header_frame,text="Welcome to Cardiff Racing Club Manager")
    header_label.grid(row=0, column=0, padx=10, pady=10, sticky="new")

    # Company logo
    image_frame = ttk.Frame(root, style="Green.TFrame")   
    image_frame.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)
    image_frame.grid_columnconfigure(0, weight=1)
    image_frame.grid_rowconfigure(0, weight=1)

    populate_application_image(image_frame)

    # Navigation buttons
    def on_start():
        logging.info("Start button clicked")
        messagebox.showinfo("Coming Soon", "Driver input coming next!")

    button_frame = ttk.Frame(root, style="Red.TFrame")   
    button_frame.grid(row=2, column=0, sticky='sew', padx=10, pady=10)
    button_frame.grid_columnconfigure(0, weight=1)
    button_frame.grid_rowconfigure(0, weight=0)

    start_button = tk.Button(button_frame, text="Start", command=on_start)
    start_button.grid(row=0, column=0, sticky='sew', pady=10, padx=10)

    root.mainloop()
