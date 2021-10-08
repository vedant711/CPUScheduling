import matplotlib.pyplot as plt


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

    plt.show()


p = [1, 2, 3, 4, 5]
at = [0, 2, 4, 6, 8]
bt = [3, 6, 4, 5, 2]
hrrn(p, at, bt)
