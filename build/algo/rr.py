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

    plt.show()


p = [1, 2, 3, 4, 5, 6]
at = [0, 1, 2, 3, 4, 6]
bt = [4, 5, 2, 1, 6, 3]
tq = 4
rr(p, at, bt, tq)
