'''
/ this code can read TXT files and CSV files and makes house an battery objects with the
/ information from the rows
'''

import csv
import operator
import classes

def readtxt(txtfile):
    with open(txtfile, newline='') as batterijen1:
        readCSV = csv.reader(batterijen1, delimiter=']')
        next(readCSV, None)

        battery_list = []
        for row in readCSV:
            parts = row[0].split(',')
            battery = classes.Battery(int(parts[0].strip()[1:]), int(parts[1].strip()), float(row[1].strip()))
            battery_list.append(battery)

        return battery_list


def readcsv(csvfile):
    with open(csvfile) as wijk1:
        readCSV = csv.reader(wijk1, delimiter=',')
        next(readCSV)

        house_list = []
        for row in readCSV:
            house = classes.House(int(row[0]), int(row[1]), float(row[2]))
            house_list.append(house)

        return house_list


def match_with_house(house, battery):
    if house.output < battery.capacity:
        return True
    else:
        return False


def connect_to_battery(house, battery, cable_list, batteries, houses):
    # cable loops through x
    connected = 0
    while cable_list[-1].pos_x != batteries[battery].pos_x:
        if cable_list[-1].pos_x < batteries[battery].pos_x:
            cable = classes.Cable(cable_list[-1].pos_x + 1, cable_list[-1].pos_y, battery)
            cable_list.append(cable)

        elif cable_list[-1].pos_x > batteries[battery].pos_x:
            cable = classes.Cable(cable_list[-1].pos_x - 1, cable_list[-1].pos_y, battery)
            cable_list.append(cable)

    # cable loops through y
    while cable_list[-1].pos_y != batteries[battery].pos_y:
        if cable_list[-1].pos_y < batteries[battery].pos_y:
            cable = classes.Cable(cable_list[-1].pos_x, cable_list[-1].pos_y + 1, battery)
            cable_list.append(cable)

        elif cable_list[-1].pos_y > batteries[battery].pos_y:
            cable = classes.Cable(cable_list[-1].pos_x, cable_list[-1].pos_y - 1, battery)
            cable_list.append(cable)

    if cable_list[-1].pos_y == batteries[battery].pos_y and cable_list[-1].pos_x == batteries[battery].pos_x:
        connected += 1
        batteries[battery].capacity -= houses[house].output
        # houses[house].output -= houses[house].output

    return cable_list


def reconnect_to_battery(house, battery, second_battery, cable_list, batteries, houses):
    # cable loops through x
    connected = 0
    while cable_list[houses[house]].pos_x != batteries[battery].pos_x:
        if cable_list[houses[house]].pos_x < batteries[battery].pos_x:
            cable = classes.Cable(cable_list[houses[house]].pos_x + 1, cable_list[houses[house]].pos_y, battery)
            cable_list.remove(cable)
            cable_list[houses[house]].pos_x += 1

        elif cable_list[houses[house]].pos_x > batteries[battery].pos_x:
            cable = classes.Cable(cable_list[houses[house]].pos_x - 1, cable_list[houses[house]].pos_y, battery)
            cable_list.remove(cable)
            cable_list[houses[house]].pos_x -= 1

    # cable loops through y
    while cable_list[houses[house]].pos_y != batteries[battery].pos_y:
        if cable_list[houses[house]].pos_y < batteries[battery].pos_y:
            cable = classes.Cable(cable_list[houses[house]].pos_x, cable_list[houses[house]].pos_y + 1, battery)
            cable_list.remove(cable)
            cable_list[houses[house]].pos_y += 1

        elif cable_list[houses[house]].pos_y > batteries[battery].pos_y:
            cable = classes.Cable(cable_list[houses[house]].pos_x, cable_list[houses[house]].pos_y - 1, battery)
            cable_list.remove(cable)
            cable_list[houses[house]].pos_y -= 1

    if cable_list[houses[house]].pos_y == batteries[battery].pos_y and cable_list[houses[house]].pos_x == batteries[battery].pos_x:
        connected -= 1
        batteries[battery].capacity += houses[house].output

    while cable_list[-1].pos_x != batteries[battery].pos_x:
        if cable_list[-1].pos_x < batteries[battery].pos_x:
            cable = classes.Cablecable_list[-1].pos_x + 1, cable_list[-1].pos_y, battery)
            cable_list.append(cable)

        elif cable_list[-1].pos_x > batteries[battery].pos_x:
            cable = classes.Cablecable_list[-1].pos_x - 1, cable_list[-1].pos_y, battery)
            cable_list.append(cable)

    # cable loops through y
    while cable_list[-1].pos_y != batteries[battery].pos_y:
        if cable_list[-1].pos_y < batteries[battery].pos_y:
            cable = classes.Cablecable_list[-1].pos_x, cable_list[-1].pos_y + 1, battery)
            cable_list.append(cable)

        elif cable_list[-1].pos_y > batteries[battery].pos_y:
            cable = classes.Cablecable_list[-1].pos_x, cable_list[-1].pos_y - 1, battery)
            cable_list.append(cable)

    if cable_list[-1].pos_y == batteries[battery].pos_y and cable_list[-1].pos_x == batteries[battery].pos_x:
        connected += 1
        batteries[battery].capacity -= houses[house].output
        houses[house].output -= houses[house].output


def second_smallest(lst):
    lst.sort()
    return lst[1]


def third_smallest(lst):
    lst.sort()
    return lst[2]


def fourth_smallest(lst):
    lst.sort()
    return lst[4]


def distance_sort(batteries, houses):
    distances = []
    for j in range(len(houses)):
        distance = {}
        for i in range(len(batteries)):
            dis = (abs(houses[j].pos_x - batteries[i].pos_x) + abs(houses[j].pos_y - batteries[i].pos_y))
            distance[i] = dis
        sorted_distance = sorted(distance.items(), key=operator.itemgetter(1))
        distances.append(sorted_distance)

    return distances


def sort_houses(houses):
    distance = {}
    for i in range(len(houses)):
        dis = (abs(houses[i].pos_x - 25) + abs(houses[i].pos_y - 25))
        distance[i] = dis

    sorted_distance = sorted(distance.items(), key=operator.itemgetter(1), reverse=True)

    return sorted_distance


def sort_on_battery_distance(batteries, houses):
    distances = []
    for j in range(len(houses)):
        distance = []
        for i in range(len(batteries)):
            dis = (abs(houses[j].pos_x - batteries[i].pos_x) + abs(houses[j].pos_y - batteries[i].pos_y))
            triple = [dis, i, j]
            # distance[dis] = i, j
            distance.append(triple)
        sorted_distance = sorted(distance, key=operator.itemgetter(0))
        distances.append(sorted_distance)

    end_sort = sorted(distances, key=lambda x: x[0][0], reverse=True)
    return end_sort


def connection(sorted_houses, distance, batteries, houses):
    cable_list = []
    cl = []
    connected = 0
    for house in sorted_houses:
        for key in distance[house[0]]:
            if match_with_house(houses[house[0]], batteries[key[0]]) and houses[house[0]].output > 0:
                cable = classes.Cablehouses[house[0]].pos_x, houses[house[0]].pos_y, key[0])
                cable_list.append(cable)
                cl = connect_to_battery(house[0], key[0], cable_list, batteries, houses)
                connected += 1
                break
    return cl


def reset_batteries(batteries):
    for bat in batteries:
        bat.capacity = 1507.0

    return batteries
