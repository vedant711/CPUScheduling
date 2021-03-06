from math import sin, cos
import subprocess
from pathlib import Path
import os

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Label, Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter.constants import ANCHOR
import webbrowser


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def callback(url):
    webbrowser.open_new_tab(url)


def one():
    file1 = "python cpuScheduling.py"
    # os.system(file1)
    p = subprocess.Popen(file1, shell=True, stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()


def two():
    file2 = "python PageReplacement.py"
    # os.system(file1)
    p = subprocess.Popen(file2, shell=True, stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()


def three():
    file3 = "python DiskScheduling.py"
    # os.system(file1)
    p = subprocess.Popen(file3, shell=True, stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()


def readme(p):
    # path = '/readme.pdf'
    # subprocess.Popen([path], shell=True)
    path_parent = os.path.dirname(os.getcwd())
    os.chdir(path_parent)
    os.system(p)


window = Tk()

window.geometry("800x596")
window.configure(bg="#FFFFFF")


canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=596,
    width=800,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_rectangle(
    0.0,
    0.0,
    400.0,
    600.0,
    fill="#FFFFFF",
    outline="")


def create_good_rectangle(canvas, x1, y1, x2, y2, feather, res=5, color='black'):
    points = []
    # top side
    points += [x1 + feather, y1,
               x2 - feather, y1]
    # top right corner
    for i in range(res):
        points += [x2 - feather + sin(i/res*2) * feather,
                   y1 + feather - cos(i/res*2) * feather]
    # right side
    points += [x2, y1 + feather,
               x2, y2 - feather]
    # bottom right corner
    for i in range(res):
        points += [x2 - feather + cos(i/res*2) * feather,
                   y2 - feather + sin(i/res*2) * feather]
    # bottom side
    points += [x2 - feather, y2,
               x1 + feather, y2]
    # bottom left corner
    for i in range(res):
        points += [x1 + feather - sin(i/res*2) * feather,
                   y2 - feather + cos(i/res*2) * feather]
    # left side
    points += [x1, y2 - feather,
               x1, y1 + feather]
    # top left corner
    for i in range(res):
        points += [x1 + feather - cos(i/res*2) * feather,
                   y1 + feather - sin(i/res*2) * feather]

    return canvas.create_polygon(points, fill=color)  # ?


bg_right = PhotoImage(file="triangle4-01.png")
# mylabel1 = Label(window, image=bg_right)
# mylabel1.place(x=400, y=0, relwidth=0.5, relheight=1)


canvas.create_rectangle(
    400.0,
    0.0,
    800.0,
    600.0,
    fill="#000000",
    outline="")

# bg_left = PhotoImage(file="triangle 2-01.png")
# mylabel = Label(window, image=bg_left)
# mylabel.place(x=0, y=0, relwidth=0.5, height="600px")

canvas.create_image(400, 0, image=bg_right, anchor='nw')
# box = Label(window, )

canvas.create_rectangle(
    281.0,
    292.0,
    360.0,
    352.0,
    fill="#ffffff",
    outline="")

canvas.create_rectangle(
    161.0,
    278.0,
    244.0,
    367.0,
    fill="#ffffff",
    outline="")

canvas.create_rectangle(
    62.0,
    300.0,
    103.0,
    345.0,
    fill="#ffffff",
    outline="")

# canvas.create_rectangle(
#     481.0,
#     158.0,
#     730.0,
#     443.0,
#     fill="#ffffff",
#     outline="")

create_good_rectangle(canvas, 481, 158, 730, 443, 15, 5, '#ffffff')


button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=506.0,
    y=383.4266662597656,
    width=201.0,
    height=42.573333740234375
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: two(),
    relief="flat"
)
button_2.place(
    x=504.0,
    y=311.9066467285156,
    width=201.0,
    height=42.093353271484375
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: three(),
    relief="flat"
)
button_3.place(
    x=504.0,
    y=241.0,
    width=202.0,
    height=42.0
)

button_image_yt = PhotoImage(
    file=relative_to_assets("y1-01.png"))
button_yt = Button(
    image=button_image_yt,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: callback('https://youtu.be/-fI59snCfAs'),
    relief="flat"
)
button_yt.place(
    x=57.0,
    y=347.0,
    width=69.0,
    height=50.0
)

button_image_gh = PhotoImage(
    file=relative_to_assets("g1-01 1.png"))
button_gh = Button(
    image=button_image_gh,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: callback("https://github.com/vedant711/CPUScheduling"),
    relief="flat"
)
button_gh.place(
    x=177.0,
    y=333.0,
    width=60.0,
    height=78.0
)

button_image_rm = PhotoImage(
    file=relative_to_assets("r1-01.png"))
button_rm = Button(
    image=button_image_rm,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: readme('readme.pdf'),
    relief="flat"
)
button_rm.place(
    x=288.0,
    y=347.0,
    width=69.0,
    height=50.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=one,
    relief="flat"
)
button_4.place(
    x=504.0,
    y=176.0,
    width=202.0,
    height=42.0
)

# canvas.create_rectangle(
#     0.0,
#     0.0,
#     410.0,
#     263.0,
#     fill="#FFFFFF",
#     outline="")


# canvas.create_text(
#     122.0,
#     210.0,
#     anchor="nw",
#     text="VIRTUAL LAB",
#     fill="#000000",
#     font=("Roboto Bold", 24 * -1)
# )

title = Label(window, text='''OPERATING SYSTEM
VIRTUAL LAB''', font=("Roboto Bold", 30 * -1), background='white')
title.place(x=50.0, y=168.0)


# canvas.create_text(
#     91.0,
#     178.0,
#     anchor="nw",
#     text="OPERATING SYSTEM",
#     fill="#000000",
#     font=("Roboto Bold", 30 * -1)
# )
window.resizable(False, False)
window.mainloop()
