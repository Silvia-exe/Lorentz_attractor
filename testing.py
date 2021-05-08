
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
xs_iv = np.linspace(1.0,1.1,10)
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
    for  i in range(stepCnt):
    # Derivatives of the X, Y, Z state
        x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i],ss,rs,bs)
        xs[i + 1] = xs[i] + (x_dot * dt)
        ys[i + 1] = ys[i] + (y_dot * dt)
        zs[i + 1] = zs[i] + (z_dot * dt)
    xs = np.array(xs)
    xs_array.append(xs)
    ys_array.append([ys])
    zs_array.append([zs])

print(len(xs_array))
print(xs_array)

xs_delta = []

for i in range(len(xs_array)-1):
    xs_delta = xs_array[i] - xs_array[i+1]
    plt.plot(xs_delta)
    plt.show()

plt.savefig("s" + str(int(ss)) + "_r" + str(int(rs)) + "_b"+ str(int(bs)) +"_" + str(xs[0])+str(ys[0])+str(zs[0])+".png")

print(xs[-1])
print(ys[-1])
print(zs[-1])

plt.show()