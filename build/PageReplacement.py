from tkinter import *                          #Tkinter library
import random                                  #Used in Random Page Replacement Algorithm
import matplotlib.pyplot as plt                #Plotted graph using matplotlib
import subprocess                              #Link Theory.py with this page

# Theory of PRA
def theory():
    file1 = "python Theory.py"
    # os.system(file1)
    p = subprocess.Popen(file1, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()

#-----------------------------------------------------------------------------------------------------------------------
# Initializing the variables
def Initialize():
    global root
    global row
    global col
    global FaultRatio
    row = 0
    col = 1
    FaultRatio = 0

#-----------------------------------------------------------------------------------------------------------------------
# First In Out First Out Page Replacement Algorithm
def FIFO(pages, n, capacity, txt, animation):
    Initialize()
    global FaultRatio
    global col
    global root
    global row

    fault_record = []
    hit_record = []
    frames = [c for c in range(capacity + 3)]

    if animation is True:
        new_window(txt, capacity)
    for ii in frames:
        if ii == 0:
            fault_record.append(0)
            hit_record.append(0)
            continue
        s = set()
        front = 0
        indexes = []
        page_faults = 0
        fault = []
        for i in range(n):
            if (len(s) < ii):
                if (pages[i] not in s):
                    s.add(pages[i])
                    page_faults += 1
                    fault.append(True)
                    indexes.append(pages[i])
                else:
                    fault.append(False)
            else:
                if (pages[i] not in s):
                    s.remove(indexes[front])
                    s.add(pages[i])
                    indexes[front] = pages[i]
                    page_faults += 1
                    fault.append(True)
                    front+=1
                    if(front>ii-1):
                        front=0
                else:
                    fault.append(False)
            if ii == capacity:
                FaultRatio = float((page_faults) / n)
                dummy = indexes
                if animation is True:
                    anime(capacity, pages[i], dummy, fault[i], FaultRatio, txt, n, frames, fault_record, hit_record)
                col += 1
        fault_record.append(page_faults)
        hit_record.append(n-page_faults)

#-----------------------------------------------------------------------------------------------------------------------
# Last IN First Out Page Replacement Algorithm
def LIFO(pages, n, capacity, txt, animation):
    Initialize()
    global col
    global FaultRatio
    global root
    global row

    fault_record = []
    hit_record = []
    frames = [c for c in range(capacity + 3)]


    if animation is True:
        new_window(txt, capacity)

    for ii in frames:
        if ii == 0:
            fault_record.append(0)
            hit_record.append(0)
            continue
        s = set()
        end_l = ii-1
        indexes = []
        page_faults = 0
        fault = []
        for i in range(n):
            if (len(s) < ii):
                if (pages[i] not in s):
                    s.add(pages[i])
                    page_faults += 1
                    fault.append(True)
                    indexes.append(pages[i])
                else:
                    fault.append(False)
            else:
                if (pages[i] not in s):
                    s.remove(indexes[end_l])
                    s.add(pages[i])
                    indexes[end_l] = pages[i]
                    page_faults += 1
                    fault.append(True)
                else:
                    fault.append(False)
            if ii == capacity:
                FaultRatio = float((page_faults) / n)
                dummy = indexes
                if animation is True:
                    anime(capacity, pages[i], dummy, fault[i], FaultRatio, txt, n, frames, fault_record, hit_record)
                col += 1
        fault_record.append(page_faults)
        hit_record.append(n-page_faults)

#-----------------------------------------------------------------------------------------------------------------------
# Least Recently Used Page Replacement Algorithm
def LRU(processList, n, capacity, txt, animation):
    Initialize()
    global FaultRatio
    global col
    global root
    global row

    fault_record = []
    hit_record = []
    frames = [c for c in range(capacity + 3)]


    if animation is True:
        new_window(txt, capacity)

    for ii in frames:
        if ii == 0:
            fault_record.append(0)
            hit_record.append(0)
            continue
        s = []
        fault = []
        st = []
        pageFaults = 0
        j = 0
        for i in processList:

            if i not in s:

                if (len(s) < ii):
                    s.append(i)
                    st.append(len(s)-1)

                else:
                    ind = st.pop(0)
                    s[ind] = i
                    st.append(ind)

                pageFaults += 1
                fault.append(True)
            else:
                fault.append(False)
                st.append(st.pop(st.index(s.index(i))))
            if ii == capacity:
                FaultRatio = float((pageFaults)/n)
                dummy = s
                if animation is True:
                    anime(capacity, processList[j], dummy, fault[j], FaultRatio, txt, n, frames, fault_record, hit_record)
                j+=1
                col += 1
        fault_record.append(pageFaults)
        hit_record.append(n-pageFaults)

#-----------------------------------------------------------------------------------------------------------------------
# Most Recently Used Page Replacement Algorithm
def MRU(processList, n, capacity, txt, animation):
    Initialize()
    global FaultRatio
    global col
    global root
    global row

    fault_record = []
    hit_record = []
    frames = [c for c in range(capacity + 3)]


    if animation is True:
        new_window(txt, capacity)
    for ii in frames:
        if ii == 0:
            fault_record.append(0)
            hit_record.append(0)
            continue
        j = 0
        s = []
        fault = []
        st = []
        pageFaults = 0
        last_used_index = 0
        for i in processList:

            if i not in s:

                if (len(s) < ii):
                    s.append(i)
                    st.append(len(s)-1)
                    last_used_index = len(s)-1
                else:
                    # ind = st.pop(0)
                    s[last_used_index] = i
                    st.append(last_used_index)

                pageFaults += 1
                fault.append(True)
            else:
                fault.append(False)
                for k in range(len(s)):
                    if s[k] == i:
                        last_used_index = k
            if ii == capacity:
                FaultRatio = float((pageFaults)/n)
                dummy = s
                if animation is True:
                    anime(capacity, processList[j], dummy, fault[j], FaultRatio, txt, n, frames, fault_record, hit_record)
                j+=1
                col += 1
        fault_record.append(pageFaults)
        hit_record.append(n-pageFaults)

#-----------------------------------------------------------------------------------------------------------------------
# Optimal Page Replacement Algorithm
def Optimal(processList, n, capacity, txt, animation):
    Initialize()
    global FaultRatio
    global col
    global root
    global row

    fault_record = []
    hit_record = []
    frames = [c for c in range(capacity + 3)]
    if animation is True:
        new_window(txt, capacity)
    for ii in frames:
        if ii == 0:
            fault_record.append(0)
            hit_record.append(0)
            continue
        s = []
        fault = []
        pageFaults = 0
        occurance = [None for i in range(ii)]
        for i in range(n):
            if processList[i] not in s:
                if len(s) < ii:
                    s.append(processList[i])
                else:
                    for x in range(len(s)):
                        if s[x] not in processList[i + 1:]:
                            s[x] = processList[i]
                            break
                        else:
                            occurance[x] = processList[i + 1:].index(s[x])
                    else:
                        s[occurance.index(max(occurance))] = processList[i]
                pageFaults += 1
                fault.append(True)
            else:
                fault.append(False)
            if ii == capacity:
                FaultRatio = float((pageFaults)/n)
                dummy = s
                if animation is True:
                    anime(capacity, processList[i], dummy, fault[i], FaultRatio, txt, n, frames, fault_record, hit_record)
                col += 1
        fault_record.append(pageFaults)
        hit_record.append(n-pageFaults)

#-----------------------------------------------------------------------------------------------------------------------
# Random Page Replacement Algorithm
def Random(pages, n, capacity, txt, animation):
    Initialize()
    global FaultRatio
    global col
    global root
    global row

    fault_record = []
    hit_record = []
    frames = [c for c in range(capacity + 3)]

    if animation is True:
        new_window(txt, capacity)

    for ii in frames:
        if ii == 0:
            fault_record.append(0)
            hit_record.append(0)
            continue
        s = set()
        indexes = []
        page_faults = 0
        fault = []
        for i in range(n):
            if (len(s) < ii):
                if (pages[i] not in s):
                    s.add(pages[i])
                    page_faults += 1
                    fault.append(True)
                    indexes.append(pages[i])
                else:
                    fault.append(False)
            else:
                randomIndex = random.randint(0, ii - 1)
                if (pages[i] not in s):
                    s.remove(indexes[randomIndex])
                    s.add(pages[i])
                    indexes[randomIndex] = pages[i]
                    page_faults += 1
                    fault.append(True)
                else:
                    fault.append(False)
            if ii == capacity:
                FaultRatio = float((page_faults) / n)
                dummy = indexes
                if animation is True:
                    anime(capacity, pages[i], dummy, fault[i], FaultRatio, txt, n, frames, fault_record, hit_record)
                col += 1
        fault_record.append(page_faults)
        hit_record.append(n-page_faults)

#-----------------------------------------------------------------------------------------------------------------------
# All functions used for the visualization of the algorithms:
# Opens new window for the visualization
def new_window(txt, capacity):
    global root
    root = Tk()
    Basic_design(capacity)
    root.title("Visualisation Of Algorithm: " + txt)
    root.geometry("1600x660")

# For spaces in between Frames and for better clarity and visibility
def empty_space():
    global root
    global row
    global col
    L = Label(root, text=" ", height="1", width="1")
    L.grid(row=row, column=col)
    row += 1

# If the reference string is too large then remove this function for better visibility
def build_EmptyLabel():
    global col
    global row
    MyLabel1= Label(root,text=" ",padx=15,pady=10)
    MyLabel1.grid(row=1,column=col+1)
    col+=1

# Basic layout design
def Basic_design(N):
    k=N

    RefStringLabel= Label(root,text="Reference String")
    RefStringLabel.configure(font=("Century Gothic", 15))
    RefStringLabel.grid(row=0,column=0,padx=20,pady=10)
    for i in range(N):
        mylabel= Label(root,text="Frame "+str(k),pady=10,padx=20,fg="black")
        mylabel.configure(font=("Century Gothic", 15))
        mylabel.grid(row=i+1,column=0)
        k-=1
    FaultStringLabel= Label(root,text="Page Faults")
    FaultStringLabel.configure(font=("Century Gothic", 15))
    FaultStringLabel.grid(row=N+1,column=0,padx=20,pady=10)

# Function to build the labels containing reference string
def cell(element):
    global root
    global row
    global col
    L = Label(root, text=element, padx=20,pady=10,bd=1,fg="green",relief=SOLID,anchor="center")
    L.configure(font=("Century Gothic", 12))
    L.grid(row=row, column=col)
    row += 1


# Label for the fault and hit ratio
def FrameRatio(FaultRatio, Frames, txt, frames, fault_record, hit_record):
    lenCol = int(Frames / 2)
    frame1 = LabelFrame(root, text=" "+txt+" Page Fault Ratio ",pady=15, padx=10)
    frame1.configure(font=("Century Gothic", 15))
    frame1.grid(row=Frames + 4, column=lenCol, columnspan=int(Frames))
    HitRatio = 1 - FaultRatio
    myLabel4 = Label(frame1, text=" Hit Ratio:   =", fg="green", bd=1, padx=10, pady=15, relief=FLAT)
    myLabel4.configure(font=("Century Gothic", 14, 'bold'))
    myLabel4.grid(row=1, column=0)
    myLabel5 = Label(frame1, text="Fault Ratio: =", fg="red", bd=1, padx=10, pady=15, relief=FLAT)
    myLabel5.configure(font=("Century Gothic", 14, 'bold'))
    myLabel5.grid(row=2, column=0)
    e2 = Label(frame1, text=str(round(HitRatio,11)), borderwidth=3)
    e2.configure(font=("Century Gothic", 14))
    e2.grid(row=1, column=1)
    e3 = Label(frame1, text=str(round(FaultRatio,11)), borderwidth=3)
    e3.configure(font=("Century Gothic", 14))
    e3.grid(row=2, column=1)
    Graph = Button(root, borderwidth="0", text="Show Graph", bg="#e8e8e8", fg="green", font=("Century Gothic", 15),
               activeforeground="black", activebackground="#bbbfca", command=lambda: graphy(frames, fault_record, hit_record))
    Graph.grid(row=Frames+5, column=lenCol, columnspan=int(Frames), pady=18)
    Back = Button(root, borderwidth="0", text="Back", bg="#e8e8e8", fg="green", font=("Century Gothic", 15),
               activeforeground="black", activebackground="#bbbfca", command=root.destroy)
    Back.grid(row=Frames+6, column=lenCol, columnspan=int(Frames))

# Graph of hit and fault
def graphy(frames, fault_record, hit_record):
    fig = plt.figure(figsize=(8, 8), dpi=80)
    plt.subplot(2, 1, 1)
    plt.xlabel("No. Of Frames --->")
    plt.ylabel("Fault --->")
    plt.plot(frames, fault_record, marker='x', color="red", ls="--")
    plt.subplot(2, 1, 2)
    plt.xlabel("No. Of Frames --->")
    plt.ylabel("Hit --->")
    plt.plot(frames, hit_record, marker='o', color="green")
    plt.show()

# Main Animation Function
def anime(Frames, Page, Q, faultOrHit, FaultRatio, txt, n, frames, fault_record, hit_record):
    global root
    global row
    global col
    row = 0
    L = Label(root, text=Page, pady=10, fg="green")
    L.configure(font=("Century Gothic", 15))
    L.grid(row=row, column=col)
    row += 1
    ls = []
    ls = Q
    for i in range(Frames - len(ls)):
        empty_space()

    for i in reversed(ls):
        cell(i)

    build_EmptyLabel()

    if (faultOrHit == True):
        FaultOrHit1 = "Fault"
        L1 = Label(root, text=FaultOrHit1, fg="red")
        L1.configure(font=("Century Gothic", 12, 'bold'))
        L1.grid(row=row, column=col - 1)
        row += 1
    else:
        FaultOrHit1 = "Hit"
        L1 = Label(root, text=FaultOrHit1, font="Questrial", fg="green")
        L1.configure(font=("Century Gothic", 12, 'bold'))
        L1.grid(row=row, column=col - 1)
        row += 1
    FrameRatio(FaultRatio, n, txt, frames, fault_record, hit_record)

#-----------------------------------------------------------------------------------------------------------------------
# Graph Function
def graph(noF, refString):
    plot_list=[]
    algos=["FIFO","LIFO","LRU","MRU","Optimal","Random"]
    dummy=0
    N = int(noF)
    pageR = list(refString.split(" "))
    n = len(pageR)

    Initialize()
    FIFO(pageR, n, N, None, False)
    dummy=FaultRatio
    plot_list.append(dummy)

    Initialize()
    LIFO(pageR, n, N, None, False)
    dummy=FaultRatio
    plot_list.append(dummy)

    Initialize()
    LRU(pageR, n, N, None, False)
    dummy=FaultRatio
    plot_list.append(dummy)

    Initialize()
    MRU(pageR, n, N, None, False)
    dummy=FaultRatio
    plot_list.append(dummy)

    Initialize()
    Optimal(pageR, n, N, None, False)
    dummy=FaultRatio
    plot_list.append(dummy)

    Initialize()
    Random(pageR, n, N, None, False)
    dummy=FaultRatio
    plot_list.append(dummy)

    fig = plt.figure()
    plt.bar(algos, plot_list)
    plt.show()

#-----------------------------------------------------------------------------------------------------------------------
# Visualise Button Command
def Visualise(option, noFrame, refString):
    noF = (int)(noFrame)
    pageR = list(map(int, refString.split(" ")))
    N = len(pageR)

    txt = "0"
    if option == "FIFO":
        txt = "First In First Out"
        FIFO(pageR, N, noF, txt, True)

    elif option == "LIFO":
        txt = "Last In First Out"
        LIFO(pageR, N, noF, txt, True)

    elif option == "LRU":
        txt = "Least Recently Used"
        LRU(pageR, N, noF, txt, True)

    elif option == "MRU":
        txt = "Most Recently Used"
        MRU(pageR, N, noF, txt, True)

    elif option == "Optimal PRA":
        txt = "Optimal PRA"
        Optimal(pageR, N, noF, txt, True)

    elif option == "Random PRA":
        txt = "Random PRA"
        Random(pageR, N, noF, txt, True)



# ----------------------------------------------------------------------------------------------------------------------
# Main Page
Menu = Tk()
Menu.title("Page Replacement Algorithm")
Menu.overrideredirect(False)
# Menu.iconbitmap("icon.ico")
Menu.geometry("800x750+0+0")
Menu.resizable(False, False)

L1 = Label(bg="black", text="Page Replacement Algorithm", fg="white", font=("Century Gothic", 35), width="900",
           height="1").pack()

F1 = Frame(bg="white").pack()

L2 = Label(F1, text="Choose Algorithm:", font=("Century Gothic", 18)).pack(pady="15")

variable = StringVar()
variable.set("FIFO")  # default value
dropDown = OptionMenu(F1, variable, "FIFO", "LIFO", "LRU", "MRU","Optimal PRA", "Random PRA")
dropDown.configure(borderwidth="0", width="12", bg="#e8e8e8", fg="green", font=("Century Gothic", 12),
                   activeforeground="black", activebackground="#bbbfca")
dropDown.pack(pady="5")

L3 = Label(F1, text="Enter the no. of frames:", font=("Century Gothic", 18)).pack(pady="20")

# take input
noFrames = Entry(F1, width="15", bg="#e8e8e8", fg="green", font=("Century Gothic", 15), bd="0", justify="center")
noFrames.pack()

L4 = Label(F1, text="Enter Page Reference: ", font=("Century Gothic", 18)).pack(pady="30")

# take input
pageRef = Entry(F1, bg="#e8e8e8", fg="green", font=("Century Gothic", 15), bd="0", justify="center")
pageRef.pack()

L5 = Button(F1, borderwidth="0", text="Visualise", bg="#e8e8e8", fg="green", font=("Century Gothic", 18),
            activeforeground="black", activebackground="#bbbfca",
            command=lambda: Visualise(variable.get(), noFrames.get(), pageRef.get())).pack(pady="25")

L6 = Button(F1, borderwidth="0", text="Compare All Algorithms", bg="#e8e8e8", fg="green", font=("Century Gothic", 18),
            activeforeground="black", activebackground="#bbbfca", command=lambda: graph(noFrames.get(), pageRef.get())).pack()

L7 = Button(F1, borderwidth="0", text="Theory", bg="#e8e8e8", fg="green", font=("Century Gothic", 18),
            activeforeground="black", activebackground="#bbbfca", command=theory).pack(pady="25")

L8 = Button(F1, borderwidth="0", text="Back", bg="#e8e8e8", fg="green", font=("Century Gothic", 18),
            activeforeground="black", activebackground="#bbbfca", command=Menu.destroy).pack()
Menu.mainloop()