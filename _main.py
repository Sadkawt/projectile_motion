from tkinter import *
import numpy as np
import pygame
from pygame.locals import *
import sys
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from animation import pygame_proj
from multi import multi_proj
from normal import normal_proj

def SICKO_MODE():
    print("not yett ; )")


def add_options():
    if variable.get() == "Multi Graph":
        print("tjenis")
        Qdtheta = Entry(master)
        Qdtheta.insert(10,"")
        Qdtheta.grid(row=2, column=2)


def save_entry_fields():
    global globvars, kval_glob, mass_glob
    first = Qvelocity.get()
    second = Qangle.get()
    third = Qheight.get()
    fourth = Qdt.get()
    type = variable.get()
    if variablecheck.get() == 1:
        kval_glob = 0.00079
        mass_glob = 0.148
    print(type)

    globvars = [first, second, third, fourth, type]
    print(globvars)

    Qvelocity.delete(0,END)
    Qangle.delete(0,END)
    Qheight.delete(0,END)
    Qdt.delete(0,END)

    if globvars[4] == "Default Graph":
        normal_proj()
    if globvars[4] == "Multi Graph":
        multi_proj()
    if globvars[4] == "Animation":
        pygame_proj()
    if globvars[4] == "SICKO MODE":
        SICKO_MODE()


def save_entry_fields2():
    global kval_glob, mass_glob
    try:
        kval_glob = (float(Q2fluid.get())*float(Q2drag.get())*float(Q2ref.get()))/2
        mass_glob = Q2mass.get()
        Successwindow = Toplevel(master)
        Label(Successwindow, text="Calculations succesfull!").grid(row=0)
        Label(Successwindow, text=("k = ", str(kval_glob))).grid(row=1)
        Button(Succeswindow, text='Ok', command=Succeswindow.destroy).grid(row=2)
    except ValueError:
        errorwindow = Toplevel(master)
        Label(errorwindow, text="ONLY INT AND FLOAT VALUES ALLOWED!!!").grid(row=0)
        Button(errorwindow, text='Ok', command=errorwindow.destroy).grid(row=1)


def save_entry_fields3():
    global xlow_glob, xupp_glob, ylow_glob, yupp_glob
    try:
        xlow_glob = int(Qxlow.get())
        xupp_glob = int(Qxupp.get())
        ylow_glob = int(Qylow.get())
        yupp_glob = int(Qyupp.get())

        if False in {isinstance(xlow_glob,int), isinstance(xupp_glob,int), isinstance(ylow_glob,int), isinstance(yupp_glob,int)}:
            xlow_glob = 0
            xupp_glob = 100
            ylow_glob = 0
            yupp_glob = 100
            errorwindow = Toplevel(master)
            Label(errorwindow, text="ONLY INT VALUES ALLOWED").grid(row=0)
            Button(errorwindow, text='Ok', command=errorwindow.destroy).grid(row=1)
        else:
            Succeswindow = Toplevel(master)
            Label(Succeswindow, text="Values have been saved").grid(row=0)
            Button(Succeswindow, text='Ok', command=Succeswindow.destroy).grid(row=1)

    except ValueError:
        errorwindow = Toplevel(master)
        Label(errorwindow, text="ONLY INT VALUES ALLOWED").grid(row=0)
        Button(errorwindow, text='Ok', command=errorwindow.destroy).grid(row=1)


def enter_other_variables():
    global Q2mass, Q2fluid, Q2ref, Q2drag, window
    print("tjebbo :-)")
    window = Toplevel(master)

    Label(window, text="Mass (m)= ").grid(row=0)
    Label(window, text="Fluid density= ").grid(row=1)
    Label(window, text="Reference area= ").grid(row=2)
    Label(window, text="Drag coefficient= ").grid(row=3)


    Q2mass = Entry(window)
    Q2fluid = Entry(window)
    Q2ref = Entry(window)
    Q2drag = Entry(window)

    Q2mass.insert(10,"")
    Q2fluid.insert(10,"")
    Q2ref.insert(10,"")
    Q2drag.insert(10,"")

    Q2mass.grid(row=0, column=1)
    Q2fluid.grid(row=1, column=1)
    Q2ref.grid(row=2, column=1)
    Q2drag.grid(row=3, column=1)

    Button(window, text='Back', command=window.destroy).grid(row=4, column=0, sticky=W, pady=4)
    Button(window, text='Done', command=save_entry_fields2).grid(row=4, column=2, sticky=W, pady=4)


def set_bounds():
    global Qxlow, Qxupp, Qylow, Qyupp
    window = Toplevel(master)

    Label(window, text="x lower bound").grid(row=0, column=0)
    Label(window, text="x upper bound").grid(row=1, column=0)
    Label(window, text="y lower bound").grid(row=0, column=2)
    Label(window, text="y upper bound").grid(row=1, column=2)

    Qxlow = Entry(window)
    Qxupp = Entry(window)
    Qylow = Entry(window)
    Qyupp = Entry(window)

    Qxlow.insert(10,"")
    Qxupp.insert(10,"")
    Qylow.insert(10,"")
    Qyupp.insert(10,"")

    Qxlow.grid(row=0, column=1)
    Qxupp.grid(row=1, column=1)
    Qylow.grid(row=0, column=3)
    Qyupp.grid(row=1, column=3)

    Button(window, text='Back', command=window.destroy).grid(row=5, column=0, sticky=W, pady=4)
    Button(window, text='Done', command=save_entry_fields3).grid(row=5, column=2, sticky=W, pady=4)

master = Tk()
Label(master, text="Velocity= ").grid(row=0)
Label(master, text="Angle= ").grid(row=1)
Label(master, text="Starting Height= ").grid(row=2)
Label(master, text="dt= ").grid(row=3)

Qvelocity = Entry(master)
Qangle = Entry(master)
Qheight = Entry(master)
Qdt = Entry(master)

Qvelocity.insert(10,"")
Qangle.insert(10,"")
Qheight.insert(10,"")
Qdt.insert(10,"0.01")

Qvelocity.grid(row=0, column=1)
Qangle.grid(row=1, column=1)
Qheight.grid(row=2, column=1)
Qdt.grid(row=3, column=1)

variable = StringVar(master)
variable.set("Default Graph") # default value

DispType = OptionMenu(master, variable, "Default Graph", "Multi Graph", "Animation", "SICKO MODE",command=add_options)
DispType.grid(row=0, column=2, sticky=W,pady=4)

variablecheck = IntVar()
checkbutton = Checkbutton(master, text="Baseball", variable=variablecheck)
checkbutton.grid(row=1, column=2, sticky=W, pady=4)
checkbutton.select()

Button(master, text='Set bounds', command=set_bounds).grid(row=2, column=2, sticky=W, pady=4)
Button(master, text='Quit', command=master.quit).grid(row=4, column=0, sticky=W, pady=4)
Button(master, text='Go', command=save_entry_fields).grid(row=4, column=1, sticky=W, pady=4)
Button(master, text='Other variables', command=enter_other_variables).grid(row=4, column=2, sticky=W, pady=4)


mainloop()
