from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter.ttk import Combobox 
from datetime import date; import datetime
import tkinter as tk
import os

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt

from backend import load_and_prepare_data, scale_data, split_data, train_model, evaluate_model, make_prediction

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
root.geometry("1445x730+60+80")
#root.resizable(False, False)
root.config(bg=BACKGROUND_COLOR)

######### Analysis #######################
def analysis():
    name = Name.get()
    D1 = Date.get()
    today = datetime.date.today()
    A = today.year-DOB.get()

    try:
        B = selection()
    except:
        messagebox.showerror("missing", "Please select Gender!!")
        return
    
    try:
        F = selection2()
    except:
        messagebox.showerror("missing", "Please select fbs!!")
        return
    
    try:
        I = selection3()
    except:
        messagebox.showerror("missing", "Please select exang!!")
        return
    
    try:
        C = int(selection4())
    except:
        messagebox.showerror("missing", "Please select cp!!")
        return
    
    try:
        G = int(restecg_combobox.get())
    except:
        messagebox.showerror("missing", "Please select restecg!!")
        return
    
    try:
        K = int(selection5())
    except:
        messagebox.showerror("missing", "Please select slope!!")
        return
    
    try:
        L = int(ca_combobox.get())
    except:
        messagebox.showerror("missing", "Please select ca!!")
        return

    try:
        M = int(thal_combobox.get())
    except:
        messagebox.showerror("missing", "Please select thal!!")
        return
    
    try:
        D = int(trestbps.get())
        E = int(chol.get())
        H = int(thalach.get())
        J = int(oldpeak.get())
    except:
        messagebox.showerror("missing data", "Some data entries are missing!!")
        return
    
    ####### First Graph
    f = Figure(figsize=(5,5), dpi=100)
    a = f.add_subplot(111)
    a.plot(["Gender", 'fbs', 'exang'], [B, F, I], marker='o', linestyle='-')
    f.subplots_adjust(left=0.2, top=0.95, right=0.95)
    canvas = FigureCanvasTkAgg(f)
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
    canvas._tkcanvas.place(width=250, height=250, x=650, y=215)

    ####### Second Graph
    f2 = Figure(figsize=(5,5), dpi=100)
    a2 = f2.add_subplot(111)
    a2.plot(["age", 'trestbps', 'chol', 'thalach'],[A, D, E, H], marker='o', linestyle='-')
    f2.subplots_adjust(left=0.2, top=0.95, right=0.93)
    canvas2 = FigureCanvasTkAgg(f2)
    canvas2.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
    canvas2._tkcanvas.place(width=250, height=250, x=900, y=215)

    ####### Third Graph
    f3 = Figure(figsize=(5,5), dpi=100)
    a3 = f3.add_subplot(111)
    a3.plot(['oldpeak', 'restcg','cp'],[J, G, C], marker='o', linestyle='-')
    f3.subplots_adjust(left=0.2, top=0.95, right=0.95)
    canvas3 = FigureCanvasTkAgg(f3)
    canvas3.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
    canvas3._tkcanvas.place(width=250, height=250, x=650, y=465)

    ####### Fourth Graph
    f4 = Figure(figsize=(5,5), dpi=100)
    a4 = f4.add_subplot(111)
    a4.plot(['slope', 'ca', 'thal'],[K, L, M], marker='o', linestyle='-')
    f4.subplots_adjust(left=0.2, top=0.95, right=0.95)
    canvas3 = FigureCanvasTkAgg(f4)
    canvas3.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
    canvas3._tkcanvas.place(width=250, height=250, x=900, y=465)

    # Load and prepare data
    X, Y = load_and_prepare_data('heart.csv')

    # Scale data
    X_scaled, scaler = scale_data(X)

    # Split data
    X_train, X_test, Y_train, Y_test = split_data(X_scaled, Y)

    # Train model
    model = train_model(X_train, Y_train)

    # Evaluate model
    evaluate_model(model, X_train, Y_train, X_test, Y_test)

    input_data = (A, B, C, D, E, F, G, H, I, J, K, L, M)  
    feature_names = X.columns  # Use feature names from the loaded data
    prediction = make_prediction(model, scaler, input_data, feature_names)

    if prediction == 0:
        print('The Person does not have a Heart Disease')
        report.config(text=f"Report: {0}", fg='#8dc63f')
        report1.config(text=f"{name}, you don't \n have a heart disease")
    else:
        print('The Person has Heart Disease')
        report.config(text=f"Report: {1}", fg='#ed1c24')
        report1.config(text=f"{name}, you have \n a heart disease")

