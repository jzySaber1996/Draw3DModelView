import numpy as np
import matplotlib.pyplot as plt


def draw_single_layer():
    list_x = []
    list_y = []
    count = 0
    file2 = open("data_perimeter.txt")
    while 1:
        line = file2.readline()
        if not line:
            break
        if "X" in line and "Y" in line:
            res = line.split()
            x = float(res[1][1:])
            y = float(res[2][1:])
            list_x.insert(count, x)
            list_y.insert(count, y)
            count += 1
    x_last = list_x[len(list_x) - 1]
    y_last = list_y[len(list_y) - 1]
    del list_x[len(list_x) - 1]
    del list_y[len(list_y) - 1]
    plt.plot(list_x, list_y)

    list_x = []
    list_y = []
    count = 0
    file = open("data_infill.txt")
    while 1:
        line = file.readline()
        if not line:
            break
        if "X" in line and "Y" in line:
            res = line.split()
            x = float(res[1][1:])
            y = float(res[2][1:])
            list_x.insert(count, x)
            list_y.insert(count, y)
            count += 1
    list_x.insert(0, x_last)
    list_y.insert(0, y_last)
    plt.plot(list_x, list_y)
    plt.show()


# draw_single_layer()
