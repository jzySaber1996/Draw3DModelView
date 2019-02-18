import numpy as np
import matplotlib.pyplot as plt

str_print = "(61.75,26.375)->(62.0,26.375)->(62.25,26.375)->(62.5,26.375)->(62.75,26.375)->(62.875,26.5)->(63.0,26.625)->(63.25,26.625)->(63.5,26.625)->(63.75,26.625)->(64.0,26.625)->(64.25,26.625)->(64.375,26.5)->(64.5,26.375)->(64.75,26.375)->(65.0,26.375)->(65.25,26.375)->(65.5,26.375)->(65.75,26.375)->(66.0,26.375)->(66.125,26.25)->(66.25,26.125)->(66.5,26.125)->(66.625,26.0)->(66.75,25.875)->(67.0,25.875)->(67.25,25.875)->(67.375,25.75)->(67.5,25.625)->(67.75,25.625)->(67.875,25.5)->(68.0,25.375)->(68.125,25.25)->(68.25,25.125)->(68.375,25.0)->(68.5,24.875)->(68.625,24.75)->(68.75,24.625)->(68.875,24.5)->(69.0,24.375)->(69.125,24.25)->(69.25,24.125)->(69.375,24.0)->(69.5,23.875)->(69.625,23.75)->(69.75,23.625)->(69.875,23.5)->(69.875,23.25)->(70.0,23.125)->(70.125,23.0)->(70.125,22.75)->(70.125,22.5)->(70.25,22.375)->(70.375,22.25)->(70.375,22.0)->(70.375,21.75)->(70.375,21.5)->(70.375,21.25)->(70.375,21.0)->(70.375,20.75)->(70.375,20.5)->(70.375,20.25)->(70.375,20.0)->(70.25,19.875)->(70.125,19.75)->(70.125,19.5)->(70.0,19.375)->(69.875,19.25)->(69.875,19.0)->(69.75,18.875)->(69.625,18.75)->(69.625,18.5)->(69.5,18.375)->(69.375,18.25)->(69.25,18.125)->(69.125,18.0)->(69.0,17.875)->(68.875,17.75)->(68.75,17.625)->(68.625,17.5)->(68.5,17.375)->(68.375,17.25)->(68.25,17.125)->(68.125,17.0)->(68.0,16.875)->(67.875,16.75)->(67.75,16.625)->(67.5,16.625)->(67.375,16.5)->(67.25,16.375)->(67.0,16.375)->(66.875,16.25)->(66.75,16.125)->(66.5,16.125)->(66.25,16.125)->(66.125,16.0)->(66.0,15.875)->(65.75,15.875)->(65.5,15.875)->(65.25,15.875)->(65.0,15.875)->(64.875,15.75)->(64.75,15.625)->(64.5,15.625)->(64.25,15.625)->(64.0,15.625)->(63.75,15.625)->(63.5,15.625)->(63.25,15.625)->(63.0,15.625)->(62.875,15.75)->(62.75,15.875)->(62.5,15.875)->(62.25,15.875)->(62.0,15.875)->(61.875,16.0)->(61.75,16.125)->(61.5,16.125)->(61.375,16.25)->(61.25,16.375)->(61.0,16.375)->(60.875,16.5)->(60.75,16.625)->(60.5,16.625)->(60.375,16.75)->(60.25,16.875)->(60.125,17.0)->(60.0,17.125)->(59.875,17.25)->(59.75,17.375)->(59.5,17.375)->(59.375,17.5)->(59.25,17.625)->(59.125,17.75)->(59.0,17.875)->(58.875,18.0)->(58.75,18.125)->(58.625,18.25)->(58.5,18.375)->(58.375,18.5)->(58.375,18.75)->(58.25,18.875)->(58.125,19.0)->(58.0,19.125)->(57.875,19.25)->(57.75,19.375)->(57.625,19.5)->(57.625,19.75)->(57.5,19.875)->(57.375,20.0)->(57.375,20.25)->(57.25,20.375)->(57.125,20.5)->(57.125,20.75)->(57.0,20.875)->(56.875,21.0)->(56.875,21.25)->(56.75,21.375)->(56.625,21.5)->(56.625,21.75)->(56.5,21.875)->(56.375,22.0)->(56.375,22.25)->(56.375,22.5)->(56.25,22.625)->(56.125,22.75)->(56.125,23.0)->(56.0,23.125)->(55.875,23.25)->(55.875,23.5)->(55.75,23.625)->(55.625,23.75)->(55.625,24.0)->(55.5,24.125)->(55.375,24.25)->(55.375,24.5)->(55.375,24.75)->(55.25,24.875)->(55.125,25.0)->(55.125,25.25)->(55.0,25.375)->(54.875,25.5)->(54.875,25.75)->(54.75,25.875)->(54.625,26.0)->(54.625,26.25)->(54.625,26.5)->(54.625,26.75)->(54.5,26.875)->(54.375,27.0)->(54.375,27.25)->(54.375,27.5)->(54.25,27.625)->(54.125,27.75)->(54.125,28.0)->(54.125,28.25)->(54.125,28.5)->(54.125,28.75)->(54.0,28.875)->(53.875,29.0)->(54.0,29.125)->(54.125,29.25)->(54.125,29.5)->(54.125,29.75)->(54.125,30.0)->(54.25,30.125)->(54.375,30.25)->(54.5,30.375)->(54.75,30.375)->(55.0,30.375)->(55.25,30.375)->(55.5,30.375)->(55.625,30.25)->(55.75,30.125)->(56.0,30.125)->(56.25,30.125)->(56.375,30.0)->(56.5,29.875)->(56.625,29.75)->(56.75,29.625)->(57.0,29.625)->(57.125,29.5)->(57.25,29.375)->(57.375,29.25)->(57.5,29.125)->(57.625,29.0)->(57.75,28.875)->(57.875,28.75)->(58.0,28.625)->(58.125,28.5)->(58.25,28.375)->(58.375,28.25)->(58.5,28.125)->(58.625,28.0)->(58.75,27.875)->(59.0,27.875)->(59.125,27.75)->(59.25,27.625)->(59.375,27.5)->(59.5,27.375)->(59.625,27.25)->(59.75,27.125)->(59.875,27.0)->(60.0,26.875)->(60.25,26.875)->(60.375,26.75)->(60.5,26.625)->(60.75,26.625)->(61.0,26.625)->(61.25,26.625)->(61.5,26.625)->(61.625,26.5)->(61.75,26.375)"
str_print_next = "(45.625,42.25)->(45.75,42.125)->(45.875,42.0)->(45.875,41.75)->(46.0,41.625)->(46.125,41.5)->(46.125,41.25)->(46.25,41.125)->(46.375,41.0)->(46.5,40.875)->(46.625,40.75)->(46.625,40.5)->(46.75,40.375)->(46.875,40.25)->(46.875,40.0)->(47.0,39.875)->(47.125,39.75)->(47.125,39.5)->(47.25,39.375)->(47.375,39.25)->(47.5,39.125)->(47.625,39.0)->(47.625,38.75)->(47.75,38.625)->(47.875,38.5)->(48.0,38.375)->(48.125,38.25)->(48.125,38.0)->(48.25,37.875)->(48.375,37.75)->(48.5,37.625)->(48.625,37.5)->(48.75,37.375)->(48.875,37.25)->(48.875,37.0)->(49.0,36.875)->(49.125,36.75)->(49.25,36.625)->(49.375,36.5)->(49.5,36.375)->(49.625,36.25)->(49.75,36.125)->(49.875,36.0)->(50.0,35.875)->(50.25,35.875)->(50.375,35.75)->(50.5,35.625)->(50.625,35.5)->(50.75,35.375)->(50.875,35.25)->(51.0,35.125)->(51.125,35.25)->(51.25,35.375)->(51.375,35.5)->(51.375,35.75)->(51.5,35.875)->(51.625,36.0)->(51.625,36.25)->(51.625,36.5)->(51.625,36.75)->(51.625,37.0)->(51.625,37.25)->(51.625,37.5)->(51.625,37.75)->(51.625,38.0)->(51.5,38.125)->(51.375,38.25)->(51.375,38.5)->(51.375,38.75)->(51.375,39.0)->(51.375,39.25)->(51.375,39.5)->(51.25,39.625)->(51.125,39.75)->(51.125,40.0)->(51.125,40.25)->(51.0,40.375)->(50.875,40.5)->(50.875,40.75)->(50.875,41.0)->(50.75,41.125)->(50.625,41.25)->(50.625,41.5)->(50.625,41.75)->(50.5,41.875)->(50.375,42.0)->(50.375,42.25)->(50.375,42.5)->(50.25,42.625)->(50.125,42.75)->(50.125,43.0)->(50.0,43.125)->(49.875,43.25)->(49.875,43.5)->(49.875,43.75)->(49.75,43.875)->(49.625,44.0)->(49.625,44.25)->(49.5,44.375)->(49.375,44.5)->(49.375,44.75)->(49.25,44.875)->(49.125,45.0)->(49.125,45.25)->(49.0,45.375)->(48.875,45.5)->(48.75,45.625)->(48.625,45.75)->(48.625,46.0)->(48.5,46.125)->(48.375,46.25)->(48.375,46.5)->(48.25,46.625)->(48.125,46.75)->(48.0,46.875)->(47.875,47.0)->(47.75,47.125)->(47.625,47.25)->(47.625,47.5)->(47.5,47.625)->(47.375,47.75)->(47.25,47.875)->(47.125,48.0)->(47.0,48.125)->(46.875,48.25)->(46.75,48.375)->(46.625,48.5)->(46.5,48.625)->(46.375,48.75)->(46.25,48.875)->(46.0,48.875)->(45.875,49.0)->(45.75,49.125)->(45.5,49.125)->(45.375,49.25)->(45.25,49.375)->(45.0,49.375)->(44.75,49.375)->(44.5,49.375)->(44.25,49.375)->(44.0,49.375)->(43.875,49.25)->(43.875,49.0)->(43.75,48.875)->(43.625,48.75)->(43.625,48.5)->(43.625,48.25)->(43.625,48.0)->(43.625,47.75)->(43.625,47.5)->(43.625,47.25)->(43.625,47.0)->(43.75,46.875)->(43.875,46.75)->(43.875,46.5)->(43.875,46.25)->(44.0,46.125)->(44.125,46.0)->(44.125,45.75)->(44.125,45.5)->(44.25,45.375)->(44.375,45.25)->(44.375,45.0)->(44.5,44.875)->(44.625,44.75)->(44.625,44.5)->(44.625,44.25)->(44.75,44.125)->(44.875,44.0)->(44.875,43.75)->(45.0,43.625)->(45.125,43.5)->(45.125,43.25)->(45.25,43.125)->(45.375,43.0)->(45.375,42.75)->(45.5,42.625)->(45.625,42.5)->(45.625,42.25)"
list_print = str_print.split(")->(")
list_print[0] = list_print[0][1:]
list_print[-1] = list_print[-1][:-1]
print_last = list_print[-1]
list_x = []
list_y = []
count_index = 0
for print_element in list_print:
    print_coordinate = print_element.split(",")
    list_x.insert(count_index, float(print_coordinate[0]))
    list_y.insert(count_index, float(print_coordinate[1]))
    count_index += 1
# print(list_print)
plt.plot(list_x, list_y, 'aqua')

list_print = str_print_next.split(")->(")
list_print[0] = list_print[0][1:]
list_print[-1] = list_print[-1][:-1]
print_last = list_print[-1]
list_x = []
list_y = []
count_index = 0
for print_element in list_print:
    print_coordinate = print_element.split(",")
    list_x.insert(count_index, float(print_coordinate[0]))
    list_y.insert(count_index, float(print_coordinate[1]))
    count_index += 1
# print(list_print)
plt.plot(list_x, list_y, 'aqua')
plt.show()