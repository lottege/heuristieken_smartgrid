'''
/ this code can read CSV files and makes house objects with the
/ information from the rows
'''

import csv


class House:
    number = 0

    def __init__(self, pos_x, pos_y, output):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.output = output
        House.number += 1


if __name__ == '__main__':

    with open('wijk1_huizen.csv') as wijk1:
        readCSV = csv.reader(wijk1, delimiter=',')

        house_list = []
        for row in readCSV:
            house = House(row[0], row[1], row[2])
            house_list.append(house)


print("x-coordinate: {}\ny-coordinate: {}\noutput: {}".format(house_list[5].pos_x, house_list[5].pos_y, house_list[5].output))





