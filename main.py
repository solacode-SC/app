import tkinter as tk
from functions import *
from frames import *

root = tk.Tk()
root.title("Verification App")
root.resizable(False, False)
root.configure(bg="white")
window_width = 1000
window_height = 600
center_window(root, window_width, window_height)

header_set(root)

# Create a body frame with fixed height and variable width
body = tk.Frame(root, bg='#F1EFEF', width=window_width, height=(3 * window_height) // 4)
body.pack_propagate(False)  # Prevent frame from resizing to fit its children
body.pack(fill='x', pady=(window_height // 4, 0))  # Only fill horizontally, with padding at the top to position correctly

start_part(body,window_width, (3 * window_height) // 4)

root.mainloop()
