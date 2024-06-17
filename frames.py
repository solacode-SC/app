from functions import *
from frame_Asblg import *
from frame_P3 import *
import tkinter as tk
from PIL import Image, ImageTk



def header_set(header):
    header_label = tk.Label(header, text="Verification Automatique des regles de metiers", font=("Arial", 16), bg='white', fg='black')
    header_label.place(y=110)

    image_path1 = 'C:\\Users\\synel\\Desktop\\myProjects\\Programming\\Python\\python tkinter\MedAllal\\program\\img\\1.png'  # Replace with your image path
    image_path2 = 'C:\\Users\\synel\\Desktop\\myProjects\\Programming\\Python\\python tkinter\MedAllal\\program\\img\\2.png'  # Replace with your image path
    image_path3 = 'C:\\Users\\synel\\Desktop\\myProjects\\Programming\\Python\\python tkinter\MedAllal\\program\\img\\10.png'  # Replace with your image path

    img1 = load_image(image_path1, 150, 110)
    img2 = load_image(image_path2, 150, 110)
    img3 = load_image(image_path3, 300, 100)

    label1 = tk.Label(header, image=img1, bd=0, highlightthickness=0)
    label1.image = img1  # Keep a reference to avoid garbage collection
    label1.place(x=40, y=0)

    label2 = tk.Label(header, image=img2, bd=0, highlightthickness=0)
    label2.image = img2  # Keep a reference to avoid garbage collection
    label2.place(x=820, y=0)

    label3 = tk.Label(header, image=img3, bd=0, highlightthickness=0)
    label3.image = img3 # Keep a reference to avoid garbage collection
    label3.place(x=350, y=10)
    
    start_header_animation(header_label, header)

a = 0

def start_part(body, width_body, height_body):
    def show_about_us():
        global a
        if a == 0:
            a = 1
            new_img_path = 'C:\\Users\\synel\\Desktop\\myProjects\\Programming\\Python\\python tkinter\\MedAllal\\program\\img\\7.png'  # Replace with your new image path
            new_img = load_image(new_img_path, 400, 400)
            image_label.config(image=new_img)
            image_label.image = new_img  # Keep a reference to avoid garbage collection
            button_frame.pack(side='left', padx=150, pady=20)
            image_label.pack(side='right', padx=20, pady=20)
        elif a == 1:
            a = 0
            new_img_path = 'C:\\Users\\synel\\Desktop\\myProjects\\Programming\\Python\\python tkinter\\MedAllal\\program\\img\\4.png'  # Replace with your new image path
            new_img = load_image(new_img_path, 400, 400)
            image_label.config(image=new_img)
            image_label.image = new_img  # Keep a reference to avoid garbage collection
            button_frame.pack(side='right', padx=150, pady=20)
            image_label.pack(side='left', padx=20, pady=20)

    def start_program():
        main_frame.pack_forget()
        new_frame.pack(fill='both', expand=True)

    # Main frame with image and buttons
    main_frame = tk.Frame(body, width=width_body, height=height_body, bg='#F1EFEF')
    main_frame.pack(fill='both', expand=True)

    image_path = 'C:\\Users\\synel\\Desktop\\myProjects\\Programming\\Python\\python tkinter\\MedAllal\\program\\img\\4.png'  # Replace with your image path
    img = load_image(image_path, 400, 400)

    image_label = tk.Label(main_frame, image=img, bg='white', bd=0, highlightthickness=0)
    image_label.image = img  # Keep a reference to avoid garbage collection
    image_label.pack(side='left', padx=20, pady=20)


    button_frame = tk.Frame(main_frame,  width=400, height=400, bg='#F1EFEF')
    button_frame.pack(side='right', padx=150, pady=20)

    # Start button with image
    start_image_path = 'C:\\Users\\synel\\Desktop\\myProjects\\Programming\\Python\\python tkinter\\MedAllal\\program\\img\\5.png'  # Replace with your image path
    start_img = load_image(start_image_path, 200, 80)
    start_button = tk.Button(button_frame, image=start_img, bg='white', bd=0, highlightthickness=0, command=start_program)
    start_button.image = start_img  # Keep a reference to avoid garbage collection
    start_button.pack(pady=20)

    # About Us button with image
    about_us_image_path = 'C:\\Users\\synel\\Desktop\\myProjects\\Programming\\Python\\python tkinter\\MedAllal\\program\\img\\6.png'  # Replace with your image path
    # about_us_image_path1 = 'C:\\Users\\synel\\Desktop\\myProjects\\Programming\\Python\\python tkinter\\MedAllal\\program\\img\\17.png'
    about_us_img = load_image(about_us_image_path, 200, 80)
    about_us_button = tk.Button(button_frame, image=about_us_img, bg='white', bd=0, highlightthickness=0, command=lambda: show_about_us())
    about_us_button.image = about_us_img  # Keep a reference to avoid garbage collection
    about_us_button.pack(pady=20)


    # New frame to be shown when "Start" is clicked
    new_frame = tk.Frame(body, width=width_body, height=height_body, bg='#F1EFEF')
    fill_new_frame(new_frame, main_frame, body, width_body, height_body)