############### Info window (operated by info button) #############
def info():
    icon_window = Toplevel(root)
    icon_window.title('Information')
    icon_window.geometry("700x550+400+100")

    # icon image of tkinter info window
    icon_image = PhotoImage(file='Images/info.png')
    icon_window.iconphoto(False, icon_image)

    # Heading
    Label(icon_window, text="Information related to Dataset", font='Robot 19 bold').pack(padx=20,pady=20)

    # Info
    Label(icon_window, text="age :- age in years", font='arial 11').place(x=20, y=100)
    Label(icon_window, text="gender :- gender (1 = male; 0 = female)", font='arial 11').place(x=20, y=130)
    Label(icon_window, text="cp :- chest pain type (0 = typical angina; 1 = atypical angina; 2 = non-anginal pain; 3 = asymptomatic)", font='arial 11').place(x=20, y=160)
    Label(icon_window, text="trestbps :- resting blood pressure (in mm Hg on admission to the hospital)", font='arial 11').place(x=20, y=190)
    Label(icon_window, text="chol :- serum cholesterol in mg/dl", font='arial 11').place(x=20, y=220)
    Label(icon_window, text="fbs :- fasting blood sugar > 120 mg/dl (1 = true; 0 = false)", font='arial 11').place(x=20, y=250)
    Label(icon_window, text="restecg :- resting electrocardiographic results (0 = normal; 1 = having ST-T; 2 = hypertrophy)", font='arial 11').place(x=20, y=280)
    Label(icon_window, text="thalach :- maximum heart rate achieved", font='arial 11').place(x=20, y=310)
    Label(icon_window, text="exang :- exercise induced angina (1 = yes; 0 = no)", font='arial 11').place(x=20, y=340)
    Label(icon_window, text="oldpeak :- ST depression induced by exercise relative to rest", font='arial 11').place(x=20, y=370)
    Label(icon_window, text="slope :- the slope of the peak exercise ST segment (0 = upsloping; 1 = flat; 2 = downsloping)", font='arial 11').place(x=20, y=400)
    Label(icon_window, text="ca :- number of major vessels (0-3) colored by flourosopy", font='arial 11').place(x=20, y=430)
    Label(icon_window, text="thal :- 0 = normal; 1 = fixed defect; 2 = reversable defect", font='arial 11').place(x=20, y=460)

    icon_window.mainloop()

# This is used for logging out a user and closing window
def logout():
    root.destroy()

#### It is used to clear the entry fields all at once
def clear():
    Name.get("")
    DOB.get("")
    trestbps.get("")
    chol.get("")
    thalach.set('')
    oldpeak.set('')

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

Entry_image=PhotoImage(file="Images/Rectangle1.png")
Entry_image2=PhotoImage(file="Images/Rectangle2.png")
Label(heading_entry,image=Entry_image,bg="#B9BBB6").place(x=25,y=40)
Label(heading_entry,image=Entry_image,bg="#B9BBB6").place(x=350,y=40)
Label(heading_entry,image=Entry_image2,bg="#B9BBB6").place(x=25,y=120)
Label(heading_entry,image=Entry_image2,bg="#B9BBB6").place(x=350,y=120)

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
Name = StringVar()
name_entry = Entry(heading_entry, textvariable=Name, width=21, font="arial 16", bg="#ededed", fg="#222222", bd=0)
name_entry.place(x=31, y=128)

# Entry field for Date of Birth
DOB = IntVar()
dob_entry = Entry(heading_entry, textvariable=DOB, width=18, font="arial 16", bg="#ededed", fg="#222222", bd=0)
dob_entry.place(x=360, y=130)

