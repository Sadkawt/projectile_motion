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
        vx0 = vxny(vx0, ax0, dt)
        vy0 = vyny(vy0, ay0, dt)
        theta0 = theta(vx0, vy0)
        v0 = v(vx0, vy0)
        ax0 = ax(k, v0, theta0, m)
        ay0 = ay(k, v0, theta0, m)
        x = langdx(x, vx0, dt)
        y = langdy(y, vy0, dt)
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
