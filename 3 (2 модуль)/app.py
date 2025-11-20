import tkinter as tk
from tkinter import PhotoImage
import pygame
import os
from PIL import Image, ImageTk

class SoundsPlayer:
    def __init__(self):
        pygame.mixer.init()
        self.base_dir = os.path.dirname(os.path.abspath(__file__))

    def abs_path(self, folder, file):
        return os.path.join(self.base_dir, folder, file)

    def play(self, file):
        pygame.mixer.music.load(self.abs_path("music", file))
        pygame.mixer.music.play()

class MusicApp:
    def __init__(self):
        self.player = SoundsPlayer()
        self.root = tk.Tk()
        self.root.title("My Favorite Songs")
        self.root.geometry('750x450')
        self.root.resizable(False, False)

        self.left_frame = tk.Frame(self.root)
        self.right_frame = tk.Frame(self.root)
        self.left_frame.grid(row=0, column=0, padx=20, pady=20, sticky="n")
        self.right_frame.grid(row=0, column=1, padx=20, pady=20)

        self.right_frame.grid_columnconfigure(0, weight=1)
        self.right_frame.grid_rowconfigure(0, weight=1)

        self.image_label = tk.Label(self.right_frame)
        self.image_label.grid(row=0, column=0, pady=10)

        self.artist_label = tk.Label(self.right_frame, font=("Arial", 14, "bold"))
        self.artist_label.grid(row=1, column=0)

        self.create_buttons()

    def show_image_and_artist(self, photo_file, artist_name):
        path = self.player.abs_path("photo", photo_file)
        image = Image.open(path)
        image = image.resize((300, 300))
        img = ImageTk.PhotoImage(image)
        self.image_label.config(image=img)
        self.image_label.image = img
        self.artist_label.config(text=artist_name)

    def create_buttons(self):
        songs = [
            ("Famous", "1.mp3", "1.jpg", "All Day Project"),
            ("Cherish (My love)", "2.mp3", "2.jpeg", "Illit"),
            ("SOB", "3.mp3", "3.jpg", "Close Your Eyes"),
            ("Touch", "4.mp3", "4.png", "Katseye"),
            ("Killing it girl (solo ver.)", "5.mp3", "5.jpg", "Jhope"),
        ]

        for title, mp3, photo, artist in songs:
            tk.Button(
                self.left_frame,
                text=title,
                font=("Arial", 14),
                width=20,
                command=lambda m=mp3, p=photo, a=artist: (
                    self.player.play(m),
                    self.show_image_and_artist(p, a)
                )
            ).pack(pady=5)

    def run(self):
        self.root.mainloop()