######################################### Body for all the personal health details ##################

detail_entry = Frame(root, width=540, height=260, bg="#EC9706")
detail_entry.place(x=60, y=420)

# Creating the entry for Radio buttons
Label(detail_entry,text='Gender:', font='arial 13', bg=RADIO_BG_COLOR,fg=FRAME_FG_COLOR).place(x=30,y=10)
Label(detail_entry,text='Fbs:', font='arial 13', bg=RADIO_BG_COLOR,fg=FRAME_FG_COLOR).place(x=220,y=10)
Label(detail_entry,text='Exang:', font='arial 13', bg=RADIO_BG_COLOR,fg=FRAME_FG_COLOR).place(x=370,y=10)

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
    elif fbs.get()==2:
        Fbs = 2
        return(Fbs)

# Stores if Exang is there or not
def selection3():
    if exang.get()==1:
        Exang = 1
        return(Exang)
    elif exang.get()==2:
        Exang = 2
        return(Exang)

# Gender radio button
gender = IntVar()
R1_button = Radiobutton(detail_entry, text='Male', variable = gender, value= 1, command= selection)
R2_button = Radiobutton(detail_entry, text='Female', variable = gender, value= 2, command= selection)
R1_button.place(x=95, y=10)
R2_button.place(x=145, y=10)

# Fbs radio button
fbs = IntVar()
R3_button = Radiobutton(detail_entry, text='True', variable = fbs, value= 1, command= selection2)
R4_button = Radiobutton(detail_entry, text='False', variable = fbs, value= 2, command= selection2)
R3_button.place(x=258, y=10)
R4_button.place(x=305, y=10)

# Exang radio button
exang = IntVar()
R5_button = Radiobutton(detail_entry, text='Yes', variable = exang, value= 1, command= selection3)
R6_button = Radiobutton(detail_entry, text='No', variable = exang, value= 2, command= selection3)
R5_button.place(x=425, y=10)
R6_button.place(x=465, y=10)

############# Combo box ############################
Label(detail_entry, text='cp:', font='arial 13', bg= RADIO_BG_COLOR, fg=FRAME_FG_COLOR).place(x=30, y=50)
Label(detail_entry, text='restecg:', font='arial 13', bg= RADIO_BG_COLOR, fg=FRAME_FG_COLOR).place(x=30, y=90)
Label(detail_entry, text='slope:', font='arial 13', bg= RADIO_BG_COLOR, fg=FRAME_FG_COLOR).place(x=30, y=130)
Label(detail_entry, text='ca:', font='arial 13', bg= RADIO_BG_COLOR, fg=FRAME_FG_COLOR).place(x=30, y=170)
Label(detail_entry, text='thal:', font='arial 13', bg= RADIO_BG_COLOR, fg=FRAME_FG_COLOR).place(x=30, y=210)

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

# This is to get the condition of slope
def selection5():
    input = slope_combobox.get()
    if input=="0 = upsloping":
        return(0)
    elif input=="1 = flat":
        return(1)
    elif input=="2 = downsloping":
        return(2)


# These are all the detailed options in each of the combo boxes
cp_combobox = Combobox(detail_entry, values=['0 = typical angina', '1 = atypical angina', '2 = non-anginal pain', '3 = asymptomatic'], font= 'arial 12' , state='r', width=15)
restecg_combobox = Combobox(detail_entry, values=['0', '1', '2'], font= 'arial 12' , state='r', width=11)
slope_combobox = Combobox(detail_entry, values=['0 = upsloping', '1 = flat', '2 = downsloping'], font= 'arial 12' , state='r', width=13)
ca_combobox = Combobox(detail_entry, values=['0','1','2','3','4'], font= 'arial 12' , state='r', width=15)
thal_combobox = Combobox(detail_entry, values=['0','1','2','3'], font= 'arial 12' , state='r', width=14)

cp_combobox.place(x=70, y=50)
restecg_combobox.place(x=105, y=90)
slope_combobox.place(x=90, y=130)
ca_combobox.place(x=70, y=170)
thal_combobox.place(x=78, y=210)

