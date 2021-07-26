import numpy as np
from math import sin, cos
import matplotlib.pyplot as plt


def rotate_matrix(phi):
    return np.array([[cos(phi), sin(phi)], [-sin(phi), cos(phi)]])


def rotate(v, phi):
    return np.dot(v, rotate_matrix(phi))


def transition(x, v, dt, do_branch=False):
    if do_branch:
        phi = (2 * np.random.random(1) - 1) * np.pi / 5
    else:
        phi = 0
    phi_noise = (2 * np.random.random(1) - 1) * np.pi * (1 / 15)
    vp = rotate(v, phi + phi_noise)
    drift = np.array([0, np.random.random(1)[0]])
    return x + dt * (vp + drift), vp


def plt_line(x, xp, branch_num):
    plt.plot(
        [x[0], xp[0]],
        [x[1], xp[1]],
        color="brown",
        linewidth=7 / (1.5) ** branch_num,
    )


def random_branch(
    x_init=np.array([0, 0]),
    v_init=np.array([0, 1]),
    dt=0.01,
    p=0.8,
    current_step=0,
    max_step=300,
    branch_num=1,
):

    if current_step < max_step:

        x, v = x_init, v_init
        a = np.random.binomial(n=1, p=p, size=1)

        if a == 0:
            # barnching does not occure
            dt_new = dt / 1
            xp, vp = transition(x, v, dt_new)
            plt_line(x, xp, branch_num)
            random_branch(xp, vp, dt_new, p, current_step + 1, max_step, branch_num=branch_num)

        else:

            q = p / 2
            dt_new = dt / 2

            xp, vp = transition(x, v, dt_new, do_branch=True)
            plt_line(x, xp, branch_num + 1)
            random_branch(xp, vp, dt_new, q, current_step + 1, max_step, branch_num=branch_num + 1)

            xp, vp = transition(x, v, dt_new, do_branch=True)
            plt_line(x, xp, branch_num + 1)
            random_branch(xp, vp, dt_new, q, current_step + 1, max_step, branch_num=branch_num + 1)


plt.figure(figsize=(20, 20))
plt.axis("off")
N = 10
for i in range(N):
    random_branch(v_init=np.random.random(2))
plt.savefig("./vessel.png")
