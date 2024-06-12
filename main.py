from tkinter import *

# Importing necessary modules
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
root.geometry("1450x730+60+80")
root.resizable(False, False)
root.config(bg=background)

# Changed the icon of tkinter as heart 
icon_path = "spirit_love_like_valentine_romance_soul_heart_game_icon_262424.ico"
root.iconbitmap(icon_path)

# Header Section 2
logo = PhotoImage(file="Images/Header1.jpg")
myimage = Label(image=logo, bg=background)
myimage.place(x=0, y=0)

root.mainloop()
