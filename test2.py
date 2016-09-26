# % matplotlib inline
import scipy
import numpy as np
import matplotlib.pyplot as plt

from scipy.interpolate import spline

from math import *


def get_point(x, y, theta, steering, distance):
    length = 20.
    turn = tan(steering) * distance / length
    radius = distance / turn
    cx = x - (sin(theta) * radius)
    cy = y + (cos(theta) * radius)
    theta = (theta + turn) % (2.0 * pi)
    x2 = cx + (sin(theta) * radius)
    y2 = cy - (cos(theta) * radius)
    return x2, y2, theta, steering, distance


def smoothly_print_points(x, y):
    print "points:"
    print x
    print y
    x = np.array(x)
    y = np.array(y)
    # xnew = np.linspace(x.min(), x.max(), 100)
    # power_smooth = spline(x, y, xnew)
    #
    # print xnew
    # print power_smooth
    plt.plot(x, y)
    # plt.show()


def print_path(x1, y1, theta1, steering, x2, y2, d, delta=0.1):
    distance = 0
    x, y, theta = x1, y1, theta1
    x_print = [x1]
    y_print = [y1]
    while distance < d:
        distance += delta
        newx, newy, theta, steering, distance = get_point(x, y, theta1, steering, distance)
        print newx, newy, theta, steering, distance
        x_print.append(newx)
        y_print.append(newy)
    if x2 != x_print[-1] and y2 != y_print[-1]:
        x_print.append(x2)
        y_print.append(y2)
    smoothly_print_points(x_print, y_print)


x, y, theta, steering, distance = 0., 0., 0., 0.2, 10.

x, y, theta = 0., 0., 0.
actions = [(0.2, 10.), (0.8, 40.), (-0.9, 20), (-0.5, 20), (-0.1, 30)]

# print_path(x, y, theta, steering, 29.5398545262, 4.52594328886, 20)

# for i in range(10):
#     x, y, theta, steering, distance = get_point(x, y, theta, steering, distance)
#     print x, y, theta, steering, distance


if __name__ == "__main__":
    for action in actions:
        x2, y2, theta2, steering, distance = get_point(x, y, theta, action[0], action[1])
        print 'np'
        print x2, y2, theta2, steering, distance
        print_path(x, y, theta, action[0], x2, y2, distance)
        x, y, theta = x2, y2, theta2
    # plt.plot(args)
    plt.show()
