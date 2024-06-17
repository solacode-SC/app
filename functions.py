import tkinter as tk
from PIL import Image, ImageTk


def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    window.geometry(f'{width}x{height}+{int(x)}+{int(y)}')





def start_header_animation(header_label, header):
    # Animation to move the label from right to left
    def move_label():
        x = header_label.winfo_x()
        new_x = x - 2 if x > -header_label.winfo_width() else header.winfo_width()
        header_label.place(x=new_x, y=110)
        header.after(10, move_label)  # Move every 10ms

    # def blink():
    #     current_color = header_label.cget("foreground")
    #     next_color = "red" if current_color == "black" else "black"
    #     header_label.config(foreground=next_color)
    #     header.after(500, blink)  # Toggle every 500ms

    # blink()

    move_label()

def load_image(path, width, height):
    img = Image.open(path)
    img = img.resize((width, height), Image.LANCZOS)
    return ImageTk.PhotoImage(img)


