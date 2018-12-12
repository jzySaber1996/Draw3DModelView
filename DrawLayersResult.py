import DrawBasement
from xml.etree.ElementTree import parse


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


if __name__ == '__main__':
    et = parse("printParameters.xml")
    root = et.getroot()
    print(root)
    et_print = root.findall('entry[@key="shellLayers"]')[0]
    data = int(et_print.text)
    print_single_layer(30, data)
    DrawBasement.draw_single_layer()
