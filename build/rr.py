from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, font
from tkinter.constants import END
import matplotlib.pyplot as plt


def back():
    window.destroy()

import matplotlib.pyplot as plt


def rr(p, at, bt, tq):
    n = len(p)
    ct = [0] * n
    wt = [0]*n
    tat = [0]*n
    at1 = [0]*n
    bt1 = [0]*n
    arrived = []
    arrived_left_bt = []
    p1 = [0]*n
    ct1 = []
    completed = []
    completed_bt = []

    yticks = []  # This is to store the bartick values
    ytickL = []  # This is to store the bartick lables
    barHeightVar = 1
    fig, gnt = plt.subplots()
    gnt.set_xlabel('Time')
    gnt.set_ylabel('Processes')

    for i in range(n):
        at1[i] = at[i]

    at1.sort()
    for j in range(n):
        x = at.index(at1[j])
        bt1[j] = bt[x]
        p1[j] = p[x]

    d = True
    chart = 0
    while d:
        # appending process to arrived queue
        for i in range(n):
            if (at1[i] <= chart) and (p1[i] not in arrived) and (bt1[i] not in arrived_left_bt) and (p1[i] not in completed) and (bt1[i] not in completed_bt):
                arrived.append(p1[i])
                arrived_left_bt.append(bt1[i])

        # for breaking the while loop if arrived array is empty then while loop is broken
        if len(arrived) == 0:
            d = False

        # applying the round robin algorithm
        for ele in arrived_left_bt:
            j = arrived_left_bt.index(ele)

            # for the process whose remaining burst time is greater then the tq
            if ele > tq:
                st = chart
                chart += tq
                bt_append = ele - tq
                buffer_pro = arrived[j]

                # appending process to arrived queue
                for i in range(n):
                    if (at1[i] <= chart) and (p1[i] not in arrived) and (bt1[i] not in arrived_left_bt) and (p1[i] not in completed) and (bt1[i] not in completed_bt):
                        arrived.append(p1[i])
                        arrived_left_bt.append(bt1[i])

                # removing and appending elements from the arrived arrays
                arrived_left_bt.remove(ele)
                arrived.remove(buffer_pro)
                arrived.append(buffer_pro)
                arrived_left_bt.append(bt_append)

                # graph for processes not completed but executed atleast once using its start time and tq
                gnt.broken_barh([(st, tq)], (barHeightVar, 2),
                                facecolors='tab:blue')
                yticks.append(
                    barHeightVar + 1)  # thickness of bars is 2 and base starts at barHeightVar, so +1 will give us middle

                ytickL.append(buffer_pro)
                barHeightVar += 3

                break

            else:
                st = chart
                chart += ele
                ct1.append(chart)
                completed_pro = arrived[j]

                # adding the process to completed array
                completed.append(arrived[j])

                # appending process to arrived queue
                for i in range(n):
                    if (at1[i] <= chart) and (p1[i] not in arrived) and (bt1[i] not in arrived_left_bt) and (p1[i] not in completed) and (bt1[i] not in completed_bt):
                        arrived.append(p1[i])
                        arrived_left_bt.append(bt1[i])

                # removing and appending elements from the arrived arrays
                arrived_left_bt.remove(ele)
                arrived.remove(arrived[j])

                # graph for processes not completed but executed atleast once using its start time and tq
                gnt.broken_barh([(st, ele)], (barHeightVar, 2),
                                facecolors='tab:blue')
                yticks.append(
                    barHeightVar + 1)  # thickness of bars is 2 and base starts at barHeightVar, so +1 will give us middle

                ytickL.append(completed_pro)
                barHeightVar += 3

                break

    # indexing according to the completed array
    for i in range(n):
        y = p.index(completed[i])
        ct[y] = ct1[i]

    for i in range(n):
        tat[i] = ct[i] - at[i]

    # For loop for calculating wt
    for i in range(n):
        wt[i] = tat[i] - bt[i]

        gnt.set_ylim(0, (n + 2) * 3)

    # Setting X-axis limits last plus five
    gnt.set_xlim(0, max(ct) + 5)

    # Setting ticks on y-axis
    gnt.set_yticks(yticks)

    # Labelling tickes of y-axis
    gnt.set_yticklabels(ytickL)

    avg_wt = sum(wt)/n
    avg_tat = sum(tat)/n

    for i in range(n):
        print(str(p[i]) + "\t" + str(at[i]) + "\t" + str(bt[i]) + "\t" + str(ct[i]) +
              "\t" + str(tat[i]) + "\t" + str(wt[i]))

    print(avg_wt)
    print(avg_tat)
    lst = [('P', 'AT', 'BT', 'CT', 'TAT', 'WT')]
    for i in range(len(p)):
        ls = (p[i], at[i], bt[i], ct[i], tat[i], wt[i])
        lst.append(ls)
    class Table:

        def __init__(self, window, p, at, bt):

            # code for creating table

            # lst1, avg_tat, avg_wt = FCFS(p, at, bt)
            total_rows = len(lst)
            total_columns = 6
            for i in range(total_rows):
                for j in range(total_columns):
                    width = 65
                    height = 25
                    self.e = Entry(window, width=60, fg='white', bg='#00071D',
                                   font=('Arial', 14, 'bold'))

                    self.e.grid(row=i, column=j)
                    self.e.place(
                        y=(250 + (height*i)),
                        x=(400 + (width*j)),
                    )
                    self.e.insert(END, lst[i][j])
            self.tat = Text(window, fg='white', bg='#00071D',
                            font=('Arial', 14, 'bold'))
            self.tat.insert(END, f'Average TAT = {avg_tat}')
            self.tat.place(
                y=500,
                x=400
            )
            self.wt = Text(window, fg='white', bg='#00071D',
                           font=('Arial', 14, 'bold'))
            self.wt.insert(END, f'Average WT = {avg_wt}')
            self.wt.place(
                y=550,
                x=400,
                height=50
            )
    t = Table(window, p, at, bt)
    plt.show()

