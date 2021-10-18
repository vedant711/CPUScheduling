import matplotlib.pyplot as plt


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
                gnt.broken_barh([(st, ele)], (barHeightVar, 2),
                                facecolors='tab:blue')
                yticks.append(
                    barHeightVar + 1)  # thickness of bars is 2 and base starts at barHeightVar, so +1 will give us middle

                ytickL.append("P{}".format(p[x]))
                barHeightVar += 3
                break

        if all(at1[i] > chart for i in range(len(at1))):
            chart += 1

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

    plt.show()


p = [1, 2, 3, 4, 5]
at = [2, 3, 4, 5, 6]
bt = [3, 2, 4, 5, 6]
ljf(p, at, bt)
