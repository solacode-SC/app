from functions import *
from frames import *
import tkinter as tk
from PIL import Image, ImageTk


def p3_frame_fun(p3_frame, main_frame, width_body, height_body):
    def return_home():
        p3_frame.pack_forget()
        main_frame.pack(fill='both', expand=True)

    def change_ass_r(r_num):
        if r_num == 1:
            p3_r2_frame.pack_forget()
            p3_r3_frame.pack_forget()
            p3_r1_frame.pack(fill='both', expand=True)
        elif r_num == 2:
            p3_r1_frame.pack_forget()
            p3_r3_frame.pack_forget()
            p3_r2_frame.pack(fill='both', expand=True)
        elif r_num == 3:
            p3_r1_frame.pack_forget()
            p3_r2_frame.pack_forget()
            p3_r3_frame.pack(fill='both', expand=True)


    home_image_path = 'C:\\Users\\synel\\Desktop\\myProjects\\Programming\\Python\\python tkinter\\MedAllal\\program\\img\\12.png'  # Replace with your image path
    home_img = load_image(home_image_path, 30, 30)
    home_button = tk.Button(p3_frame, image=home_img, bg='white', bd=0, highlightthickness=0, command=return_home)
    home_button.image = home_img  # Keep a reference to avoid garbage collection
    home_button.place(x=10, y=10)
    # Main frame with image and buttons
    left_frame = tk.Frame(p3_frame, width=width_body * 0.3, height=height_body - 50, bg='#F1EFEF')

    p3_r1_image_path = 'C:\\Users\\synel\\Desktop\\myProjects\\Programming\\Python\\python tkinter\\MedAllal\\program\\img\\31.png'  # Replace with your image path
    p3_r1_img = load_image(p3_r1_image_path, 200, 80)
    p3_r1_button = tk.Button(left_frame, image=p3_r1_img, bg='white', bd=0, highlightthickness=0, cursor="hand2", command=lambda: change_ass_r(1))
    p3_r1_button.image = p3_r1_img  # Keep a reference to avoid garbage collection
    # p3_button.pack(side='left', padx=20, pady=20)
    p3_r1_button.place(x=40, y=10)

    p3_r2_image_path = 'C:\\Users\\synel\\Desktop\\myProjects\\Programming\\Python\\python tkinter\\MedAllal\\program\\img\\34.png'  # Replace with your image path
    p3_r2_img = load_image(p3_r2_image_path, 200, 80)
    p3_r2_button = tk.Button(left_frame, image=p3_r2_img, bg='white', bd=0, highlightthickness=0, cursor= "hand2", command=lambda: change_ass_r(2))
    p3_r2_button.image = p3_r2_img  # Keep a reference to avoid garbage collection
    # p3_button.pack(side='left', padx=20, pady=20)
    p3_r2_button.place(x=40, y=90)

    p3_r3_image_path = 'C:\\Users\\synel\\Desktop\\myProjects\\Programming\\Python\\python tkinter\\MedAllal\\program\\img\\35.png'  # Replace with your image path
    p3_r3_img = load_image(p3_r3_image_path, 200, 80)
    p3_r3_button = tk.Button(left_frame, image=p3_r3_img, bg='white', bd=0, highlightthickness=0, cursor= "hand2", command=lambda: change_ass_r(3))
    p3_r3_button.image = p3_r3_img  # Keep a reference to avoid garbage collection
    # p3_button.pack(side='left', padx=20, pady=20)
    p3_r3_button.place(x=40, y=170)

    left_frame.place(x=0, y=50)

    right_frame = tk.Frame(p3_frame, width=width_body * 0.7 - 10, height=height_body, bg='#F1EFEF')
    
    p3_r3_frame = tk.Frame(right_frame, width=width_body * 0.7 - 10, height=height_body, bg='#F1EFEF')
    
    image_path1 = 'C:\\Users\\synel\\Desktop\\myProjects\\Programming\\Python\\python tkinter\MedAllal\\program\\img\\30.png'  # Replace with your image path

    img1 = load_image(image_path1, 670, 170)

    label1 = tk.Label(p3_r3_frame, image=img1, bd=0, highlightthickness=0)
    label1.image = img1  # Keep a reference to avoid garbage collection
    label1.place(x=0, y=0)

    image_path2 = 'C:\\Users\\synel\\Desktop\\myProjects\\Programming\\Python\\python tkinter\MedAllal\\program\\img\\ss.png'  # Replace with your image path

    img2 = load_image(image_path2, 250, 180)

    label2 = tk.Label(p3_r3_frame, image=img2, bd=0, highlightthickness=0)
    label2.image = img2  # Keep a reference to avoid garbage collection
    label2.place(x=180, y=180)


    p3_r1_btn_path = 'C:\\Users\\synel\\Desktop\\myProjects\\Programming\\Python\\python tkinter\\MedAllal\\program\\img\\check1.png'  # Replace with your image path
    p3_r1_btn_img = load_image(p3_r1_btn_path, 200, 80)
    p3_r1_btn = tk.Button(p3_r3_frame, image=p3_r1_btn_img, bg='white', bd=0, highlightthickness=0, cursor= "hand2", command=lambda: change_ass_r(3))
    p3_r1_btn.image = p3_r1_btn_img  # Keep a reference to avoid garbage collection
    # p3_button.pack(side='left', padx=20, pady=20)
    p3_r1_btn.place(x=0, y=370)

    image_path4 = 'C:\\Users\\synel\\Desktop\\myProjects\\Programming\\Python\\python tkinter\MedAllal\\program\\img\\passwd.png'  # Replace with your image path

    img4 = load_image(image_path4, 200, 80)

    label4 = tk.Label(p3_r3_frame, image=img4, bd=0, highlightthickness=0)
    label4.image = img4  # Keep a reference to avoid garbage collection
    label4.place(x=400, y=370)


    p3_r3_frame.place(x=1, y=0)

    p3_r2_frame = tk.Frame(right_frame, width=width_body * 0.7 - 10, height=height_body, bg='#F1EFEF')
    
    image_path1 = 'C:\\Users\\synel\\Desktop\\myProjects\\Programming\\Python\\python tkinter\MedAllal\\program\\img\\33.png'  # Replace with your image path

    img1 = load_image(image_path1, 670, 170)

    label1 = tk.Label(p3_r2_frame, image=img1, bd=0, highlightthickness=0)
    label1.image = img1  # Keep a reference to avoid garbage collection
    label1.place(x=0, y=0)

    image_path2 = 'C:\\Users\\synel\\Desktop\\myProjects\\Programming\\Python\\python tkinter\MedAllal\\program\\img\\33.png'  # Replace with your image path

    img2 = load_image(image_path2, 670, 170)

    label2 = tk.Label(p3_r2_frame, image=img2, bd=0, highlightthickness=0)
    label2.image = img2  # Keep a reference to avoid garbage collection
    label2.place(x=100, y=900)

    image_path2 = 'C:\\Users\\synel\\Desktop\\myProjects\\Programming\\Python\\python tkinter\MedAllal\\program\\img\\ss.png'  # Replace with your image path

    img2 = load_image(image_path2, 250, 180)

    label2 = tk.Label(p3_r2_frame, image=img2, bd=0, highlightthickness=0)
    label2.image = img2  # Keep a reference to avoid garbage collection
    label2.place(x=180, y=180)


    p3_r1_btn_path = 'C:\\Users\\synel\\Desktop\\myProjects\\Programming\\Python\\python tkinter\\MedAllal\\program\\img\\check1.png'  # Replace with your image path
    p3_r1_btn_img = load_image(p3_r1_btn_path, 200, 80)
    p3_r1_btn = tk.Button(p3_r2_frame, image=p3_r1_btn_img, bg='white', bd=0, highlightthickness=0, cursor= "hand2", command=lambda: change_ass_r(3))
    p3_r1_btn.image = p3_r1_btn_img  # Keep a reference to avoid garbage collection
    # p3_button.pack(side='left', padx=20, pady=20)
    p3_r1_btn.place(x=0, y=370)

    image_path4 = 'C:\\Users\\synel\\Desktop\\myProjects\\Programming\\Python\\python tkinter\MedAllal\\program\\img\\passwd.png'  # Replace with your image path

    img4 = load_image(image_path4, 200, 80)

    label4 = tk.Label(p3_r2_frame, image=img4, bd=0, highlightthickness=0)
    label4.image = img4  # Keep a reference to avoid garbage collection
    label4.place(x=400, y=370)


    p3_r2_frame.place(x=1, y=0)

    p3_r1_frame = tk.Frame(right_frame, width=width_body * 0.7 - 10, height=height_body, bg='#F1EFEF')
    
    image_path1 = 'C:\\Users\\synel\\Desktop\\myProjects\\Programming\\Python\\python tkinter\MedAllal\\program\\img\\30.png'  # Replace with your image path

    img1 = load_image(image_path1, 670, 170)

    label1 = tk.Label(p3_r1_frame, image=img1, bd=0, highlightthickness=0)
    label1.image = img1  # Keep a reference to avoid garbage collection
    label1.place(x=0, y=0)

    image_path2 = 'C:\\Users\\synel\\Desktop\\myProjects\\Programming\\Python\\python tkinter\MedAllal\\program\\img\\36.png'  # Replace with your image path

    img2 = load_image(image_path2, 250, 200)

    label2 = tk.Label(p3_r1_frame, image=img2, bd=0, highlightthickness=0)
    label2.image = img2  # Keep a reference to avoid garbage collection
    label2.place(x=0, y=160)

    image_path3 = 'C:\\Users\\synel\\Desktop\\myProjects\\Programming\\Python\\python tkinter\MedAllal\\program\\img\\37.png'  # Replace with your image path

    img3 = load_image(image_path3, 250, 200)

    label3 = tk.Label(p3_r1_frame, image=img3, bd=0, highlightthickness=0)
    label3.image = img3  # Keep a reference to avoid garbage collection
    label3.place(x=400, y=160)

    p3_r1_btn_path = 'C:\\Users\\synel\\Desktop\\myProjects\\Programming\\Python\\python tkinter\\MedAllal\\program\\img\\check1.png'  # Replace with your image path
    p3_r1_btn_img = load_image(p3_r1_btn_path, 200, 80)
    p3_r1_btn = tk.Button(p3_r1_frame, image=p3_r1_btn_img, bg='white', bd=0, highlightthickness=0, cursor= "hand2", command=lambda: change_ass_r(3))
    p3_r1_btn.image = p3_r1_btn_img  # Keep a reference to avoid garbage collection
    # p3_button.pack(side='left', padx=20, pady=20)
    p3_r1_btn.place(x=0, y=370)

    image_path4 = 'C:\\Users\\synel\\Desktop\\myProjects\\Programming\\Python\\python tkinter\MedAllal\\program\\img\\passwd.png'  # Replace with your image path

    img4 = load_image(image_path4, 200, 80)

    label4 = tk.Label(p3_r1_frame, image=img4, bd=0, highlightthickness=0)
    label4.image = img4  # Keep a reference to avoid garbage collection
    label4.place(x=400, y=370)

    p3_r1_frame.place(x=1, y=0)


    right_frame.place(x=width_body * 0.3 + 10, y=0)








