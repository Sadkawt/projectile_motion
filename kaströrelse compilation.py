from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
import pygame
from pygame.locals import *
import sys

def normal_proj():
    dt = float(globvars[3])
    t = np.arange(0, 30, dt)
    m = float(mass_glob)
    theta0 = np.radians(float(globvars[1]))
    v0 = float(globvars[0])
    k = float(kval_glob)
    g = 9.82
    vx0 = v0 * np.cos(theta0)
    vy0 = v0 * np.sin(theta0)
    ax0 = -(k * v0 * vx0) / m
    ay0 = -(k * v0 * vy0) / m - g
    x = 0
    y = float(globvars[2])


    def theta(vx, vy):
        theta = np.arctan(vy / vx)
        print("theta", theta)
        return theta


    def ax(k, v, theta, m):
        ax = -k * np.square(v) * np.cos(theta) / m
        print("ax", ax)
        return ax


    def ay(k, v, theta, m):
        ay = -k * np.square(v) * np.sin(theta) / m - g
        print("ay", ay)
        return ay


    def vxny(vx, ax, dt):
        vxny = vx + ax * dt
        print("vx", vxny)
        return vxny


    def vyny(vy, ay, dt):
        vyny = vy + ay * dt
        print("vy", vyny)
        return vyny


    def v(vx, vy):
        v = np.sqrt(np.square(vx) + np.square(vy))
        print("v", v)
        return v


    def langdx(x, vxny, dt):
        xny = x + vxny * dt
        print("x:", xny)
        return xny


    def langdy(y, vyny, dt):
        yny = y + vyny * dt
        print("y:", yny)
        return yny


    x1 = [0]
    y1 = [float(globvars[2])]

    for delta_t in t:
        x = langdx(x, vx0, dt)
        y = langdy(y, vy0, dt)
        vx0 = vxny(vx0, ax0, dt)
        vy0 = vyny(vy0, ay0, dt)
        theta0 = theta(vx0, vy0)
        v0 = v(vx0, vy0)
        ax0 = ax(k, v0, theta0, m)
        ay0 = ay(k, v0, theta0, m)
        x1.append(x)
        y1.append(y)
        plt.plot(x1, y1)
        print("Delta t", delta_t, "\n")
        if y <= 0:
            print("max y:", max(y1))
            break
    try:
        plt.axis([xlow_glob, xupp_glob, ylow_glob, yupp_glob])
    except NameError:
        plt.axis([0,100,0,100])
    plt.show()

def multi_proj():
    dt = float(globvars[3])
    d_theta = np.radians(Angle_interval_glob)
    t = np.arange(0, 30, dt)
    m = float(mass_glob)
    theta0 = np.arange(np.float128(np.radians(Lower_angle_glob)), np.float128(np.radians(Upper_angle_glob)), np.float128(np.radians(Angle_interval_glob)))          #Converts degrees to radians
    print(Lower_angle_glob, Upper_angle_glob, Angle_interval_glob)
    print("theta: ", theta0)
    v0 = float(globvars[0])
    g = 9.82
    k = float(kval_glob)
    vx0 = v0 * np.cos(theta0)
    vy0 = v0 * np.sin(theta0)
    ax0 = -(k * v0 * vx0) / m
    ay0 = -(k * v0 * vy0) / m - g

    def theta_ny(vx, vy):
        theta = np.arctan(vy / vx)
        print("theta:", theta)
        return theta

    def ax(k, v, theta, m):
        ax = -k * np.square(v) * np.cos(theta) / m
        print("ax:", ax)
        return ax

    def ay(k, v, theta, m):
        ay = -k * np.square(v) * np.sin(theta) / m - g
        print("ay:", ay)
        return ay

    def vxny(vx, ax, dt):
        vxny = vx + ax * dt
        print("vx:", vxny)
        return vxny

    def vyny(vy, ay, dt):
        vyny = vy + ay * dt
        print("vy:", vyny)
        return vyny

    def v(vx, vy):
        v = np.sqrt(np.square(vx) + np.square(vy))
        print("v:", v)
        return v

    def längdx(x, vxny, dt):
        xny = x + vxny * dt
        print("x:", xny)
        return xny

    def längdy(y, vyny, dt):
        yny = y + vyny * dt
        print("y:", yny)
        return yny

    x1 = [0]
    y1 = [float(globvars[2])]
    p = 0
    diktx = {}
    dikty = {}

    for delta_theta in theta0:
        print("Delta Theta:", delta_theta)
        diktx[p] = x1
        dikty[p] = y1
        p += 1
        v0 = float(globvars[0])
        vx0 = v0 * np.cos(delta_theta)
        vy0 = v0 * np.sin(delta_theta)
        ax0 = -(k * v0 * vx0) / m
        ay0 = -(k * v0 * vy0) / m - g
        x = 0
        y = float(globvars[2])
        x1 = [0]
        y1 = [float(globvars[2])]
        thetan = delta_theta
        for delta_t in t:
            vx0 = vxny(vx0, ax0, dt)
            vy0 = vyny(vy0, ay0, dt)
            thetan = theta_ny(vx0, vy0)
            v0 = v(vx0, vy0)
            ax0 = ax(k, v0, thetan, m)
            ay0 = ay(k, v0, thetan, m)
            x = längdx(x, vx0, dt)
            y = längdy(y, vy0, dt)
            x1.append(x)
            y1.append(y)
            print("tid:", delta_t, "\n")
            if y <= 0:
                print("maxy:", max(y1), "\n")
                diktx[p] = x1
                dikty[p] = y1
                break


    for j in range(1, p+1):
        plt.plot(diktx[j], dikty[j])

    for j in range(1, p+1):
        print(int(np.degrees(theta0[j-1])), ":", max(diktx[j]))

    try:
        plt.axis([xlow_glob, xupp_glob, ylow_glob, yupp_glob])
    except NameError:
        plt.axis([0,100,0,100])
    plt.show()


