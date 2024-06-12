from tkinter import *
from PIL import Image, ImageTk
from tkinter.ttk import Combobox
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
BACKGROUND_COLOR = "#63C5DA" # Light Blue color
FRAME_BG_COLOR = "#62a7ff" # Medium Blue color
FRAME_FG_COLOR = "#fefbfb" # White with a hint of Red and green
ENTRY_BG_COLOR = "#0e5363" # Dark teal with a mix of blue and green
ENTRY_FG_COLOR = "white" 
LABEL_BG_COLOR = "#FF7F7F" # Light red or salmon color
LABEL_FG_COLOR = FRAME_FG_COLOR
RADIO_BG_COLOR = "#228B22"


# Create the main window
root = Tk()
root.title("Heart Attack Prediction System")
root.geometry("1400x730+60+80")
root.resizable(False, False)
root.config(bg=BACKGROUND_COLOR)

# Set the icon of tkinter as heart
icon_path = "spirit_love_like_valentine_romance_soul_heart_game_icon_262424.ico"
root.iconbitmap(icon_path)

# This is used for loading and placing images for header
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

header_images = ["Images/Header1.png", "Images/Header2.png", "Images/Header3.png"]
x_offset = 0
labels = []

for img_path in header_images:
    label = load_and_place_image(img_path, x=x_offset, y=0, bg_color=BACKGROUND_COLOR)
    if label:
        labels.append(label)
        x_offset += label.image.width()

# Frame 3
heading_entry = Frame(root, width=650, height=180, bg="#B9BBB6") # Light grey with subtle green
heading_entry.place(x=0, y=200)

# This creates label for all the four entry fields
def create_label(master, text, x, y):
    return Label(master, text=text, font="arial 13", bg=LABEL_BG_COLOR, fg=LABEL_FG_COLOR).place(x=x, y=y)

create_label(heading_entry, "Registration Number", 25, 10)
create_label(heading_entry, "Today's Date", 350, 10)
create_label(heading_entry, "Patient Name", 25, 90)
create_label(heading_entry, "Birth Year", 350, 90)

entry_images = [PhotoImage(file="Images/Rectangle1.png"), PhotoImage(file="Images/Rectangle2.png")]
entry_positions = [(25, 40), (25, 120), (350, 40), (350, 120)]

for img, (x, y) in zip(entry_images*2, entry_positions):
    Label(heading_entry, image=img, bg="#B9BBB6").place(x=x, y=y)

# Entry field for Registration number
registration = IntVar()
reg_entry = Entry(heading_entry, textvariable=registration, width=20, font="arial 15", bg=ENTRY_BG_COLOR, fg=ENTRY_FG_COLOR, bd=0)
reg_entry.place(x=31, y=49)

# Entry field for Current date
Date = StringVar()
today = date.today()
Date.set(today.strftime("%d/%m/%Y"))
date_entry = Entry(heading_entry, textvariable=Date, width=15, font='arial 15', bg=ENTRY_BG_COLOR, fg=ENTRY_FG_COLOR, bd=0)
date_entry.place(x=360, y=49)

# Entry field for Name
name = StringVar()
name_entry = Entry(heading_entry, textvariable=name, width=21, font="arial 16", bg="#ededed", fg="#222222", bd=0)
name_entry.place(x=31, y=128)

# Entry field for Date of Birth
DOB = IntVar()
dob_entry = Entry(heading_entry, textvariable=DOB, width=18, font="arial 16", bg="#ededed", fg="#222222", bd=0)
dob_entry.place(x=360, y=130)

######################################### body for all the personal health details ##################
detail_entry = Frame(root, width=500, height=260, bg="#EC9706")
detail_entry.place(x=30, y=420)

# Creating the entry for Radio buttons
Label(detail_entry,text='Gender:', font='arial 13', bg=RADIO_BG_COLOR,fg=FRAME_FG_COLOR).place(x=10,y=10)
Label(detail_entry,text='Fbs:', font='arial 13', bg=RADIO_BG_COLOR,fg=FRAME_FG_COLOR).place(x=200,y=10)
Label(detail_entry,text='Exang:', font='arial 13', bg=RADIO_BG_COLOR,fg=FRAME_FG_COLOR).place(x=350,y=10)

# Stores the selected gender
def selection():
    if gender.get()==1:
        GENDER = 1
        return(GENDER)
    elif gender.get()==2:
        GENDER = 2
        return(GENDER)
    else:
        print(GENDER)

# Stores the result of fbs
def selection2():
    if fbs.get()==1:
        Fbs = 1
        return(Fbs)
    elif Fbs.get()==2:
        Fbs = 2
        return(Fbs)
    else:
        print(Fbs)

# Stores if Exang is there or not
def selection3():
    if exang.get()==1:
        Exang = 1
        return(Exang)
    elif Exang.get()==2:
        Exang = 2
        return(Exang)
    else:
        print(Exang)


# Gender radio button
gender = IntVar()
R1_button = Radiobutton(detail_entry, text='Male', variable = gender, value= 1, command= selection)
R2_button = Radiobutton(detail_entry, text='Female', variable = gender, value= 2, command= selection)
R1_button.place(x=75, y=10)
R2_button.place(x=125, y=10)

# Fbs radio button
fbs = IntVar()
R3_button = Radiobutton(detail_entry, text='True', variable = fbs, value= 1, command= selection2)
R4_button = Radiobutton(detail_entry, text='False', variable = fbs, value= 2, command= selection2)
R3_button.place(x=238, y=10)
R4_button.place(x=285, y=10)

