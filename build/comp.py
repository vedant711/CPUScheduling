from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, font
from tkinter.constants import END
import matplotlib.pyplot as plt
import numpy as np


def back():
    window.destroy()


def FCFS(p, at, bt):
    no_of_process = len(p)
    tat = [0] * no_of_process
    wt = [0] * no_of_process
    ct = [0] * no_of_process
    chart = [0] * no_of_process
    at1 = []

    for m in range(no_of_process):
        at1.append(at[m])

    ct1 = [0] * no_of_process
    at1.sort()
    bt1 = [0] * no_of_process
    for j in range(no_of_process):
        x = at.index(at1[j])
        bt1[j] = bt[x]

    # For loop for calculating ct
    for i in range(no_of_process):
        free_time = 0

        if at1[i] <= chart[i-1]:
            if at1[i] == at1[i-1] and p[i] < p[i-1]:
                ct1[i] = at1[i] + bt1[i]
                chart[i] = (ct1[i])
            else:
                ct1[i] = ct1[i-1] + bt1[i]
                chart[i] = (ct1[i])
        else:
            free_time = at1[i] - ct1[i-1]

            ct1[i] = ct1[i-1] + bt1[i] + free_time
            chart[i] = (ct1[i])

    for k in range(no_of_process):
        y = at1.index(at[k])
        ct[k] = ct1[y]

    # For loop for calculating tat
    for i in range(no_of_process):
        tat[i] = ct[i] - at[i]

    # For loop for calculating wt
    for i in range(no_of_process):
        wt[i] = tat[i] - bt[i]

    avg_wt = sum(wt)/no_of_process
    avg_tat = sum(tat)/no_of_process
    return avg_wt, avg_tat


def hrrn(p, at, bt):
    n = len(p)
    ct = [0]*n
    tat = [0] * n
    wt = [0] * n
    at1 = [0] * n  # sort at
    bt1 = [0] * n
    ct1 = [0] * n

    at2 = [0] * n  # rr appending
    bt2 = [0] * n
    executed = []
    p2 = [0] * n  # sorting p
    p3 = [0] * n  # rr appending

    st = [0] * n

    for i in range(n):
        at1[i] = at[i]
        at2[i] = at[i]

    at1.sort()
    at2.sort()

    for i in range(n):
        x = at.index(at1[i])
        bt1[i] = bt[x]
        bt2[i] = bt[x]
        p2[i] = p[x]
        p3[i] = p[x]

    for i in range(n):
        if at2[i] <= ct1[i-1]:
            ct1[i] = ct1[i-1] + bt2[i]
            st[i] = ct1[i-1]
            executed.append(p3[i])
            not_executed = []
            response_ratio = []
            for ele in p3:
                if ele not in executed:
                    not_executed.append(ele)

            for j in not_executed:
                if at1[j-1] <= ct1[i]:
                    rr = ((ct1[i] - at1[j-1]) + bt1[j-1]) / bt1[j-1]
                    response_ratio.append(rr)
                    for ele in response_ratio:
                        if rr > ele:
                            buffer_p3 = p3[i+1]
                            buffer_at2 = at2[i+1]
                            buffer_bt2 = bt2[i+1]
                            at2[i+1] = at1[j-1]
                            bt2[i+1] = bt1[j-1]
                            p3[i+1] = p2[j-1]
                            at2.append(buffer_at2)
                            bt2.append(buffer_bt2)
                            p3.append(buffer_p3)
                            at2.remove(at2[i+2])
                            bt2.remove(bt2[i+2])
                            p3.remove(p3[i+2])

    for i in range(n):
        x = at2.index(at1[i])
        ct[i] = ct1[x]

    ct2 = [0]*n
    for i in range(n):
        x = bt1.index(bt[i])
        ct2[i] = ct[x]

    for i in range(n):
        tat[i] = ct2[i] - at[i]
        wt[i] = tat[i] - bt[i]

    avgtat = sum(tat)/n
    avgwt = sum(wt)/n
    return avgwt, avgtat


