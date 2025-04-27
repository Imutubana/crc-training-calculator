from tkinter import ttk
from PIL import Image, ImageTk
from app import Config
from app.config import resource_path

def populate_application_image(container):
    # Load the image
    original_image = Image.open(resource_path(Config.LOGO_PATH))
    resized_image = original_image.resize((300, 300), Image.Resampling.LANCZOS)
    photo_image = ImageTk.PhotoImage(resized_image)

    # Place image in label
    image_label = ttk.Label(container, image=photo_image, style="Yellow.TLabel")
    image_label.grid(row=0, column=0, padx=10, pady=10)
    image_label.image = photo_image
