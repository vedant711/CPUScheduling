from pathlib import Path
import subprocess
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def back():
    window.destroy()


def first():
    file1 = "python fcfs.py"
    # os.system(file1)
    p = subprocess.Popen(file1, shell=True, stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()


def second():
    file1 = "python sjf.py"
    # os.system(file1)
    p = subprocess.Popen(file1, shell=True, stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()


def third():  # function to hrrn desktop
    file1 = "python hrrn.py"
    # os.system(file1)
    p = subprocess.Popen(file1, shell=True, stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()


def fourth():  # function to hrrn desktop
    file1 = "python rr.py"
    # os.system(file1)
    p = subprocess.Popen(file1, shell=True, stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()


def fifth():
    file1 = "python ljf.py"
    # os.system(file1)
    p = subprocess.Popen(file1, shell=True, stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()


def comp():
    file = 'python comp.py'
    p = subprocess.Popen(file, shell=True, stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()


window = Tk()

window.geometry("800x600")
window.configure(bg="#FFFFFF")


canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=600,
    width=800,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_rectangle(
    0.0,
    0.0,
    800.0,
    85.0,
    fill="#00071D",
    outline="")

canvas.create_text(
    250.0,
    20.0,
    anchor="nw",
    text="CPU SCHEDULING",
    fill="#FFFFFF",
    font=("Exo SemiBoldItalic", 36 * -1)
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=back,
    relief="flat"
)
button_10.place(
    x=16.0,
    y=21.0,
    width=48.0,
    height=48.0
)


canvas.create_rectangle(  # line
    408.0,
    253.0,
    410.24524092674255,
    575.9983825683594,
    fill="#00071D",
    outline="")

cpuImage = PhotoImage(file=relative_to_assets("CPUU-01.png"))  # CPU image
canvas.create_image(16, 268, anchor='nw', image=cpuImage)

"""
canvas.create_rectangle(
    26.0,
    284.0,
    386.0,
    562.0,
    fill="#00071D",
    outline="")
"""
canvas.create_rectangle(
    16.0,
    21.0,
    61.0,
    66.0,
    fill="#00071D",
    outline="")


canvas.create_rectangle(
    432.0,
    253.0,
    766.0,
    576.0,
    fill="#00071D",
    outline="")

canvas.create_rectangle(
    455.0,
    511.0,
    743.0,
    549.0,
    fill="#00071D",
    outline="")

canvas.create_rectangle(
    455.0,
    454.0,
    743.0,
    492.0,
    fill="#00071D",
    outline="")
'''
canvas.create_text(
    455.0,
    234.0,
    anchor="nw",
    text="CPU  SCHEDULING ALGORITHMS",
    fill="#00071D",
    font=("Exo ExtraBoldItalic", 18 * -1)
)
'''
canvas.create_text(
    16.0,
    96.0,
    anchor="nw",
    fill="#00071D",
    font=("Exo2 BoldItalic", 18 * -1)
)

button_image_12 = PhotoImage(
    file=relative_to_assets("button_12.png"))
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=first,
    relief="flat"
)
button_12.place(
    x=455.0,
    y=265.0,
    width=288.0,
    height=38.0
)

button_image_13 = PhotoImage(
    file=relative_to_assets("button_13.png"))
button_13 = Button(
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=second,
    relief="flat"
)
button_13.place(
    x=455.0,
    y=316.0,
    width=288.0,
    height=38.0
)

button_image_15 = PhotoImage(  # HRRN button
    file=relative_to_assets("button_15.png"))
button_15 = Button(
    image=button_image_15,
    borderwidth=0,
    highlightthickness=0,
    command=third,
    relief="flat"
)
button_15.place(
    x=455.0,
    y=367.0,
    width=288.0,
    height=38.0
)

button_image_16 = PhotoImage(
    file=relative_to_assets("Button.png"))
button_16 = Button(
    image=button_image_16,
    borderwidth=0,
    highlightthickness=0,
    command=fourth,
    relief="flat"
)
button_16.place(
    x=455.0,
    y=418.0,
    width=288.0,
    height=38.0
)

button_image_17 = PhotoImage(  # LJF Button
    file=relative_to_assets("button_16.png"))
button_17 = Button(
    image=button_image_17,
    borderwidth=0,
    highlightthickness=0,
    command=fifth,
    relief="flat"
)
button_17.place(
    x=455.0,
    y=469.0,
    width=288.0,
    height=38.0
)

button_image_18 = PhotoImage(  # Comparison buttoon
    file=relative_to_assets("COMP.png"))
button_18 = Button(
    image=button_image_18,
    borderwidth=0,
    highlightthickness=0,
    command=comp,
    relief="flat"
)
button_18.place(
    x=455.0,
    y=520.0,
    width=288.0,
    height=38.0
)

# button_image_2 = PhotoImage(
#     file=relative_to_assets("button_2.png"))
# button_2 = Button(
#     image=button_image_2,
#     borderwidth=0,
#     highlightthickness=0,
#     command=lambda: print("button_2 clicked"),
#     relief="flat"
# )
# button_2.place(
#     x=455.0,
#     y=395.0,
#     width=288.0,
#     height=38.0
# )

"""
bg_right = PhotoImage(file="image1.png")
mylabel1 = Label(window, image=bg_right)
mylabel1.place(x=26, y=284, width=360, height=278)
"""

canvas.create_text(
    4.0,
    202.0,
    anchor="nw",
    text=" of the processes in memory that are ready for execution.",
    fill="#00071D",
    font=("Exo2 SemiBoldItalic", 18 * -1)
)

canvas.create_text(
    4.0,
    181.0,
    anchor="nw",
    text=" for execution. The selection process will be carried out by the CPU scheduler. It selects one",
    fill="#00071D",
    font=("Exo2 SemiBoldItalic", 18 * -1)
)

canvas.create_text(
    9.0,
    162.0,
    anchor="nw",
    text="the CPU remains idle, the OS at least select one of the processes available in the ready queue",
    fill="#00071D",
    font=("Exo2 SemiBoldItalic", 18 * -1)
)

canvas.create_text(
    4.0,
    141.0,
    anchor="nw",
    text=" another process is on hold. The main task of CPU scheduling is to make sure that whenever ",
    fill="#00071D",
    font=("Exo2 SemiBoldItalic", 18 * -1)
)

canvas.create_text(
    9.0,
    118.0,
    anchor="nw",
    text="CPU Scheduling is a process of determining which process will own CPU for execution while",
    fill="#00071D",
    font=("Exo2 SemiBoldItalic", 18 * -1)
)
window.resizable(False, False)
window.mainloop()
