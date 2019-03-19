def pygame_proj():
    dt = float(globvars[3])
    t = np.arange(0, 30, dt)
    m = float(mass_glob)
    theta0 = float(globvars[1])
    v0 = float(globvars[0])
    k = float(kval_glob)
    g = 9.81
    vx0 = v0 * np.cos(theta0)
    vy0 = v0 * np.sin(theta0)
    ax0 = -(k * v0 * vx0) / m
    ay0 = -(k * v0 * vy0) / m - g
    x = 0
    y = float(globvars[2])


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
            vx0 = 0
            vy0 = vyny(vy0, ay0, dt)
            v0 = v(vx0, vy0)
            ax0 = 0
            ay0 = ay(k, v0, theta0, m)
            x = 0
            y = langdy(y, vy0, dt)
            if y < 0:
                break
            x1.append(x)
            y1.append(y)


    else:
        for delta_t in t:
            vx0 = vxny(vx0, ax0, dt)
            vy0 = vyny(vy0, ay0, dt)
            theta0 = theta(vx0, vy0)
            v0 = v(vx0, vy0)
            ax0 = ax(k, v0, theta0, m)
            ay0 = ay(k, v0, theta0, m)
            x = langdx(x, vx0, dt)
            y = langdy(y, vy0, dt)
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
