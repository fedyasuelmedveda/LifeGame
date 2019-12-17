from random import randrange as rnd, choice
import tkinter as tk
import math
import time
import graphics as gr

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x650')
canv = tk.Canvas(root, bg='pink')
canv.pack(fill=tk.BOTH, expand=1)
k_x = 1
k_y = 1
i = 0
k = 0
x_0 = 100
y_0 = 25
R = 300
a = 200
M = 1
dt = 1
w = 0.001
enemys = []


def create_objects():
    canv.create_oval(x_0, y_0, x_0 + 2 * R, y_0 + 2 * R, outline="gray", fill="red", width=2)
    canv.create_oval(x_0 + R - a, y_0 + R - a, x_0 + R + a, y_0 + R + a, fill="white", width=2)


class Ball():
    def __init__(self, x=400, y=325):
        self.x = x
        self.y = y
        self.r = 2
        self.live = 200
        self.vx = 40
        self.vy = 40
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )

    def set_coords(self):
        canv.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

    def move(self):
        self.x += self.vx
        self.y -= self.vy
        self.set_coords()


class Player():

    def __init__(self, ):
        self.f2_power = 20
        self.f2_on = 0
        self.x = 400
        self.y = 325

        self.ay = 0
        self.ax = 0
        self.xc = 400
        self.yc = 325
        self.m = 10
        self.F = self.m * M * 0.1

        self.an = 1
        # self.color = choice(['blue', 'green', 'yellow', 'brown'])
        self.a1 = 30
        self.a2 = 15
        self.vx = 0
        self.vy = 0
        self.v = math.sqrt(self.vx ** 2 + self.vy ** 2)
        self.l = 50
        self.id1 = canv.create_oval(
            self.x - self.a1,
            self.y - self.a1,
            self.x + self.a1,
            self.y + self.a1,
            fill='blue'
        )

        self.id3 = canv.create_line(self.x, self.y, self.x, self.y - self.l, width=6)

        self.id2 = canv.create_oval(
            self.x - self.a2,
            self.y - self.a2,
            self.x + self.a2,
            self.y + self.a2,
            fill='yellow'
        )

    def set_coords2(self):
        canv.coords(
            self.id2,
            self.x - self.a2,
            self.y - self.a2,
            self.x + self.a2,
            self.y + self.a2
        )

    def set_coords1(self):
        canv.coords(
            self.id1,
            self.x - self.a1,
            self.y - self.a1,
            self.x + self.a1,
            self.y + self.a1
        )

    def set_coords3(self):
        global k_x, k_y

        canv.coords(
            self.id3,
            self.x,
            self.y,
            self.x + self.l * k_x,
            self.y + self.l * k_y
        )

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.x, self.y)
        new_ball.r += 5
        self.an = math.atan2((event.y - new_ball.y), (event.x - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        global k_x, k_y

        if event:
            self.an = math.atan2((event.y - self.y), (event.x - self.x))
            canv.coords(self.id3,
                        self.x,
                        self.y,
                        self.x + self.l * math.cos(self.an),
                        self.y + self.l * math.sin(self.an)
                        )
        k_x = math.cos(self.an)
        k_y = math.sin(self.an)

    def acceleration(self):
        global k_x, k_y
        # sina = (self.y-self.yc)/math.sqrt( (self.x-self.xc)**2 + (self.y-self.yc)**2   )
        # cosa =(self.x-self.xc)/math.sqrt( (self.x-self.xc)**2 + (self.y-self.yc)**2  )
        # self.ax = self.F*k_x/self.m + k_x * 2*w*self.vy + w**2*(self.x-self.xc)
        # self.ay = self.F*k_y/self.m + k_y * 2*w*self.vx + w**2*(self.y-self.yc)
        self.ax = -2 * w * self.vy + (w ** 2) * (self.x - self.xc)
        self.ay = 2 * w * self.vx + (w ** 2) * (self.y - self.yc)
        self.vx += self.ax * dt
        self.vy += self.ay * dt
        self.v = math.sqrt(self.vx ** 2 + self.vy ** 2)

    def move(self):
        global k_x, k_y
        # self.x += -k_y*self.v
        # self.y += k_x*self.v
        self.x += self.vx  # *0.1
        self.y += self.vy  # *0.1
        self.set_coords1()
        self.set_coords2()
        self.set_coords3()

    def move_right(self, event):
        global k_x, k_y
        self.x += -k_y * self.v
        self.y += k_x * self.v
        self.set_coords1()
        self.set_coords2()
        self.set_coords3()

    def move_left(self, event):
        global k_x, k_y
        self.x += k_y * self.v
        self.y += -k_x * self.v
        self.set_coords1()
        self.set_coords2()
        self.set_coords3()

    def move_up(self, event):
        global k_x, k_y
        self.vx += self.F * k_x / self.m
        self.vy += self.F * k_y / self.m
        # self.x += k_x*self.v
        # self.y += k_y*self.v
        self.set_coords1()
        self.set_coords2()
        self.set_coords3()

    def move_down(self, event):
        global k_x, k_y

        self.x += -k_x * self.v
        self.y += -k_y * self.v
        self.set_coords1()
        self.set_coords2()
        self.set_coords3()


def get_r_vector(x, y):
    length_vector = math.sqrt(((x_0 + R) - x) ** 2 + ((y_0 + R) - y) ** 2)
    radius_vector = gr.Point(((x_0 + R) - x) / length_vector, ((y_0 + R) - y) / length_vector)
    return radius_vector


def get_normal(x, y):
    length_vector = math.sqrt(((x_0 + R) - x) ** 2 + ((y_0 + R) - y) ** 2)
    normal_vector = gr.Point(((y_0 + R) - y) / length_vector, -((x_0 + R) - x) / length_vector)
    return normal_vector


def scalar_multiplication(vector_1, vector_2):
    scalar = vector_1.x * vector_2.x + vector_1.y * vector_2.y
    return scalar


def change_velocity_vx(vx, vy, x, y):
    velocity = gr.Point(vx, vy)
    vel_normal_0 = gr.Point(get_r_vector(x, y).x
                            * scalar_multiplication(get_r_vector(x, y), velocity),
                            get_r_vector(x, y).y
                            * scalar_multiplication(get_r_vector(x, y), velocity)
                            )
    vel_tau = gr.Point(get_normal(x, y).x
                       * scalar_multiplication(get_normal(x, y), velocity),
                       get_normal(x, y).y
                       * scalar_multiplication(get_normal(x, y), velocity)
                       )
    vel_normal_1 = gr.Point(-vel_normal_0.x, -vel_normal_0.y)
    i = gr.Point(1, 0)

    vel_1_x = scalar_multiplication(vel_normal_1, i)
    vel_2_x = scalar_multiplication(vel_tau, i)

    vx = vel_1_x + vel_2_x

    return vx


def change_velocity_vy(vx, vy, x, y):
    velocity = gr.Point(vx, vy)
    vel_normal_0 = gr.Point(get_r_vector(x, y).x
                            * scalar_multiplication(get_r_vector(x, y), velocity),
                            get_r_vector(x, y).y
                            * scalar_multiplication(get_r_vector(x, y), velocity)
                            )
    vel_tau = gr.Point(get_normal(x, y).x
                       * scalar_multiplication(get_normal(x, y), velocity),
                       get_normal(x, y).y
                       * scalar_multiplication(get_normal(x, y), velocity)
                       )
    vel_normal_1 = gr.Point(-vel_normal_0.x, -vel_normal_0.y)
    j = gr.Point(0, 1)

    vel_1_y = scalar_multiplication(vel_normal_1, j)
    vel_2_y = scalar_multiplication(vel_tau, j)

    vy = vel_1_y + vel_2_y

    return vy


def new_enemy():
    x = rnd(100, 700)
    y = rnd(100, 500)
    r = rnd(10, 15)
    vx = rnd(-4, 4)
    vy = rnd(-4, 4)
    if (x - (x_0 + R)) ** 2 + (y - (y_0 + R)) ** 2 >= a ** 2 and (x - (x_0 + R)) ** 2 + (y - (y_0 + R)) ** 2 <= (
            R - 40) ** 2:
        id_ = canv.create_oval(x - r, y - r, x + r, y + r, fill='black', width=0)
        enemy = {'id': id_, 'x': x, 'y': y, 'r': r, 'vx': vx, 'vy': vy}
        enemys.append(enemy)
    root.after(600, new_enemy)


def motion():
    for e in enemys:
        if (x_0 + R - e['x']) ** 2 + (y_0 + R - e['y']) ** 2 >= (R) ** 2:
            e['vx'] = change_velocity_vx(e['vx'], e['vy'], e['x'], e['y'])
            e['vy'] = change_velocity_vy(e['vx'], e['vy'], e['x'], e['y'])
        e['x'] += e['vx']
        e['y'] += e['vy']
        canv.move(e['id'], e['vx'], e['vy'])
    root.after(10, motion)


balls = []
bullet = 0


def game_process(event=''):
    global balls, bullet
    root.bind('<Button-1>', P1.fire2_start)
    root.bind('<ButtonRelease-1>', P1.fire2_end)
    root.bind('<Motion>', P1.targetting)
    root.bind('<Right>', P1.move_right)
    root.bind('<Left>', P1.move_left)
    root.bind('<Up>', P1.move_up)
    root.bind('<Down>', P1.move_down)
    delete = []
    for b in balls:
        b.move()
        b.live += -1
        if b.live <= 0:
            canv.delete(b.id)
    canv.update()
    P1.move()
    P1.acceleration()
    P1.targetting()
    time.sleep(0.03)

    root.after(1, game_process)


create_objects()

P1 = Player()

game_process()
new_enemy()
motion()

root.mainloop()