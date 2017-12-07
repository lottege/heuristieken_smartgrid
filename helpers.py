'''
/ this code can read TXT files and CSV files and makes house an battery objects with the
/ information from the rows
'''

import csv
import operator

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
        self.battery = 0


class Cable:
    def __init__(self, pos_x, pos_y, battery_nr):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.battery_nr = battery_nr


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
            cable = Cable(cable_list[-1].pos_x + 1, cable_list[-1].pos_y, battery)
            cable_list.append(cable)

        elif cable_list[-1].pos_x > batteries[battery].pos_x:
            cable = Cable(cable_list[-1].pos_x - 1, cable_list[-1].pos_y, battery)
            cable_list.append(cable)

    # cable loops through y
    while cable_list[-1].pos_y != batteries[battery].pos_y:
        if cable_list[-1].pos_y < batteries[battery].pos_y:
            cable = Cable(cable_list[-1].pos_x, cable_list[-1].pos_y + 1, battery)
            cable_list.append(cable)

        elif cable_list[-1].pos_y > batteries[battery].pos_y:
            cable = Cable(cable_list[-1].pos_x, cable_list[-1].pos_y - 1, battery)
            cable_list.append(cable)

    if cable_list[-1].pos_y == batteries[battery].pos_y and cable_list[-1].pos_x == batteries[battery].pos_x:
        connected += 1
        batteries[battery].capacity -= houses[house].output
        houses[house].output -= houses[house].output

    houses[house].battery = battery
    return cable_list


def switch_houses(house, second_house, battery, second_battery, cable_list, batteries):
    connected = 0

    house_pointer = house
    battery_pointer = battery

    if battery.capacity + house.output >= second_house.output and second_battery.capacity + second_house.output >= house.output and battery != second_battery:

    # disconnects battery
    # cable loops through x
        change = cable_list.remove
        k = 0
        for i in range(2):
            for j in range(2):
                while house_pointer.pos_x != battery_pointer.pos_x:
                    if house_pointer.pos_x < battery_pointer.pos_x:
                        while house_pointer.pos_x < battery_pointer.pos_x:
                            if cable_list[k].pos_x is house_pointer.pos_x and cable_list[k].pos_y is house_pointer.pos_y:
                                # print(cable_list[k].pos_x, house_pointer.pos_x, cable_list[k].pos_y, house_pointer.pos_y)
                                change(cable_list[k])
                                house_pointer.pos_x += 1
                                k -=1
                                # if cable_list[k].pos_x is not house_pointer.pos_x:
                                #     break
                            k += 1
                            if k == len(cable_list):
                                k = 0

                    elif house_pointer.pos_x > battery_pointer.pos_x:
                        while house_pointer.pos_x > battery_pointer.pos_x:
                            if cable_list[k].pos_x is house_pointer.pos_x and cable_list[k].pos_y is house_pointer.pos_y:
                                # print(cable_list[k].pos_x, house_pointer.pos_x, cable_list[k].pos_y, house_pointer.pos_y)
                                change(cable_list[k])
                                house_pointer.pos_x -= 1
                                k -=1
                                # if cable_list[k].pos_x is not house_pointer.pos_x:
                                #     break
                            k += 1
                            if k == len(cable_list):
                                k = 0

            # cable loops through y
                while house_pointer.pos_y != battery_pointer.pos_y:
                    if house_pointer.pos_y < battery_pointer.pos_y:
                        while house_pointer.pos_y < battery_pointer.pos_y:
                            if cable_list[k].pos_x is house_pointer.pos_x and cable_list[k].pos_y is house_pointer.pos_y:
                                # print(cable_list[k].pos_x, house_pointer.pos_x, cable_list[k].pos_y, house_pointer.pos_y)
                                change(cable_list[k])
                                house_pointer.pos_y += 1
                                k -=1
                                # if cable_list[k].pos_y is not house_pointer.pos_y:
                                #     break
                            k += 1
                            if k == len(cable_list):
                                k = 0

                    elif house_pointer.pos_y > battery_pointer.pos_y:
                        while house_pointer.pos_y > battery_pointer.pos_y:
                            if cable_list[k].pos_x is house_pointer.pos_x and cable_list[k].pos_y is house_pointer.pos_y:
                                # print(cable_list[k].pos_x, house_pointer.pos_x, cable_list[k].pos_y, house_pointer.pos_y)
                                change(cable_list[k])
                                house_pointer.pos_y -= 1
                                k -= 1
                                # if cable_list[k].pos_y is not house_pointer.pos_y:
                                #     break
                            k += 1
                            if k == len(cable_list):
                                k = 0

                if house_pointer.pos_y == battery_pointer.pos_y and house_pointer.pos_x == battery_pointer.pos_x and i is 0:
                    connected -= 1
                    # print("disconnected", house_pointer.pos_x, battery_pointer.pos_x, house_pointer.pos_y, battery_pointer.pos_y)
                    if j is 0:
                        battery.capacity += house.output
                        battery_pointer = second_battery
                        house_pointer = second_house
                    elif j is 1:
                        second_battery.capacity += second_house.output
                        house_pointer = house
                        change = cable_list.append


                elif house_pointer.pos_y == battery_pointer.pos_y and house_pointer.pos_x == battery_pointer.pos_x and i is 1:
                    connected += 1
                    # print("connected", house_pointer.pos_x, battery_pointer.pos_x, house_pointer.pos_y, battery_pointer.pos_y)
                    if j is 0:
                        second_battery.capacity -= house.output
                        battery_pointer = battery
                        house_pointer = second_house
                    elif j is 1:
                        battery.capacity -= second_house.output

                # else:
                    # print("not connected: ", house_pointer.pos_x, battery_pointer.pos_x, house_pointer.pos_y, battery_pointer.pos_y)

        return True
    else:
        return False


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
                cable = Cable(houses[house[0]].pos_x, houses[house[0]].pos_y, key[0])
                cable_list.append(cable)
                cl = connect_to_battery(house[0], key[0], cable_list, batteries, houses)
                connected += 1
                break
    return cl


def reset_batteries(batteries):
    for bat in batteries:
        bat.capacity = 1507.0

    return batteries
