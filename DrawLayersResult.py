import DrawBasement
from xml.etree.ElementTree import parse
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def print_single_layer(layer_count, perimeter_count):
    # point = PointPrint(0.5, 0.5)
    # print(point._PointPrint__a)
    g_code_file = open("NewOutput.txt")
    count_total = -1
    count_print_total = 0
    file_perimeter = open("data_perimeter.txt", "w+")
    file_infill = open("data_infill.txt", "w+")
    mark_print = False
    mark_exit = False
    while 1:
        line = g_code_file.readline()
        if not line:
            print("finish!")
            break
        if "G1 Z" in line:
            count_total += 1
            if count_total == layer_count:
                while 1:
                    if "G1 X" in line:
                        file_perimeter.write(line)
                    if "G1 F" in line:
                        count_print_total += 1
                        if count_print_total <= perimeter_count:
                            while 1:
                                line = g_code_file.readline()
                                if "G1 F" in line:
                                    # count_print_total += 1
                                    mark_print = True
                                    break
                                if "G1 X" in line:
                                    file_perimeter.write(line)
                        if count_print_total == perimeter_count + 1:
                            while 1:
                                line = g_code_file.readline()
                                if "G1 Z" in line:
                                    mark_exit = True
                                    break
                                if "G1 X" in line:
                                    file_infill.write(line)
                    if mark_exit:
                        file_perimeter.close()
                        file_infill.close()
                        print("finish!")
                        return
                    if not mark_print:
                        line = g_code_file.readline()


def print_all_layers(perimeter_count):
    # point = PointPrint(0.5, 0.5)
    # print(point._PointPrint__a)
    g_code_file = open("NewOutput.txt")
    count_total = -1
    height = 0.0
    height_next = 0.0
    count_print_total = 0
    file_perimeter = open("data_perimeter.txt", "w+")
    file_infill = open("data_infill.txt", "w+")
    mark_print = False
    mark_exit = False
    mark_return = False
    draw_x_list_perimeter = []
    draw_y_list_perimeter = []
    draw_z_list_perimeter = []
    draw_x_list_infill = []
    draw_y_list_infill = []
    draw_z_list_infill = []
    while 1:
        line = g_code_file.readline()
        if not line:
            print("finish!")
            break
        if "G1 Z" in line:
            count_total += 1
            if count_total >= 1:
                height_string = line.split(" ")[1]
                height = float(height_string[1: len(height_string)])
                while 1:
                    if "G1 X" in line:
                        file_perimeter.write(line)
                    if "G1 F" in line:
                        count_print_total += 1
                        if count_print_total <= perimeter_count:
                            while 1:
                                line = g_code_file.readline()
                                if "G1 F" in line:
                                    # count_print_total += 1
                                    mark_print = True
                                    break
                                if "G1 X" in line:
                                    file_perimeter.write(line)
                        if count_print_total == perimeter_count + 1:
                            while 1:
                                line = g_code_file.readline()
                                if "M140 S0" in line:
                                    mark_return = True
                                    break
                                if "G1 Z" in line:
                                    mark_exit = True
                                    height_string = line.split(" ")[1]
                                    height_next = float(height_string[1: len(height_string)])
                                    break
                                if "G1 X" in line:
                                    file_infill.write(line)
                    if mark_exit:
                        file_perimeter.close()
                        file_infill.close()
                        draw_x_list_perimeter, draw_y_list_perimeter, \
                            draw_z_list_perimeter, draw_x_list_infill, \
                            draw_y_list_infill, draw_z_list_infill = \
                            DrawBasement.draw_all_layer(height, draw_x_list_perimeter, draw_y_list_perimeter,
                                                        draw_z_list_perimeter, draw_x_list_infill,
                                                        draw_y_list_infill, draw_z_list_infill)
                        print("finish one layer!")
                        file_perimeter = open("data_perimeter.txt", "w+")
                        file_infill = open("data_infill.txt", "w+")
                        mark_print = False
                        mark_exit = False
                        count_print_total = 0
                        height = height_next
                        continue
                    if not mark_print:
                        line = g_code_file.readline()
                    if mark_return:
                        break
        if mark_return:
            break
    dict_store = {'draw_x_list_perimeter': draw_x_list_perimeter,
                  'draw_y_list_perimeter': draw_y_list_perimeter,
                  'draw_z_list_perimeter': draw_z_list_perimeter,
                  'draw_x_list_infill': draw_x_list_infill,
                  'draw_y_list_infill': draw_y_list_infill,
                  'draw_z_list_infill': draw_z_list_infill}
    DrawBasement.draw_all_layers_main(dict_store)


if __name__ == '__main__':
    et = parse("printParameters.xml")
    root = et.getroot()
    print(root)
    et_print = root.findall('entry[@key="shellLayers"]')[0]
    data = int(et_print.text)
    print_single_layer(2, data)
    DrawBasement.draw_single_layer(2)
    print_all_layers(3)