def ljf(p, at, bt):
    n = len(p)
    ct = [0] * n
    wt = [0] * n
    tat = [0] * n
    bt1 = [0] * n
    at1 = [0] * n
    ct1 = []
    p1 = [0] * n
    completed_bt = []

    for i in range(n):
        bt1[i] = bt[i]
        at1[i] = at[i]

    bt1.sort()
    bt1.reverse()
    for i in range(0, n):
        x = bt.index(bt1[i])
        at1[i] = at[x]
        p1[i] = p[x]

    not_executed_bt = bt1

    d = True
    chart = 0
    while d:
        for ele in not_executed_bt:
            i = not_executed_bt.index(ele)

            if at1[i] <= chart and bt1[i] not in completed_bt:
                x = bt.index(ele)

                st = chart  # storing for graph
                chart += bt1[i]
                completed_bt.append(bt1[i])
                ct1.append(chart)
                at1.remove(at1[i])
                # adding to completed and removing from not_executed
                not_executed_bt.remove(ele)
                break

        if all(at1[i] > chart for i in range(len(at1))):
            chart += 1

        if not_executed_bt == []:
            d = False

    for i in range(n):
        y = bt.index(completed_bt[i])
        ct[y] = ct1[i]

    for i in range(n):
        tat[i] = ct[i] - at[i]

    # For loop for calculating wt
    for i in range(n):
        wt[i] = tat[i] - bt[i]

    avgtat = sum(tat)/n
    avgwt = sum(wt)/n
    return avgwt, avgtat


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

    avg_wt = sum(wt)/n
    avg_tat = sum(tat)/n
    return avg_wt, avg_tat


def sjf(p, at, bt):
    n = len(p)
    ct = [0] * n
    wt = [0] * n
    tat = [0] * n
    bt1 = [0] * n
    at1 = [0] * n
    ct1 = []
    p1 = [0] * n
    completed_bt = []

    for i in range(n):
        bt1[i] = bt[i]
        at1[i] = at[i]

    bt1.sort()
    for i in range(0, n):
        x = bt.index(bt1[i])
        at1[i] = at[x]
        p1[i] = p[x]

    not_executed_bt = bt1

    d = True
    chart = 0
    while d:
        for ele in not_executed_bt:
            i = not_executed_bt.index(ele)

            if at1[i] <= chart and bt1[i] not in completed_bt:
                x = bt.index(ele)

                st = chart  # storing for graph
                chart += bt1[i]
                completed_bt.append(bt1[i])
                ct1.append(chart)
                at1.remove(at1[i])
                # adding to completed and removing from not_executed
                not_executed_bt.remove(ele)
                break

        if all(at1[i] > chart for i in range(len(at1))):
            chart += 1

        if not_executed_bt == []:
            d = False

    for i in range(n):
        y = bt.index(completed_bt[i])
        ct[y] = ct1[i]

    for i in range(n):
        tat[i] = ct[i] - at[i]

    # For loop for calculating wt
    for i in range(n):
        wt[i] = tat[i] - bt[i]

    avgtat = sum(tat)/n
    avgwt = sum(wt)/n
    return avgwt, avgtat


def compare(p, at, bt, tq):
    fig, compare = plt.subplots()
    compare.set_xlabel('Algorithm')
    compare.set_ylabel('Time')

    x = ['FCFS', 'SJF', 'HRRN', 'RR', 'LJF']
    fcfs_wt, fcfs_tat = FCFS(p, at, bt)
    sjf_wt, sjf_tat = sjf(p, at, bt)
    hrrn_wt, hrrn_tat = hrrn(p, at, bt)
    rr_wt, rr_tat = rr(p, at, bt, tq)
    ljf_wt, ljf_tat = ljf(p, at, bt)

    tat = [fcfs_tat, sjf_tat, hrrn_tat, rr_tat, ljf_tat]
    wt = [fcfs_wt, sjf_wt, hrrn_wt, rr_wt, ljf_wt]
    xaxis = np.arange(len(x))
    plt.bar(xaxis - 0.2, tat, 0.4, label='Turn Around Time')
    plt.bar(xaxis + 0.2, wt, 0.4, label='Waiting Time')
    plt.xticks(xaxis, x)
    plt.title('Comparison of All Algorithms')
    plt.legend()
    plt.show()


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
    114.0,
    24.0,
    anchor="nw",
    text="COMPARISION OF ALL ALGORITHMS",
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
    text="Longest Job First. ",
    fill="#000000",
    font=("Exo SemiBoldItalic", 18 * -1)
)

