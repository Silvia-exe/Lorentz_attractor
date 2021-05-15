
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def lorenz(x, y, z, s, r, b):
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return x_dot, y_dot, z_dot


dt = 0.01
stepCnt = 5000

# Need one more for the initial values
xs_array = []
ys_array = []
zs_array = []
xs_iv = np.linspace(1.0,1.1,100)
xs = np.empty((stepCnt + 1,))
ys = np.empty((stepCnt + 1,))
zs = np.empty((stepCnt + 1,))
ss = 10
rs = 28.
bs = 8/3

# Setting initial values
xs[0], ys[0], zs[0] = (1.0, 1.0, 1.0)

# Stepping through "time".
for x0 in xs_iv:
    xs[0] = x0
    ys[0] = ys[0]
    zs[0] = zs[0]
    for i in range(stepCnt):
    # Derivatives of the X, Y, Z state
        x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i],ss,rs,bs)
        xs[i + 1] = xs[i] + (x_dot * dt)
        ys[i + 1] = ys[i] + (y_dot * dt)
        zs[i + 1] = zs[i] + (z_dot * dt)
    xs = np.array(xs)
    ys = np.array(ys)
    zs = np.array(zs)
    xs_array.append(xs)
    ys_array.append(ys)
    zs_array.append(zs)

xs_delta = []
j = 0
for i in xs_array:
    j = j+1
    plt.clf()
    plt.plot(i)
    plt.xlabel("Time step [arb]")
    plt.ylabel("x position [arb]")
    plt.xlim(0,5000)
    plt.ylim(-30,30)
    plt.grid()
    plt.title("$x_0 =$" + str(round(i[0],6)))
    plt.savefig("x0_" + str(j) + "_" + str(round(i[0],4)) +".png")

'''ax = plt.figure().add_subplot(projection='3d')

ax.plot(xs, ys, zs, lw=0.5)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor")

plt.show()'''

'''plt.plot(xs_array[1]-xs_array[0])

plt.xlabel("Time-step [arb]")
plt.ylabel("Position in x [arb]")

plt.xlim(0,5000)
plt.ylim(-30,30)
plt.grid()
plt.title("$\Delta x$")'''

