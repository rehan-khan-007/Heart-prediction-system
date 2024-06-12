from tkinter import *

# Importing necessary modules
from PIL import Image, ImageTk
from datetime import date
from tkinter.ttk import Combobox
import datetime
import tkinter as tk
from tkinter import ttk
import os

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt

# Define colors
background = "#add8e6"  # Light blue color
framebg = "#62a7ff"
framefg = "#fefbfb"

# Create the main window
root = Tk()
root.title("Heart Attack Prediction System")
root.geometry("1500x750+60+80")
root.resizable(False, False)
root.config(bg=background)

# Changed the icon of tkinter as heart 
icon_path = "spirit_love_like_valentine_romance_soul_heart_game_icon_262424.ico"
root.iconbitmap(icon_path)

#Helps in loading and placing images 
def load_and_place_image(image_path, x, y, background):
    try:
        image = Image.open(image_path)
        photo_image = ImageTk.PhotoImage(image)
        label = Label(image=photo_image, bg=background)
        label.image = photo_image
        label.place(x=x, y=y)
        #print(f"Loaded image: {image_path} at ({x}, {y})")
        return label
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

# Load and place the first image    
label1 = load_and_place_image("Images/Header1.jpg",x=0, y=0, background=background)

# Load and place the second image to the right of the first image
if label1:
    label1_width = label1.image.width()
    label2 = load_and_place_image("Images/Header2.jpg",x=label1_width, y=0, background=background)

# Load and place the third image to the right of 1st and 2nd image
if label1 and label2:
    label2_width = label2.image.width()
    label3 = load_and_place_image("Images/Header3.jpg",x=label1_width + label2_width/2, y=0, background=background)

root.mainloop()
