from functions import *
from frames import *
import tkinter as tk
from PIL import Image, ImageTk


def assemblage_frame_fun(assemblage_frame, main_frame, width_body, height_body):
    def return_home():
        assemblage_frame.pack_forget()
        main_frame.pack(fill='both', expand=True)

    def change_ass_r(r_num):
        if r_num == 1:
            p3_r2_frame.pack_forget()
            p3_r1_frame.pack(fill='both', expand=True)
        elif r_num == 2:
            p3_r1_frame.pack_forget()
            p3_r2_frame.pack(fill='both', expand=True)

    home_image_path = 'C:\\Users\\synel\\Desktop\\myProjects\\Programming\\Python\\python tkinter\\MedAllal\\program\\img\\12.png'  # Replace with your image path
    home_img = load_image(home_image_path, 30, 30)
    home_button = tk.Button(assemblage_frame, image=home_img, bg='white', bd=0, highlightthickness=0, command=return_home)
    home_button.image = home_img  # Keep a reference to avoid garbage collection
    home_button.place(x=10, y=10)
    # Main frame with image and buttons
    left_frame = tk.Frame(assemblage_frame, width=width_body * 0.3, height=height_body - 50, bg='#F1EFEF')

    p3_r1_image_path = 'C:\\Users\\synel\\Desktop\\myProjects\\Programming\\Python\\python tkinter\\MedAllal\\program\\img\\25.png'  # Replace with your image path
    p3_r1_img = load_image(p3_r1_image_path, 200, 80)
    p3_r1_button = tk.Button(left_frame, image=p3_r1_img, bg='white', bd=0, highlightthickness=0, cursor="hand2", command=lambda: change_ass_r(1))
    p3_r1_button.image = p3_r1_img  # Keep a reference to avoid garbage collection
    # p3_button.pack(side='left', padx=20, pady=20)
    p3_r1_button.place(x=40, y=10)

    p3_r2_image_path = 'C:\\Users\\synel\\Desktop\\myProjects\\Programming\\Python\\python tkinter\\MedAllal\\program\\img\\26.png'  # Replace with your image path
    p3_r2_img = load_image(p3_r2_image_path, 200, 80)
    p3_r2_button = tk.Button(left_frame, image=p3_r2_img, bg='white', bd=0, highlightthickness=0, cursor= "hand2", command=lambda: change_ass_r(2))
    p3_r2_button.image = p3_r2_img  # Keep a reference to avoid garbage collection
    # p3_button.pack(side='left', padx=20, pady=20)
    p3_r2_button.place(x=40, y=90)



    left_frame.place(x=0, y=50)

    right_frame = tk.Frame(assemblage_frame, width=width_body * 0.7 - 10, height=height_body, bg='#F1EFEF')

    p3_r2_frame = tk.Frame(right_frame, width=width_body * 0.7 - 10, height=height_body, bg='#F1EFEF')
    
    image_path1 = 'C:\\Users\\synel\\Desktop\\myProjects\\Programming\\Python\\python tkinter\MedAllal\\program\\img\\24.png'  # Replace with your image path

    img1 = load_image(image_path1, 670, 170)

    label1 = tk.Label(p3_r2_frame, image=img1, bd=0, highlightthickness=0)
    label1.image = img1  # Keep a reference to avoid garbage collection
    label1.place(x=0, y=0)

    image_path2 = 'C:\\Users\\synel\\Desktop\\myProjects\\Programming\\Python\\python tkinter\MedAllal\\program\\img\\dd.png'  # Replace with your image path

    img2 = load_image(image_path2, 250, 200)

    label2 = tk.Label(p3_r2_frame, image=img2, bd=0, highlightthickness=0)
    label2.image = img2  # Keep a reference to avoid garbage collection
    label2.place(x=0, y=200)

    image_path3 = 'C:\\Users\\synel\\Desktop\\myProjects\\Programming\\Python\\python tkinter\MedAllal\\program\\img\\dd.png'  # Replace with your image path

    img3 = load_image(image_path3, 250, 200)

    label3 = tk.Label(p3_r2_frame, image=img3, bd=0, highlightthickness=0)
    label3.image = img3  # Keep a reference to avoid garbage collection
    label3.place(x=400, y=200)


    p3_r2_frame.place(x=1, y=0)
    p3_r1_frame = tk.Frame(right_frame, width=width_body * 0.7 - 10, height=height_body, bg='#F1EFEF')
    
    image_path1 = 'C:\\Users\\synel\\Desktop\\myProjects\\Programming\\Python\\python tkinter\MedAllal\\program\\img\\24.png'  # Replace with your image path

    img1 = load_image(image_path1, 670, 170)

    label1 = tk.Label(p3_r1_frame, image=img1, bd=0, highlightthickness=0)
    label1.image = img1  # Keep a reference to avoid garbage collection
    label1.place(x=0, y=0)


    def update_inputs():
        if radio_var.get() == 1:  # 2toles selected
            entry3.config(state='disabled')
            entry1.config(state='normal')
            entry2.config(state='normal')
        elif radio_var.get() == 2:  # 3toles selected
            entry3.config(state='normal')
            entry1.config(state='normal')
            entry2.config(state='normal')
    def get_all_values():
        e_ref = 1.3
        if radio_var.get() == 1:  # 2toles
            e1 = float(entry1.get())
            e2 = float(entry2.get())
            if (e1 < e2 and e_ref >= e2):
                return fun_diplay(1)
            else:
                return fun_diplay(0)
        if radio_var.get() == 2:  # 2toles
            e1 = float(entry1.get())
            e2 = float(entry2.get())
            e3 = float(entry3.get())
            if (e1 < e2 and e2 < e3 and e_ref >= e2):
                return fun_diplay(1)
            else:
                return fun_diplay(0)

    def fun_diplay(a):
        if a == 0:
            print(0)
        elif a == 1:
            print(1)
    # Create radio buttons for 2toles and 3toles
    radio_var = tk.IntVar(value=1)  # Default to 2toles

    type_of_toles = tk.Label(p3_r1_frame, text="TYPES OF TOLES :", font=("Arial", 10), bg='#F1EFEF', fg='black')
    type_of_toles.place(x= 20, y=200)

    radio2 = tk.Radiobutton(p3_r1_frame, text="2 toles", variable=radio_var, value=1, command=update_inputs)
    radio2.place(x= 150, y=200)

    radio3 = tk.Radiobutton(p3_r1_frame, text="3 toles", variable=radio_var, value=2, command=update_inputs)
    radio3.place(x= 250, y=200)


    # Create three entry fields
    type_of_toles = tk.Label(p3_r1_frame, text="E1 :", font=("Arial", 10), bg='#F1EFEF', fg='black')
    type_of_toles.place(x= 20, y=240)
    entry1 = tk.Entry(p3_r1_frame)
    entry1.place(x= 150, y=240)

    type_of_toles = tk.Label(p3_r1_frame, text="E2 :", font=("Arial", 10), bg='#F1EFEF', fg='black')
    type_of_toles.place(x= 20, y=280)
    entry2 = tk.Entry(p3_r1_frame)
    entry2.place(x= 150, y=280)

    type_of_toles = tk.Label(p3_r1_frame, text="E3 :", font=("Arial", 10), bg='#F1EFEF', fg='black')
    type_of_toles.place(x= 20, y=320)
    entry3 = tk.Entry(p3_r1_frame)
    entry3.place(x= 150, y=320)
    entry3.config(state='disabled')

    # Create a submit button to get the values
    submit_btn = tk.Button(p3_r1_frame, text="Check", command=get_all_values)
    submit_btn.place(x= 150, y=360)

    p3_r1_frame.place(x=1, y=0)


    
    

    right_frame.place(x=width_body * 0.3 + 10, y=0)