def pygame_proj():
    x = 0
    y = float(globvars[2])
    dt = float(globvars[3])
    t = np.arange(0, 30, dt)
    m = float(mass_glob)
    theta0 = np.radians(float(globvars[1]))
    v0 = float(globvars[0])
    k = float(kval_glob)
    g = 9.81
    vx0 = v0 * np.cos(theta0)
    vy0 = v0 * np.sin(theta0)
    ax0 = -(k * v0 * vx0) / m
    ay0 = -(k * v0 * vy0) / m - g


    def theta(vx, vy):
        theta = np.arctan(vy / vx)
        print("t", theta)
        return theta


    def ax(k, v, theta, m):
        ax = -k * np.square(v) * np.cos(theta) / m
        print("ax", ax)
        return ax


    def ay(k, v, theta, m):
        ay = -k * np.square(v) * np.sin(theta) / m - g
        print("ay", ay)
        return ay


    def vxny(vx, ax, dt):
        vxny = vx + ax * dt
        print("vx", vxny)
        return vxny


    def vyny(vy, ay, dt):
        vyny = vy + ay * dt
        print("vy", vyny)
        return vyny


    def v(vx, vy):
        v = np.sqrt(np.square(vx) + np.square(vy))
        print("v", v)
        return v


    def langdx(x, vxny, dt):
        xny = x + vxny * dt
        print(xny)
        return xny


    def langdy(y, vyny, dt):
        yny = y + vyny * dt
        print(yny)
        return yny


    x1 = [0]
    y1 = [float(globvars[2])]



    if theta0 == np.radians(90) or theta0 == np.radians(270):
        for delta_t in t:
            if vy0 <= 0 or v0 <= 0:
                theta0 = np.radians(270)
                print("down")
            else:
                theta0 = np.radians(90)
                print("up")
            x = 0
            y = langdy(y, vy0, dt)
            vx0 = 0
            vy0 = vyny(vy0, ay0, dt)
            v0 = v(vx0, vy0)
            ax0 = 0
            ay0 = ay(k, v0, theta0, m)
            if y < 0:
                break
            x1.append(x)
            y1.append(y)


    else:
        for delta_t in t:
            x = langdx(x, vx0, dt)
            y = langdy(y, vy0, dt)
            vx0 = vxny(vx0, ax0, dt)
            vy0 = vyny(vy0, ay0, dt)
            theta0 = theta(vx0, vy0)
            v0 = v(vx0, vy0)
            ax0 = ax(k, v0, theta0, m)
            ay0 = ay(k, v0, theta0, m)
            if y < 0:
                break
            x1.append(x)
            y1.append(y)


    w = 1440          #Bredden pa fonstret
    h = 900           #Hojden pa fonstret


    SCREEN_SIZE = WIDTH, HEIGHT = (w, h)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 50, 50)
    GREEN = (50, 255, 50)
    CIRCLE_RADIUS = 1

    # Initialization
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption('Circles')
    fps = pygame.time.Clock()
    paused = False

    # Ball setup
    ball_pos1 = [0, 0]


    def update(stamp):
            ball_pos1[0] = int(np.rint(10*x1[stamp]))
            ball_pos1[1] = int(np.rint(-10*y1[stamp]))+700


    def render():
        screen.fill(BLACK)
        pygame.draw.rect(screen, GREEN, (0,700,1440,900), 0)
        pygame.draw.circle(screen, WHITE, ball_pos1, CIRCLE_RADIUS, 0)
        pygame.display.update()
        fps.tick(1000)


    stamp = 0
    stamp1 = len(x1)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    paused = not paused
        if not paused:
            if stamp < stamp1:
                update(stamp)
                render()
                stamp += 1
            else:
                break