def fill_new_frame(frame, main_frame, body, width_body, height_body):
    def return_home():
        frame.pack_forget()
        main_frame.pack(fill='both', expand=True)
    
    def step_back_p3():
        p3_frame.pack_forget()
        frame.pack(fill='both', expand=True)
    
    def step_back_ass():
        assemblage_frame.pack_forget()
        frame.pack(fill='both', expand=True)

    def display_p3():
        frame.pack_forget()
        p3_frame.pack(fill='both', expand=True)

    def display_assemblage():
        frame.pack_forget()
        assemblage_frame.pack(fill='both', expand=True)
    
    home_image_path = 'C:\\Users\\synel\\Desktop\\myProjects\\Programming\\Python\\python tkinter\\MedAllal\\program\\img\\12.png'  # Replace with your image path
    home_img = load_image(home_image_path, 30, 30)
    home_button = tk.Button(frame, image=home_img, bg='white', bd=0, highlightthickness=0, command=return_home)
    home_button.image = home_img  # Keep a reference to avoid garbage collection
    home_button.place(x=10, y=10)


    assemblage_image_path = 'C:\\Users\\synel\\Desktop\\myProjects\\Programming\\Python\\python tkinter\\MedAllal\\program\\img\\8.png'  # Replace with your image path
    assemblage_img = load_image(assemblage_image_path, 200, 80)
    assemblage_button = tk.Button(frame, image=assemblage_img, bg='white', bd=0, highlightthickness=0, command=display_assemblage)
    assemblage_button.image = assemblage_img  # Keep a reference to avoid garbage collection
    assemblage_button.place(x=650, y=60)

    assemblage_desc_image_path = 'C:\\Users\\synel\\Desktop\\myProjects\\Programming\\Python\\python tkinter\\MedAllal\\program\\img\\16.png'  # Replace with your image path
    assemblage_desc_img = load_image(assemblage_desc_image_path, 350, 300)
    assemblage_desc_button = tk.Button(frame, image=assemblage_desc_img, bg='white', bd=0, highlightthickness=0)
    assemblage_desc_button.image = assemblage_desc_img  # Keep a reference to avoid garbage collection
    assemblage_desc_button.place(x=560, y=140)

    p3_image_path = 'C:\\Users\\synel\\Desktop\\myProjects\\Programming\\Python\\python tkinter\\MedAllal\\program\\img\\9.png'  # Replace with your image path
    p3_img = load_image(p3_image_path, 200, 80)
    p3_button = tk.Button(frame, image=p3_img, bg='white', bd=0, highlightthickness=0, command=display_p3)
    p3_button.image = p3_img  # Keep a reference to avoid garbage collection
    # p3_button.pack(side='left', padx=20, pady=20)
    p3_button.place(x=150, y=60)

    p3_desc_image_path = 'C:\\Users\\synel\\Desktop\\myProjects\\Programming\\Python\\python tkinter\\MedAllal\\program\\img\\16.png'  # Replace with your image path
    p3_desc_img = load_image(p3_desc_image_path, 350, 300)
    p3_desc_button = tk.Button(frame, image=p3_desc_img, bg='white', bd=0, highlightthickness=0)
    p3_desc_button.image = p3_desc_img  # Keep a reference to avoid garbage collection
    p3_desc_button.place(x=70, y=140)

    # # New frame to be shown when "Start" is clicked
    p3_frame = tk.Frame(body, width=width_body, height=height_body, bg='#F1EFEF')
    p3_frame_fun(p3_frame, frame, width_body, height_body) 

    assemblage_frame = tk.Frame(body, width=width_body, height=height_body, bg='#F1EFEF')
    assemblage_frame_fun(assemblage_frame, frame, width_body, height_body) 
    


