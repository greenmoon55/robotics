# % matplotlib inline
import scipy
import numpy as np
import matplotlib.pyplot as plt

from scipy.interpolate import spline

from math import *


def get_point(x, y, theta, steering, distance):
    length = 20
    turn = tan(steering) * distance / length
    radius = distance / turn
    cx = x - (sin(theta) * radius)
    cy = y + (cos(theta) * radius)
    theta = (theta + turn) % (2.0 * pi)
    x2 = cx + (sin(theta) * radius)
    y2 = cy - (cos(theta) * radius)
    return x2, y2, theta, steering, distance


def smoothly_print_points(x, y):
    x = np.array(x)
    y = np.array(y)
    xnew = np.linspace(x.min(), x.max(), 300)

    power_smooth = spline(x, y, xnew)

    plt.plot(xnew, power_smooth)
    plt.show()


def print_path(x1, y1, theta1, steering, x2, y2, d, delta=5):
    distance = 0
    x, y, theta = x1, y1, theta1
    x_print = []
    y_print = []
    while distance < d:
        distance += delta
        x2, y2, theta, steering, distance = get_point(x, y, theta1, steering, distance)
        print x2, y2, theta, steering, distance
        x_print.append(x2)
        y_print.append(y2)
    smoothly_print_points(x_print, y_print)


x, y, theta, steering, distance = 0., 0., 0., 0.2, 10

print_path(x, y, theta, steering, 29.5398545262, 4.52594328886, 20)

# for i in range(10):
#     x, y, theta, steering, distance = get_point(x, y, theta, steering, distance)
#     print x, y, theta, steering, distance

