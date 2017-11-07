'''
/ this code can read TXT files and CSV files and makes house an battery objects with the
/ information from the rows
'''

import csv


class Battery:
    number = 0

    def __init__(self, pos_x, pos_y, capacity):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.capacity = capacity
        Battery.number += 1


class House:
    number = 0

    def __init__(self, pos_x, pos_y, output):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.output = output
        House.number += 1


def readtxt(txtfile):
    with open(txtfile, newline='') as batterijen1:
        readCSV = csv.reader(batterijen1, delimiter=']')
        next(readCSV, None)

        battery_list = []
        for row in readCSV:
            parts = row[0].split(',')
            battery = Battery(int(parts[0].strip()[1:]), int(parts[1].strip()), float(row[1].strip()))
            battery_list.append(battery)

        return battery_list


def readcsv(csvfile):
    with open(csvfile) as wijk1:
        readCSV = csv.reader(wijk1, delimiter=',')
        next(readCSV)

        house_list = []
        for row in readCSV:
            house = House(int(row[0]), int(row[1]), float(row[2]))
            house_list.append(house)

        return house_list


batteries = readtxt("wijk1_batterijen.txt")
houses = readcsv("wijk1_huizen.csv")


def match_with_house(house_number, battery_number):
    if houses[house_number].output < batteries[battery_number].capacity:
        batteries[battery_number].capacity -= houses[house_number].output
        return True
    else:
        return False


match_with_house(4, 3)
