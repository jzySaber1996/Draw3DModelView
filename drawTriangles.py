import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def draw_triangles():
    file = open("pointlist.txt")
    count_triangle = 0
    result_x, result_y, result_z = [], [], []
    x_list, y_list, z_list = [], [], []
    while 1:
        line = file.readline()
        if not line:
            break
        if line == "-1\n":
            continue
        number_list = line.split(" ")
        count_triangle += 1
        # count_triangle = {
        #     # 1:
        # }
        x_list.insert(count_triangle - 1, float(number_list[0]))
        y_list.insert(count_triangle - 1, float(number_list[1]))
        z_list.insert(count_triangle - 1, float(number_list[2]))
        if count_triangle == 3:
            result_x.insert(len(result_x), x_list)
            result_y.insert(len(result_y), y_list)
            result_z.insert(len(result_z), z_list)
            x_list, y_list, z_list = [], [], []
            count_triangle = 0
    # print(x_list)
    list_index = [[0, 1], [1, 2], [2, 0]]
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_title("Tradition 3D Model")
    for i in range(len(result_x)):
        for j in range(len(list_index)):
            x_print, y_print, z_print = [], [], []
            x_print.insert(0, result_x[i][list_index[j][0]])
            x_print.insert(1, result_x[i][list_index[j][1]])
            y_print.insert(0, result_y[i][list_index[j][0]])
            y_print.insert(1, result_y[i][list_index[j][1]])
            z_print.insert(0, result_z[i][list_index[j][0]])
            z_print.insert(1, result_z[i][list_index[j][1]])
            ax.plot(x_print, y_print, z_print, 'aqua')
    plt.show()
    return


if __name__ == '__main__':
    draw_triangles()
