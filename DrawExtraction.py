import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def draw_triangles():
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_title("Tradition 3D Model")
    file_print = open("singlePointList.txt")
    x_print_final, y_print_final, z_print_final = [], [], []
    count_print_final = 0
    while 1:
        line = file_print.readline()
        if not line:
            break
        if line == "-1\n":
            ax.plot(x_print_final, y_print_final, z_print_final, 'red')
            x_print_final, y_print_final, z_print_final = [], [], []
            continue
        line_list = line.split(" ")
        x_print_final.insert(count_print_final, float(line_list[0]))
        y_print_final.insert(count_print_final, float(line_list[1]))
        z_print_final.insert(count_print_final, float(line_list[2]))
        count_print_final += 1
    plt.show()
    return


if __name__ == '__main__':
    draw_triangles()
