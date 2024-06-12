from tkinter import *
from PIL import Image, ImageTk
from datetime import date
import tkinter as tk
import os

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt

# Define colors
BACKGROUND_COLOR = "#add8e6"
FRAME_BG_COLOR = "#62a7ff"
FRAME_FG_COLOR = "#fefbfb"
ENTRY_BG_COLOR = "#0e5363"
ENTRY_FG_COLOR = "white"
LABEL_BG_COLOR = "#FF7F7F"
LABEL_FG_COLOR = FRAME_FG_COLOR

# Create the main window
root = Tk()
root.title("Heart Attack Prediction System")
root.geometry("1400x730+60+80")
root.resizable(False, False)
root.config(bg=BACKGROUND_COLOR)

# Set the icon of tkinter as heart
icon_path = "spirit_love_like_valentine_romance_soul_heart_game_icon_262424.ico"
root.iconbitmap(icon_path)

def load_and_place_image(image_path, x, y, bg_color):
    try:
        image = Image.open(image_path)
        photo_image = ImageTk.PhotoImage(image)
        label = Label(image=photo_image, bg=bg_color)
        label.image = photo_image  # Keep a reference to avoid garbage collection
        label.place(x=x, y=y)
        return label
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

# Load and place header images
header_images = ["Images/Header1.png", "Images/Header2.png", "Images/Header3.png"]
x_offset = 0
labels = []

for img_path in header_images:
    label = load_and_place_image(img_path, x=x_offset, y=0, bg_color=BACKGROUND_COLOR)
    if label:
        labels.append(label)
        x_offset += label.image.width()

# Frame 3
heading_entry = Frame(root, width=670, height=170, bg="#B9BBB6")
heading_entry.place(x=0, y=200)

def create_label(master, text, x, y):
    return Label(master, text=text, font="arial 13", bg=LABEL_BG_COLOR, fg=LABEL_FG_COLOR).place(x=x, y=y)

create_label(heading_entry, "Registration Number", 30, 10)
create_label(heading_entry, "Today's Date", 370, 10)
create_label(heading_entry, "Patient Name", 30, 90)
create_label(heading_entry, "Birth Year", 370, 90)

entry_images = [PhotoImage(file="Images/Rectangle1.png"), PhotoImage(file="Images/Rectangle2.png")]
entry_positions = [(30, 40), (30, 120), (370, 40), (370, 120)]

for img, (x, y) in zip(entry_images*2, entry_positions):
    Label(heading_entry, image=img, bg="#B9BBB6").place(x=x, y=y)

registration = IntVar()
reg_entry = Entry(heading_entry, textvariable=registration, width=20, font="arial 15", bg=ENTRY_BG_COLOR, fg=ENTRY_FG_COLOR, bd=0)
reg_entry.place(x=36, y=49)

Date = StringVar()
today = date.today()
Date.set(today.strftime("%d/%m/%Y"))
date_entry = Entry(heading_entry, textvariable=Date, width=15, font='arial 15', bg=ENTRY_BG_COLOR, fg=ENTRY_FG_COLOR, bd=0)
date_entry.place(x=380, y=49)

name = StringVar()
name_entry = Entry(heading_entry, textvariable=name, width=21, font="arial 16", bg="#ededed", fg="#222222", bd=0)
name_entry.place(x=36, y=128)

DOB = IntVar()
dob_entry = Entry(heading_entry, textvariable=DOB, width=18, font="arial 16", bg="#ededed", fg="#222222", bd=0)
dob_entry.place(x=380, y=130)

root.mainloop()
