import tkinter as tk
from tkinter import messagebox

import face_recognition
import os

def get_button(window, text, color, command, fg='white'):
    button = tk.Button(
                        window,
                        text=text,
                        activebackground="black",
                        activeforeground="white",
                        fg=fg,
                        bg=color,
                        command=command,
                        height=2,
                        width=20,
                        font=('Helvetica bold', 20)
                    )

    return button


def get_img_label(window):
    label = tk.Label(window)
    label.grid(row=0, column=0)
    return label


def get_text_label(window, text):
    label = tk.Label(window, text=text)
    label.config(font=("sans-serif", 21), justify="left")
    return label


def get_entry_text(window):
    inputtxt = tk.Text(window,
                       height=2,
                       width=15, 
                       font=("Arial", 32))
    return inputtxt


def msg_box(title, description):
    messagebox.showinfo(title, description)

def recognize(img, db_dir):
    # Encode the unknown image
    unknown_encodings = face_recognition.face_encodings(img)
    if not unknown_encodings:
        return "no_persons_found"
    unknown_encoding = unknown_encodings[0]

    # Loop through db images and compare
    for filename in os.listdir(db_dir):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            db_img_path = os.path.join(db_dir, filename)
            db_img = face_recognition.load_image_file(db_img_path)
            db_encodings = face_recognition.face_encodings(db_img)
            if db_encodings:
                match = face_recognition.compare_faces([db_encodings[0]], unknown_encoding)[0]
                if match:
                    return os.path.splitext(filename)[0]
    return "unknown_person"

