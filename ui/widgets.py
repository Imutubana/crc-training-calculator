import tkinter as tk
from PIL import Image, ImageTk
from app import Config

def populate_application_image(container):
    # Load the image using PIL
    original_image = Image.open(Config.LOGO_PATH)
    resized_image = original_image.resize((300, 300), Image.Resampling.LANCZOS)
    photo_image = ImageTk.PhotoImage(resized_image)

    # Place the image
    image_label = tk.Label(container, image=photo_image)
    image_label.grid(row=0, column=0, sticky='nsew')
    image_label.image = photo_image