############################# Data Entry Box ###########

Label(detail_entry, text='Smoking:', font='arial 13', width=7, bg= "#EC9706", fg='black').place(x=260, y=50)
Label(detail_entry, text='trestbps:', font='arial 13', width=7, bg= RADIO_BG_COLOR, fg=FRAME_FG_COLOR).place(x=260, y=90)
Label(detail_entry, text='chol:', font='arial 13', width=7, bg= RADIO_BG_COLOR, fg=FRAME_FG_COLOR).place(x=260, y=130)
Label(detail_entry, text='thalach:', font='arial 13', width=7, bg= RADIO_BG_COLOR, fg=FRAME_FG_COLOR).place(x=260, y=170)
Label(detail_entry, text='oldpeak:', font='arial 13', width=7, bg= RADIO_BG_COLOR, fg=FRAME_FG_COLOR).place(x=260, y=210)

trestbps = StringVar()
chol = StringVar()
thalach = StringVar()
oldpeak = StringVar()

trestbps_entry = Entry(detail_entry, textvariable=trestbps, width=15, font='arial 15', bg='#ededed', fg='#222222', bd=0)
chol_entry = Entry(detail_entry, textvariable=chol, width=15, font='arial 15', bg='#ededed', fg='#222222', bd=0)
thalach_entry = Entry(detail_entry, textvariable=thalach, width=15, font='arial 15', bg='#ededed', fg='#222222', bd=0)
oldpeak_entry = Entry(detail_entry, textvariable=oldpeak, width=15, font='arial 15', bg='#ededed', fg='#222222', bd=0)

trestbps_entry.place(x=340, y=90)
chol_entry.place(x=340, y=130)
thalach_entry.place(x=340, y=170)
oldpeak_entry.place(x=340, y=210)

######################### Report ###############

square_report_image = PhotoImage(file="Images/Report.png")
report_background = Label(image=square_report_image, bg=BACKGROUND_COLOR)
report_background.place(x=1160, y=340)

report = Label(root, font='arial 25 bold', bg='white', fg='#8dc63f')
report.place(x=1195, y=550)

report1 = Label(root, font='arial 10 bold', bg='white')
report1.place(x=1195, y=610)

######################### Graph ###############
graph_image = PhotoImage(file='Images/graph.png')
Label(image=graph_image).place(x=675, y=220)
Label(image=graph_image).place(x=920, y=220)
Label(image=graph_image).place(x=675, y=450)
Label(image=graph_image).place(x=920, y=450)

######################## Analysis Button ##########
analysis_button = PhotoImage(file="Images/analysis1.png")
Button(root, image= analysis_button, bd=0, bg='black', cursor='hand2', command=analysis).place(x=1160,y=220)

######################## Info Button ##############
info_button = PhotoImage(file="Images/info1.png")
Button(root, image= info_button, bd=0, bg=BACKGROUND_COLOR, cursor='hand2', command=info).place(x=0,y=380)    

######################## Save Button ##############
save_button = PhotoImage(file="Images/save1.png")
Button(root, image= save_button, bd=0, bg='black', cursor='hand2').place(x=1330,y=280)    

#################### Smoking and Non-Smoking Button ###############
button_mode = True
choice = 'smoking'
def change_mode():
    global button_mode
    global choice

    if button_mode:
        choice = 'non-smoking'
        mode.config(image=non_smoking_icon, activebackground='white')
        button_mode = False
    else:
        choice = 'smoking'
        mode.config(image=smoking_icon, activebackground='white')
        button_mode = True

smoking_icon = PhotoImage(file="Images/smoker.png")
non_smoking_icon = PhotoImage(file="Images/non-smoker.png")

mode = Button(root, image=smoking_icon, bg = '#dbe0e3', bd=0, cursor='hand2', command=change_mode)
mode.place(x=400, y=465)

################ Log Out Button ############

logout_icon = PhotoImage(file='Images/logout1.png')
logout_button = Button(root, image=logout_icon, bg='black', cursor='hand2', bd=0, command=logout)
logout_button.place(x=1330, y=210)

root.mainloop()