# Exang radio button
exang = IntVar()
R5_button = Radiobutton(detail_entry, text='Yes', variable = exang, value= 1, command= selection3)
R6_button = Radiobutton(detail_entry, text='No', variable = exang, value= 2, command= selection3)
R5_button.place(x=405, y=10)
R6_button.place(x=445, y=10)

############# Combo box
Label(detail_entry, text='cp:', font='arial 13', bg= RADIO_BG_COLOR, fg=FRAME_FG_COLOR).place(x=10, y=50)
Label(detail_entry, text='restecg:', font='arial 13', bg= RADIO_BG_COLOR, fg=FRAME_FG_COLOR).place(x=10, y=90)
Label(detail_entry, text='slope:', font='arial 13', bg= RADIO_BG_COLOR, fg=FRAME_FG_COLOR).place(x=10, y=130)
Label(detail_entry, text='ca:', font='arial 13', bg= RADIO_BG_COLOR, fg=FRAME_FG_COLOR).place(x=10, y=170)
Label(detail_entry, text='thal:', font='arial 13', bg= RADIO_BG_COLOR, fg=FRAME_FG_COLOR).place(x=10, y=210)

# This is to get the condition of cp
def selection4():
    input = cp_combobox.get()
    if input=="0 = typical angina":
        return(0)
    elif input=="1 = atypical angina":
        return(1)
    elif input=="2 = non-anginal pain":
        return(2)
    elif input=="3 = asymptomatic":
        return(3)
    else:
        print(Exang)

# This is to get the condition of slope
def selection5():
    input = slope_combobox.get()
    if input=="0 = upsloping":
        return(0)
    elif input=="1 = flat":
        return(1)
    elif input=="2 = downsloping":
        return(2)
    else:
        print(Exang)

# These are all the detailed options in each of the combo boxes
cp_combobox = Combobox(detail_entry, values=['0 = typical angina', '1 = atypical angina', '2 = non-anginal pain', '3 = asymptomatic'], font= 'arial 12' , state='r', width=15)
restecg_combobox = Combobox(detail_entry, values=['0', '1', '2'], font= 'arial 12' , state='r', width=11)
slope_combobox = Combobox(detail_entry, values=['0 = upsloping', '1 = flat', '2 = downsloping'], font= 'arial 12' , state='r', width=13)
ca_combobox = Combobox(detail_entry, values=['0','1','2','3','4'], font= 'arial 12' , state='r', width=15)
thal_combobox = Combobox(detail_entry, values=['0','1','2','3'], font= 'arial 12' , state='r', width=14)

cp_combobox.place(x=50, y=50)
restecg_combobox.place(x=85, y=90)
slope_combobox.place(x=70, y=130)
ca_combobox.place(x=50, y=170)
thal_combobox.place(x=58, y=210)


############################# Data Entry Box ###########

Label(detail_entry, text='Smoking:', font='arial 13', width=7, bg= "#EC9706", fg='black').place(x=240, y=50)
Label(detail_entry, text='trestbps:', font='arial 13', width=7, bg= RADIO_BG_COLOR, fg=FRAME_FG_COLOR).place(x=240, y=90)
Label(detail_entry, text='chol:', font='arial 13', width=7, bg= RADIO_BG_COLOR, fg=FRAME_FG_COLOR).place(x=240, y=130)
Label(detail_entry, text='thalach:', font='arial 13', width=7, bg= RADIO_BG_COLOR, fg=FRAME_FG_COLOR).place(x=240, y=170)
Label(detail_entry, text='oldpeak:', font='arial 13', width=7, bg= RADIO_BG_COLOR, fg=FRAME_FG_COLOR).place(x=240, y=210)


trestbps = StringVar()
chol = StringVar()
thalach = StringVar()
oldpeak = StringVar()

trestbps_entry = Entry(detail_entry, textvariable=trestbps, width=15, font='arial 15', bg='#ededed', fg='#222222', bd=0)
chol_entry = Entry(detail_entry, textvariable=chol, width=15, font='arial 15', bg='#ededed', fg='#222222', bd=0)
thalach_entry = Entry(detail_entry, textvariable=thalach, width=15, font='arial 15', bg='#ededed', fg='#222222', bd=0)
oldpeak_entry = Entry(detail_entry, textvariable=oldpeak, width=15, font='arial 15', bg='#ededed', fg='#222222', bd=0)

trestbps_entry.place(x=320, y=90)
chol_entry.place(x=320, y=130)
thalach_entry.place(x=320, y=170)
oldpeak_entry.place(x=320, y=210)

######################### Report ###############

square_report_image = PhotoImage(file="Images/Report.png")
report_background = Label(image=square_report_image, bg=BACKGROUND_COLOR)
report_background.place(x=1140, y=340)

report = Label(root, font='arial 25 bold', bg='white', fg='#8dc63f')
report.place(x=1190, y=550)

report1 = Label(root, font='arial 10 bold', bg='white')
report1.place(x=1150, y=610)

#################################################


######################### Graph ###############
graph_image = PhotoImage(file='Images/graph.png')
Label(image=graph_image).place(x=675, y=220)
Label(image=graph_image).place(x=920, y=220)
Label(image=graph_image).place(x=675, y=450)
Label(image=graph_image).place(x=920, y=450)

root.mainloop()
