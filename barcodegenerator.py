from customtkinter import *
import os, tempfile, io
from customtkinter import CTkToplevel as ct
import barcode as br
from tkinter import ttk
from PIL import Image, ImageTk
from barcode.writer import ImageWriter
def generator(id, window):
    popup = ct(window)
    popup.title("Image Popup")
    img_writer = ImageWriter()
    fp = io.BytesIO()
    br.Code128(code=id, writer=img_writer).write(fp)
    fp.seek(0)
    img = Image.open(fp)  
    photo = ImageTk.PhotoImage(img)
    image_label = ttk.Label(popup, image=photo)
    image_label.image = photo
    image_label.pack()
    print_button = ttk.Button(popup, text="Print Image", command=lambda: download(fp))
    print_button.pack(pady=10)


def download(fp):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp_file:
            tmp_file.write(fp.getvalue())
            temp_path = tmp_file.name
        os.startfile(temp_path, "print")
        print(f"Printing {temp_path}...")
    except FileNotFoundError:
        print(f"Error: Image file not found at {temp_path}")
    except Exception as e:
        print(f"An error occurred during printing: {e}")