from pathlib import Path
from tkinter.constants import END


# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import matplotlib.pyplot as plt


def back():
    window.destroy()


# import matplotlib.pyplot as plt


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

    yticks = []  # This is to store the bartick values
    ytickL = []  # This is to store the bartick lables
    barHeightVar = 1
    fig, gnt = plt.subplots()
    gnt.set_xlabel('Time')
    gnt.set_ylabel('Processes')

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
                gnt.broken_barh([(st, ele)], (barHeightVar, 2),
                                facecolors='tab:blue')
                yticks.append(
                    barHeightVar + 1)  # thickness of bars is 2 and base starts at barHeightVar, so +1 will give us middle

                ytickL.append("P{}".format(p[x]))
                barHeightVar += 3
                break

        if not_executed_bt == []:
            d = False

    for i in range(n):
        y = bt.index(completed_bt[i])
        ct[y] = ct1[i]

    print(ct)

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

    avgtat = sum(tat)/n
    avgwt = sum(wt)/n

    for i in range(n):
        print(str(p[i]) + "\t\t\t" + str(at[i]) + "\t\t\t" + str(bt[i]) + "\t\t\t" + str(ct[i]) +
              "\t\t\t" + str(tat[i]) + "\t\t\t" + str(wt[i]))

    print(avgtat)
    print(avgwt)

    lst = [('P', 'AT', 'BT', 'CT', 'TAT', 'WT')]
    for i in range(len(p)):
        ls = (p[i], at[i], bt[i], ct[i], tat[i], wt[i])
        lst.append(ls)

    class Table:

        def __init__(self, window, p, at, bt):

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
            self.tat.insert(END, f'Average TAT = {avgtat}')
            self.tat.place(
                y=500,
                x=400
            )
            self.wt = Text(window, fg='white', bg='#00071D',
                           font=('Arial', 14, 'bold'))
            self.wt.insert(END, f'Average WT = {avgwt}')
            self.wt.place(
                y=550,
                x=400,
                height=50
            )

    t = Table(window, p, at, bt)
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
    width=45.0,
    height=45.0
)

canvas.create_text(
    178.0,
    18.0,
    anchor="nw",
    text="SHORTEST-JOB-FIRST {SJF}",
    fill="#FFFFFF",
    font=("Exo SemiBoldItalic", 36 * -1)
)

canvas.create_text(
    11.0,
    208.0,
    anchor="nw",
    text=" ensures the shorter tasks are completed as early as possible.",
    fill="#000000",
    font=("Exo SemiBoldItalic", 18 * -1)
)

canvas.create_rectangle(
    347.0,
    255.0,
    350.0178027153015,
    593.9998474121094,
    fill="#FFFFFF",
    outline="")

canvas.create_text(
    10.0,
    95.0,
    anchor="nw",
    text="The shortest job first scheduling is an algorithm in which the shortest job gets executed first.",
    fill="#000000",
    font=("Exo SemiBoldItalic", 18 * -1)
)

canvas.create_text(
    11.0,
    118.0,
    anchor="nw",
    text="This algorithm is used significantly to optimise the processing speed of the processors. For a",
    fill="#000000",
    font=("Exo SemiBoldItalic", 18 * -1)
)

canvas.create_text(
    10.0,
    142.0,
    anchor="nw",
    text=" processor to perform this kind of scheduling algorithm, it must know the burst time of the",
    fill="#000000",
    font=("Exo SemiBoldItalic", 18 * -1)
)

canvas.create_text(
    10.0,
    164.0,
    anchor="nw",
    text=" processes beforehand. And this is effective for batch-type processing, in which the waiting",
    fill="#000000",
    font=("Exo SemiBoldItalic", 18 * -1)
)

canvas.create_text(
    10.0,
    186.0,
    anchor="nw",
    text=" time is not critical for the process. This kind of processing has a high throughput because it",
    fill="#000000",
    font=("Exo SemiBoldItalic", 18 * -1)
)

canvas.create_rectangle(
    32.0,
    456.0,
    321.0,
    489.0,
    fill="#00071D",
    outline="")

canvas.create_rectangle(  # center vertical line
    380.0,
    253.0,
    382.24524092674255,
    575.9983825683594,
    fill="#00071D",
    outline="")

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: sjf(list(map(int, processes.get().split())), list(
        map(int, arrival_time.get().split())), list(map(int, burst_time.get().split()))),
    relief="flat"
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
#     command=lambda: print("Graph Button clicked")
# )
# button_14.place(
#     x=528.0,
#     y=430.0,
#     width=120.1294937133789,
#     height=31.0

# )

canvas.create_text(
    40.0,
    463.0,
    anchor="nw",
    text="Burst Time (BT):",
    fill="#FFFFFF",
    font=("Exo BoldItalic", 14 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    237.0,
    472.5,
    image=entry_image_1
)
burst_time = Entry(
    bd=0,
    bg="#00071D",
    highlightthickness=0,
    foreground='#ffffff'
)
burst_time.place(
    x=160.0,
    y=462.0,
    width=154.0,
    height=19.0
)

canvas.create_rectangle(
    32.0,
    398.0,
    321.0,
    431.0,
    fill="#00071D",
    outline="")

canvas.create_text(
    40.0,
    405.0,
    anchor="nw",
    text="Arrival Time (AT): ",
    fill="#FFFFFF",
    font=("Exo BoldItalic", 14 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    237.0,
    413.5,
    image=entry_image_2
)
arrival_time = Entry(
    bd=0,
    bg="#00071D",
    highlightthickness=0,
    foreground='#ffffff'
)
arrival_time.place(
    x=160.0,
    y=403.0,
    width=154.0,
    height=19.0
)

canvas.create_rectangle(
    32.0,
    343.0,
    321.0,
    376.0,
    fill="#00071D",
    outline="")

canvas.create_text(
    40.0,
    349.0,
    anchor="nw",
    text="Processes: ",
    fill="#FFFFFF",
    font=("Exo BoldItalic", 14 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    232.0,
    359.5,
    image=entry_image_3
)
processes = Entry(
    bd=0,
    bg="#00071D",
    highlightthickness=0,
    foreground='#ffffff'
)
processes.place(
    x=155.0,
    y=349.0,
    width=154.0,
    height=19.0
)


window.resizable(False, False)
window.mainloop()
