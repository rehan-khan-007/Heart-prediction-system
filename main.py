from tkinter import *
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


background = "#f0ddd5"
framebg = "#62a7ff"
framefg = "#fefbfb"

root = Tk()
root.title("Heart Attack Prediction System")
root.geometry("1450x730+60+80")
root.resizable(False,False)
root.config(bg=background)

root.mainloop()