def SICKO_MODE():
    print("not yett ; )")

def add_options(k):
    global Qdtheta, dtheta_text, QLow, QUp, QInter
    if variable.get() == "Multi Graph":
        print("tjenis")
        window = Toplevel(master)

        Label(window, text="Lower angle= ").grid(row=0)
        Label(window, text="Upper angle= ").grid(row=1)
        Label(window, text="Interval between angles= ").grid(row=2)

        QLow = Entry(window)
        QUp = Entry(window)
        QInter = Entry(window)

        QLow.insert(10,"")
        QUp.insert(10,"")
        QInter.insert(10,"")

        QLow.grid(row=0, column=1)
        QUp.grid(row=1, column=1)
        QInter.grid(row=2, column=1)

        Button(window, text='Back', command=window.destroy).grid(row=3, column=0, sticky=W, pady=4)
        Button(window, text='Done', command=save_entry_fields4).grid(row=3, column=2, sticky=W, pady=4)

        # Qdtheta = Entry(master)
        # Qdtheta.insert(10,"")
        # Qdtheta.grid(row=2, column=3)
        #
        # dtheta_text = Label(master, text="Interval")
        # dtheta_text.grid(row=1, column=3)
        #Label(master, text="Interval").grid(row=1, column=3)
    else:
        try:
            Qdtheta.grid_remove()
            dtheta_text.grid_remove()
        except NameError:
            None

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
        kval_glob = (float(Q2fluid.get())*float(Q2drag.get())*float(Q2ref.get())*float(Q2flow.get())**2)
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

def save_entry_fields4():
    global Lower_angle_glob, Upper_angle_glob, Angle_interval_glob
    try:
        Lower_angle_glob = int(QLow.get())
        Upper_angle_glob = int(QUp.get())
        Angle_interval_glob = int(QInter.get())
        if isinstance(Lower_angle_glob,float) == True or isinstance(Lower_angle_glob,int) == True:
            if isinstance(Upper_angle_glob,float) == True or isinstance(Upper_angle_glob,int) == True:
                if isinstance(Angle_interval_glob,float) == True or isinstance(Angle_interval_glob,int) == True:
                    Succeswindow = Toplevel(master)
                    Label(Succeswindow, text="Values have been saved").grid(row=0)
                    Button(Succeswindow, text='Ok', command=Succeswindow.destroy).grid(row=1)
        else:
            errorwindow = Toplevel(master)
            Label(errorwindow, text="ONLY INT VALUES ALLOWED d").grid(row=0)
            Button(errorwindow, text='Ok', command=errorwindow.destroy).grid(row=1)
    except ValueError:
        errorwindow = Toplevel(master)
        Label(errorwindow, text="ONLY INT VALUES ALLOWED  ssdsd").grid(row=0)
        Button(errorwindow, text='Ok', command=errorwindow.destroy).grid(row=1)



def enter_other_variables():
    global Q2mass, Q2fluid, Q2flow, Q2ref, Q2drag, window
    print("tjebbo :-)")
    window = Toplevel(master)

    Label(window, text="Mass (m)= ").grid(row=0)
    Label(window, text="Fluid density (ρ)= ").grid(row=1)
    Label(window, text="Flow velocity (μ)= ").grid(row=2)
    Label(window, text="Reference area (A)= ").grid(row=3)
    Label(window, text="Drag coefficient (Cd)= ").grid(row=4)


    Q2mass = Entry(window)
    Q2fluid = Entry(window)
    Q2flow = Entry(window)
    Q2ref = Entry(window)
    Q2drag = Entry(window)

    Q2mass.insert(10,"")
    Q2fluid.insert(10,"")
    Q2flow.insert(10,"")
    Q2ref.insert(10,"")
    Q2drag.insert(10,"")

    Q2mass.grid(row=0, column=1)
    Q2fluid.grid(row=1, column=1)
    Q2flow.grid(row=2, column=1)
    Q2ref.grid(row=3, column=1)
    Q2drag.grid(row=4, column=1)

    Button(window, text='Back', command=window.destroy).grid(row=5, column=0, sticky=W, pady=4)
    Button(window, text='Done', command=save_entry_fields2).grid(row=5, column=2, sticky=W, pady=4)

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
Label(master, text="Velocity (m/s)= ").grid(row=0)
Label(master, text="Angle (°)= ").grid(row=1)
Label(master, text="Starting Height (m)= ").grid(row=2)
Label(master, text="dt (Δs)= ").grid(row=3)

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
