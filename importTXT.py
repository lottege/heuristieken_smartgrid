'''
/ this code can read TXT files and makes house objects with the
/ information from the rows
/
'''

import csv


class Battery:
    number = 0

    def __init__(self, pos_x, pos_y, capacity):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.capacity = capacity
        Battery.number += 1


if __name__ == '__main__':

    with open('wijk1_batterijen.txt', newline='') as batterijen1:
        readCSV = csv.reader(batterijen1, delimiter=']')
        next(readCSV, None)

        battery_list = []
        for row in readCSV:
            parts = row[0].split(',')
            battery = Battery(parts[0].strip()[1:], parts[1].strip(), row[1].strip())
            battery_list.append(battery)

for i in range(Battery.number):
    print("1: x-pos: {}, y-pos: {}, capacity: {}".format(battery_list[i].pos_x, battery_list[i].pos_y, battery_list[i].capacity))