canvas.create_rectangle(
    239.0,
    319.0,
    528.0,
    352.0,
    fill="#00071D",
    outline="")

canvas.create_text(
    260.0,
    326.0,
    anchor="nw",
    text="Arrival Time(AT):",
    fill="#FFFFFF",
    font=("Exo BoldItalic", 14 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    445.0,
    340.5,
    image=entry_image_1
)
arrival_time = Entry(
    bd=0,
    bg="#00071D",
    highlightthickness=0,
    foreground="#ffffff"
)
arrival_time.place(
    x=380.0,
    y=325.0,
    width=146.0,
    height=19.0
)

canvas.create_rectangle(
    239.0,
    388.0,
    528.0,
    421.0,
    fill="#00071D",
    outline="")

canvas.create_text(
    264.0,
    395.0,
    anchor="nw",
    text="Burst Time(BT):",
    fill="#FFFFFF",
    font=("Exo BoldItalic", 14 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    439.0,
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
    x=372.0,
    y=394.0,
    width=154.0,
    height=19.0
)

canvas.create_rectangle(
    239.0,
    457.0,
    528.0,
    490.0,
    fill="#00071D",
    outline="")

canvas.create_text(
    254.0,
    464.0,
    anchor="nw",
    text="Time Quantum:",
    fill="#FFFFFF",
    font=("Exo BoldItalic", 14 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    439.0,
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
    x=362.0,
    y=463.0,
    width=154.0,
    height=19.0
)


canvas.create_text(
    10.0,
    125.0,
    anchor="nw",
    text="are: First Come First Serve, Shortest Job First, Highest Response Ratio Next, Round Robin, ",
    fill="#000000",
    font=("Exo SemiBoldItalic", 18 * -1)
)

canvas.create_text(
    10.0,
    95.0,
    anchor="nw",
    text="Comparision page shows the comparision of all the algorithms implmented by us. The algorithms",
    fill="#000000",
    font=("Exo SemiBoldItalic", 18 * -1)
)

canvas.create_text(
    10.0,
    183.0,
    anchor="nw",
    text=" ",
    fill="#000000",
    font=("Exo SemiBoldItalic", 18 * -1)
)

canvas.create_rectangle(
    239.0,
    250.0,
    528.0,
    283.0,
    fill="#00071D",
    outline="")

canvas.create_text(
    264.0,
    258.0,
    anchor="nw",
    text="Processes: ",
    fill="#FFFFFF",
    font=("Exo BoldItalic", 14 * -1)
)
'''
canvas.create_rectangle(  # center vertical line
    380.0,
    253.0,
    382.24524092674255,
    575.9983825683594,
    fill="#00071D",
    outline="")
'''

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    439.0,
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
    x=362.0,
    y=256.0,
    width=154.0,
    height=19.0
)


button_image_11 = PhotoImage(
    file=relative_to_assets("compare .png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    # command=lambda: Table(window, list(map(int, process.get().split())), list(
    #     map(int, arrival_time.get().split())), list(map(int, burst_time.get().split())))
    command=lambda: compare(list(map(int, process.get().split())), list(
        map(int, arrival_time.get().split())), list(map(int, burst_time.get().split())), int(time_quantum.get()))
)
button_11.place(
    x=314.0,
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