'''
p = [1, 2, 3, 4, 5, 6]
at = [0, 1, 2, 3, 4, 6]
bt = [4, 5, 2, 1, 6, 3]
tq = 4
rr(p, at, bt, tq)
'''

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


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
    228.0,
    24.0,
    anchor="nw",
    text="ROUND ROBIN {RR}",
    fill="#FFFFFF",
    font=("Exo SemiBoldItalic", 36 * -1)
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: back(),
    relief="flat"
)
button_10.place(
    x=16.0,
    y=21.0,
    width=48.0,
    height=48.0
)

canvas.create_rectangle(
    358.0,
    212.98936462402344,
    358.00000000000006,
    589.0389251708984,
    fill="#FFFFFF",
    outline="")


canvas.create_text(
    10.0,
    153.0,
    anchor="nw",
    text="enables the system to switch between process. A fixed time is alloted to each process, is called ",
    fill="#000000",
    font=("Exo SemiBoldItalic", 18 * -1)
)

canvas.create_rectangle(
    39.0,
    319.0,
    328.0,
    352.0,
    fill="#00071D",
    outline="")

canvas.create_text(
    49.0,
    326.0,
    anchor="nw",
    text="Arrival Time(AT):",
    fill="#FFFFFF",
    font=("Exo BoldItalic", 14 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    245.0,
    332.5,
    image=entry_image_1
)
arrival_time = Entry(
    bd=0,
    bg="#00071D",
    highlightthickness=0,
    foreground="#ffffff"
)
arrival_time.place(
    x=168.0,
    y=322.0,
    width=154.0,
    height=19.0
)

canvas.create_rectangle(
    39.0,
    388.0,
    328.0,
    421.0,
    fill="#00071D",
    outline="")

canvas.create_text(
    53.0,
    395.0,
    anchor="nw",
    text="Burst Time(BT):",
    fill="#FFFFFF",
    font=("Exo BoldItalic", 14 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    239.0,
    404.5,
    image=entry_image_2
)
burst_time = Entry(
    bd=0,
    bg="#00071D",
    highlightthickness=0,
    foreground="#ffffff"
)
burst_time.place(
    x=162.0,
    y=394.0,
    width=154.0,
    height=19.0
)

canvas.create_rectangle(
    39.0,
    457.0,
    328.0,
    490.0,
    fill="#00071D",
    outline="")

canvas.create_text(
    53.0,
    464.0,
    anchor="nw",
    text="Time Quantum:",
    fill="#FFFFFF",
    font=("Exo BoldItalic", 14 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    239.0,
    473.5,
    image=entry_image_2
)
time_quantum = Entry(
    bd=0,
    bg="#00071D",
    highlightthickness=0,
    foreground="#ffffff"
)
time_quantum.place(
    x=162.0,
    y=463.0,
    width=154.0,
    height=19.0
)



canvas.create_text(
    10.0,
    125.0,
    anchor="nw",
    text="is similar to FCFS scheduling. But in Round Robin {RR} scheduling, preemption is added which",
    fill="#000000",
    font=("Exo SemiBoldItalic", 18 * -1)
)

canvas.create_text(
    10.0,
    95.0,
    anchor="nw",
    text="Round Robin {RR} scheduling algorithm mainly designed for time sharing systems. This algorithm",
    fill="#000000",
    font=("Exo SemiBoldItalic", 18 * -1)
)

canvas.create_text(
    10.0,
    183.0,
    anchor="nw",
    text="a Quantum, for execution",
    fill="#000000",
    font=("Exo SemiBoldItalic", 18 * -1)
)

canvas.create_rectangle(
    39.0,
    250.0,
    328.0,
    283.0,
    fill="#00071D",
    outline="")

canvas.create_text(
    49.0,
    258.0,
    anchor="nw",
    text="Processes: ",
    fill="#FFFFFF",
    font=("Exo BoldItalic", 14 * -1)
)

canvas.create_rectangle(  # center vertical line
    380.0,
    253.0,
    382.24524092674255,
    575.9983825683594,
    fill="#00071D",
    outline="")


entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    239.0,
    266.5,
    image=entry_image_3
)
process = Entry(
    bd=0,
    bg="#00071D",
    highlightthickness=0,
    foreground="#ffffff"
)
process.place(
    x=162.0,
    y=256.0,
    width=154.0,
    height=19.0
)


button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    # command=lambda: Table(window, list(map(int, process.get().split())), list(
    #     map(int, arrival_time.get().split())), list(map(int, burst_time.get().split())))
    command=lambda: rr(list(map(int, process.get().split())), list(
        map(int, arrival_time.get().split())), list(map(int, burst_time.get().split())),int(time_quantum.get()))
)
button_11.place(
    x=114.0,
    y=523.0,
    width=120.1294937133789,
    height=31.0

)

# button_image_14 = PhotoImage(  # Graph Button
#     file=relative_to_assets("button_14.png"))
# button_14 = Button(
#     image=button_image_14,
#     borderwidth=0,
#     highlightthickness=0,
#     command=lambda: print('Graph Button Clicked')
# )
# button_14.place(
#     x=528.0,
#     y=430.0,
#     width=120.1294937133789,
#     height=31.0

# )

window.resizable(False, False)
window.mainloop()
