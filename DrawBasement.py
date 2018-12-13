import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def draw_single_layer(height):
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
    plt.plot(list_x, list_y, 'red')

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
    plt.plot(list_x, list_y, 'aqua')
    plt.show()


# draw_single_layer()
def draw_all_layer(height, draw_x_list_perimeter, draw_y_list_perimeter, draw_z_list_perimeter,
                   draw_x_list_infill, draw_y_list_infill, draw_z_list_infill):
    list_x = []
    list_y = []
    list_z = []
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
            list_z.insert(count, height)
            count += 1
    x_last = list_x[len(list_x) - 1]
    y_last = list_y[len(list_y) - 1]
    z_last = list_z[len(list_z) - 1]
    del list_x[len(list_x) - 1]
    del list_y[len(list_y) - 1]
    del list_z[len(list_z) - 1]
    draw_x_list_perimeter.insert(len(draw_x_list_perimeter), list_x)
    draw_y_list_perimeter.insert(len(draw_y_list_perimeter), list_y)
    draw_z_list_perimeter.insert(len(draw_z_list_perimeter), list_z)

    list_x = []
    list_y = []
    list_z = []
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
            z = height
            # z = float(res[])
            list_x.insert(count, x)
            list_y.insert(count, y)
            list_z.insert(count, z)
            count += 1
    list_x.insert(0, x_last)
    list_y.insert(0, y_last)
    list_z.insert(0, z_last)

    draw_x_list_infill.insert(len(draw_x_list_infill), list_x)
    draw_y_list_infill.insert(len(draw_y_list_infill), list_y)
    draw_z_list_infill.insert(len(draw_z_list_infill), list_z)
    return draw_x_list_perimeter, draw_y_list_perimeter, draw_z_list_perimeter, \
        draw_x_list_infill, draw_y_list_infill, draw_z_list_infill


def draw_all_layers_main(dict_store):
    draw_x_list_perimeter = dict_store['draw_x_list_perimeter']
    draw_y_list_perimeter = dict_store['draw_y_list_perimeter']
    draw_z_list_perimeter = dict_store['draw_z_list_perimeter']
    draw_x_list_infill = dict_store['draw_x_list_infill']
    draw_y_list_infill = dict_store['draw_y_list_infill']
    draw_z_list_infill = dict_store['draw_z_list_infill']
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_title("3D Model")
    for i in range(len(draw_x_list_perimeter)):
        listx = draw_x_list_perimeter[i]
        listy = draw_y_list_perimeter[i]
        listz = draw_z_list_perimeter[i]
        ax.plot(listx, listy, listz, 'red')
    for i in range(len(draw_x_list_infill)):
        listx = draw_x_list_infill[i]
        listy = draw_y_list_infill[i]
        listz = draw_z_list_infill[i]
        ax.plot(listx, listy, listz, 'aqua')
    plt.show()
