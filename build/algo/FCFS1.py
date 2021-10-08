from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


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

    for i in range(no_of_process):
        print(str(p[i]) + "\t" + str(at[i]) + "\t" + str(bt[i]) + "\t" + str(ct[i]) +
              "\t" + str(tat[i]) + "\t" + str(wt[i]))

    print(avg_wt)
    print(avg_tat)
    lst = [0] * no_of_process
    for i in range(len(p)):
        lst[i] = (p[i], at[i], bt[i], ct[i], tat[i], wt[i])
    print(lst)


p = [1, 2, 3]
at = [22, 0, 23]
bt = [1, 2, 3]
FCFS(p, at, bt)
