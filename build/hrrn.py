
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, font
from tkinter.constants import END
import matplotlib.pyplot as plt

def back():
    window.destroy()

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
    yticks = []  # This is to store the bartick values
    ytickL = []  # This is to store the bartick lables
    barHeightVar = 1
    fig, gnt = plt.subplots()
    gnt.set_xlabel('Time')
    gnt.set_ylabel('Processes')

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
            print(st[i])
            executed.append(p3[i])
            # print(executed)
            # for j in range(i+1, n-i):
            #     if at1[j] <= ct1[i]:
            #         rr = ((ct1[i] - at1[j]) + bt1[j]) / bt1[j]
            #         response_ratio.append(rr)
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

            gnt.broken_barh([(st[i], bt2[i])], (barHeightVar, 2),
                            facecolors='tab:blue')
            yticks.append(
                barHeightVar + 1)  # thickness of bars is 2 and base starts at barHeightVar, so +1 will give us middle

            ytickL.append("P{}".format(p3[i]))
            barHeightVar += 3

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

    gnt.set_ylim(0, (n + 2) * 3)

    # Setting X-axis limits last plus five
    gnt.set_xlim(0, max(ct2) + 5)

    # Setting ticks on y-axis
    gnt.set_yticks(yticks)

    # Labelling tickes of y-axis
    gnt.set_yticklabels(ytickL)

    avgtat = sum(tat)/n
    avgwt = sum(wt)/n

    for i in range(n):
        print(str(p[i]) + "\t\t\t" + str(at[i]) + "\t\t\t" + str(bt[i]) + "\t\t\t" + str(ct2[i]) +
              "\t\t\t" + str(tat[i]) + "\t\t\t" + str(wt[i]))

    print(avgtat)
    print(avgwt)

    lst = [('P', 'AT', 'BT', 'CT', 'TAT', 'WT')]
    for i in range(len(p)):
        ls = (p[i], at[i], bt[i], ct2[i], tat[i], wt[i])
        lst.append(ls)

    class Table:

        def __init__(self, window, p, at, bt):

            # code for creating table
            #lst1, avg_tat, avg_wt = hrrn(p, at, bt)
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

            #print(hrrn(p, at, bt))
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

canvas.create_text(
    64,
    24,
    anchor="nw",
    text="HIGHEST RESPONSE RATIO NEXT {HRRN}",
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
    x=10.0,
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
    text="Given n processes with their Arrival times and Burst times, the task is to find average turn ",
    fill="#000000",
    font=("Exo SemiBoldItalic", 18 * -1)
)

canvas.create_rectangle(
    39.0,
    369.0,
    328.0,
    402.0,
    fill="#00071D",
    outline="")

canvas.create_text(
    49.0,
    376.0,
    anchor="nw",
    text="Arrival Time(AT):",
    fill="#FFFFFF",
    font=("Exo BoldItalic", 14 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    245.0,
    382.5,
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
    y=372.0,
    width=154.0,
    height=19.0
)

canvas.create_rectangle(
    39.0,
    438.0,
    328.0,
    471.0,
    fill="#00071D",
    outline="")

canvas.create_text(
    53.0,
    445.0,
    anchor="nw",
    text="Burst Time(BT):",
    fill="#FFFFFF",
    font=("Exo BoldItalic", 14 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    239.0,
    454.5,
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
    y=444.0,
    width=154.0,
    height=19.0
)

canvas.create_text(
    10.0,
    125.0,
    anchor="nw",
    text="select the one with the highest Response Ratio. A process once selected will run till completion.",
    fill="#000000",
    font=("Exo SemiBoldItalic", 18 * -1)
)

canvas.create_text(
    10.0,
    95.0,
    anchor="nw",
    text="The name itself states that we need to find the response ratio of all available processes and ",
    fill="#000000",
    font=("Exo SemiBoldItalic", 18 * -1)
)

canvas.create_text(
    10.0,
    183.0,
    anchor="nw",
    text="around time using HRRN scheduling algorithm. ",
    fill="#000000",
    font=("Exo SemiBoldItalic", 18 * -1)
)

canvas.create_rectangle(
    39.0,
    300.0,
    328.0,
    333.0,
    fill="#00071D",
    outline="")

canvas.create_text(
    49.0,
    308.0,
    anchor="nw",
    text="Processes: ",
    fill="#FFFFFF",
    font=("Exo BoldItalic", 14 * -1)
)

canvas.create_rectangle(
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
    316.5,
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
    y=306.0,
    width=154.0,
    height=19.0
)


button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: hrrn(list(map(int, process.get().split())), list(
        map(int, arrival_time.get().split())), list(map(int, burst_time.get().split()))),
    relief="flat"
    #Table(window, list(map(int, process.get().split())), list(
    #    map(int, arrival_time.get().split())), list(map(int, burst_time.get().split())))
)
button_11.place(
    x=114.0,
    y=523.0,
    width=120.1294937133789,
    height=31.0

)
"""
button_image_14 = PhotoImage(                       #Graph Button
    file=relative_to_assets("button_14.png"))
button_14 = Button(
    image=button_image_14,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Graph Button Clicked")
)
button_14.place(
    x=528.0,
    y=430.0,
    width=120.1294937133789,
    height=31.0

)
"""
window.resizable(False, False)
window.mainloop()
