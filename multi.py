def multi_proj():
    d_theta = np.radians(1)
    lower = np.radians(0.0001)
    upper = np.radians(float(globvars[1]))
    print("upper: ", upper)
    theta0 = np.arange(np.float128(lower), np.float128(upper), np.float128(d_theta))
    print(theta0)
    dt = float(globvars[3])
    t = np.arange(0, 30, dt)
    m = float(mass_glob)
    v0 = float(globvars[0])
    k = float(kval_glob)
    g = 9.82
    vx0 = v0 * np.cos(theta0)
    vy0 = v0 * np.sin(theta0)
    ax0 = -(k * v0 * vx0) / m
    ay0 = -(k * v0 * vy0) / m - g
    x = 0
    y = float(globvars[2])



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
    p = 0
    diktx = {}
    dikty = {}

    for delta_theta in theta0:
        print("Delta Theta:", delta_theta)
        diktx[k] = x1
        dikty[k] = y1
        p += 1
        v0 = 50
        vx0 = v0 * np.cos(delta_theta)
        vy0 = v0 * np.sin(delta_theta)
        ax0 = -(k * v0 * vx0) / m
        ay0 = -(k * v0 * vy0) / m - g
        x = 0
        y = 0
        x1 = [0]
        y1 = [0]
        thetan = delta_theta
        for delta_t in t:
            vx0 = vxny(vx0, ax0, dt)
            vy0 = vyny(vy0, ay0, dt)
            thetan = theta_ny(vx0, vy0)
            v0 = v(vx0, vy0)
            ax0 = ax(k, v0, thetan, m)
            ay0 = ay(k, v0, thetan, m)
            x = langdx(x, vx0, dt)
            y = langdy(y, vy0, dt)
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
