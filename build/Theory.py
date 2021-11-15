from tkinter import *


def one():
    photo_root = Toplevel()
    photo_root.title("FIFO Theory")
    photo_root.geometry("1152x648")
    photo_root.resizable(False, False)
    photo = PhotoImage(file="Theory/FifoTheory.png")
    photo_label = Label(photo_root, image=photo)
    photo_label.pack()
    photo_root.mainloop()


def two():
    photo_root = Toplevel()
    photo_root.title("LIFO Theory")
    photo_root.geometry("1152x648")
    photo_root.resizable(False, False)
    photo = PhotoImage(file="Theory/LifoTheory.png")
    photo_label = Label(photo_root, image=photo)
    photo_label.pack()
    photo_root.mainloop()


def three():
    photo_root = Toplevel()
    photo_root.title("LRU Theory")
    photo_root.geometry("1152x648")
    photo_root.resizable(False, False)
    photo = PhotoImage(file="Theory/LruTheory.png")
    photo_label = Label(photo_root, image=photo)
    photo_label.pack()
    photo_root.mainloop()


def four():
    photo_root = Toplevel()
    photo_root.title("MRU Theory")
    photo_root.geometry("1152x648")
    photo_root.resizable(False, False)
    photo = PhotoImage(file="Theory/MruTheory.png")
    photo_label = Label(photo_root, image=photo)
    photo_label.pack()
    photo_root.mainloop()


def five():
    photo_root = Toplevel()
    photo_root.title("Optimal Theory")
    photo_root.geometry("1152x648")
    photo_root.resizable(False, False)
    photo = PhotoImage(file="Theory/OptimalTheory.png")
    photo_label = Label(photo_root, image=photo)
    photo_label.pack()
    photo_root.mainloop()


def six():
    photo_root = Toplevel()
    photo_root.title("Random Theory")
    photo_root.geometry("1152x648")
    photo_root.resizable(False, False)
    photo = PhotoImage(file="Theory/RandomTheory.png")
    photo_label = Label(photo_root, image=photo)
    photo_label.pack()
    photo_root.mainloop()


# -----------------------------------------------------------------------------------------------------------------------
# Home Page
Menu = Tk()

Menu.title("Theory Of PRA")
Menu.overrideredirect(False)
Menu.geometry("800x750+0+0")
Menu.resizable(False, False)

L1 = Label(bg="black", text="Theory Of PRA", fg="white", font=("Century Gothic", 35), width="900",
           height="1")
L1.pack()
f1 = Frame(bg="white").pack()
l1 = Label(text="Choose Theory: ", font=("Century Gothic", 15))
l1.pack(pady="40")
Button1 = Button(f1, text="First In First Out", borderwidth="0", bg="#e8e8e8", fg="green", font=("Century Gothic", 18),
                 activeforeground="black", activebackground="#bbbfca", command=one).pack()
Button2 = Button(f1, text="Last In First Out", borderwidth="0", bg="#e8e8e8", fg="green", font=("Century Gothic", 18),
                 activeforeground="black", activebackground="#bbbfca", command=two).pack(pady="30")
Button3 = Button(f1, text="Least Recently Used", borderwidth="0", bg="#e8e8e8", fg="green", font=("Century Gothic", 18),
                 activeforeground="black", activebackground="#bbbfca", command=three).pack()
Button4 = Button(f1, text="Most Recently Used", borderwidth="0", bg="#e8e8e8", fg="green", font=("Century Gothic", 18),
                 activeforeground="black", activebackground="#bbbfca", command=four).pack(pady="30")
Button5 = Button(f1, text="Optimal PRA", borderwidth="0", bg="#e8e8e8", fg="green", font=("Century Gothic", 18),
                 activeforeground="black", activebackground="#bbbfca", command=five).pack()
Button6 = Button(f1, text="Random PRA", borderwidth="0", bg="#e8e8e8", fg="green", font=("Century Gothic", 18),
                 activeforeground="black", activebackground="#bbbfca", command=six).pack(pady="30")
Button7 = Button(f1, text="Back", borderwidth="0", bg="#e8e8e8", fg="green", font=("Century Gothic", 18),
                 activeforeground="black", activebackground="#bbbfca", command=Menu.destroy).pack()
Menu.mainloop()
