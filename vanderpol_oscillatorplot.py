import numpy as np 
import matplotlib.pyplot as plt
from scipy.integrate import odeint


# ----- change values of mu to see different cycles. mu=1 gives limit cycle.

def vdp1(y,t,mu=1):
    y2 = y[1]
    y1 = y[0]

    return np.array([y2, (mu-y1**2)*y2-y1])

steps = 20

s1 = np.linspace(-6,6,steps)
s2 = np.linspace(-6,6,steps)

x,y = np.meshgrid(s1,s2)

u = np.zeros_like(x)
v = np.zeros_like(x)

# print x.size
# print x
flattened_x = x.flatten('F')
flattened_y = y.flatten('F')

plt.ion()
for i in range(x.size):

    y_sol = odeint(vdp1,np.array([flattened_x[i],flattened_y[i]]),np.linspace(0,20),tfirst=False)

    plt.quiver(y_sol[:,0],y_sol[:,1], np.gradient(y_sol[:,0]), np.gradient(y_sol[:,1]),
                 width = 0.0005, headwidth = 3, color = 'r')
    plt.pause(0.00001)
    plt.draw()

raw_input()
