'''
/ this code can read TXT files and CSV files and makes house an battery objects with the
/ information from the rows
'''

import csv
import operator
import classes
from copy import deepcopy
import random

Cable = classes.Cable
House = classes.House
Battery= classes.Battery

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

def drain_capacity(house, battery):
    if battery.capacity - house.output > 0:
        battery.capacity -= house.output
        return True
    else:
        # print("Doesn't fit")
        return False

def sure_drain_capacity(house, battery):
    battery.capacity -= house.output

def brute_drain_capacity(house, battery):
    battery.capacity -= house.output
    house.battery = battery.number


def refill_capacity(house, battery):
    battery.capacity += house.output

def update_score(house, battery):
    x = abs(house.pos_x - battery.pos_x) + abs(house.pos_y - battery.pos_y)
    house.battery = battery.number
    # print(x, house.pos_x, house.pos_y, battery.pos_x, battery.pos_y)
    return x

def update_battery_score(house, battery):
    x = abs(house.pos_x - battery.pos_x) + abs(house.pos_y - battery.pos_y)
    # print(x, house.pos_x, house.pos_y, battery.pos_x, battery.pos_y)
    return x



# checks if a switch between houses is possible and beneficial
def check_switch(house, second_house, battery, second_battery):
    # checks if batteries have enough capacity for the switch
    if (battery.capacity + house.output - second_house.output) > 0 and (second_battery.capacity + second_house.output - house.output) > 0:
        # checks if total number of cables goes down if switched
        current_score_house_1 = check_score(house, battery)
        current_score_house_2 = check_score(second_house, second_battery)
        new_score_house_1 = check_score(house, second_battery)
        new_score_house_2 = check_score(second_house, battery)
        if current_score_house_1 + current_score_house_2 > new_score_house_1 + new_score_house_2:
            return True

    return False



def switch_score(house, second_house, battery, second_battery, score):

    # print(battery, second_battery)
    # first_score = score
    # print(battery.capacity)
    refill_capacity(house, battery)
    refill_capacity(second_house, second_battery)
    # print(battery.capacity)
    score -= abs(update_score(house, battery)) + abs(update_score(second_house, second_battery))
    # print(house.battery, second_house.battery)
    drain_capacity(house, second_battery)
    drain_capacity(second_house, battery)
    # print(battery.capacity)
    # print(house.battery, second_house.battery)
    score += abs(update_score(house, second_battery)) + abs(update_score(second_house, battery))
    # print(score)
    # second_score = score
    house.battery = second_battery.number
    second_house.battery = battery.number
    # print(battery, second_battery)
    # print(("must be equal"), first_score - second_score, check_score(house, battery) + check_score(second_house, second_battery) - check_score(house, second_battery) - check_score(second_house, battery))


    return score

def check_score(house, battery):
    return abs(house.pos_x - battery.pos_x) + abs(house.pos_y - battery.pos_y)


def connect_to_battery(house, batteries, cable_list):
    # cable loops through x
    connected = 0

    cable = house.pos_x, house.pos_y, house.battery
    cable_list.append(cable)

    house_pointer = deepcopy(house)

    while house_pointer.pos_x != batteries[house.battery].pos_x:
        if house_pointer.pos_x < batteries[house.battery].pos_x:
            cable = classes.Cable(house_pointer.pos_x + 1, house_pointer.pos_y, house.battery)
            house_pointer.pos_x += 1
            cable_list.append(cable)

        elif house_pointer.pos_x > batteries[house.battery].pos_x:
            cable = classes.Cable(house_pointer.pos_x - 1, house_pointer.pos_y, house.battery)
            house_pointer.pos_x -= 1
            cable_list.append(cable)

    # cable loops through y
    while house_pointer.pos_y != batteries[house.battery].pos_y:
        if house_pointer.pos_y < batteries[house.battery].pos_y:
            cable = Cable(house_pointer.pos_x, house_pointer.pos_y + 1, house.battery)
            house_pointer.pos_y += 1
            cable_list.append(cable)

        elif house_pointer.pos_y > batteries[house.battery].pos_y:
            cable = Cable(house_pointer.pos_x, house_pointer.pos_y - 1, house.battery)
            house_pointer.pos_y -= 1
            cable_list.append(cable)

    # if house_pointer.pos_y == battery.pos_y and house_pointer.pos_x == battery.pos_x:
    connected += 1
    house.output = 0

    # house.battery = battery_nr
    # print(battery)
    # print(len(cable_list))
    return cable_list


def disconnect_from_battery(house, battery, cable_list):

    connected = 0
    k = 0
    q = 0
    house_pointer = deepcopy(house)

    # print(house.battery)
    if house_pointer.pos_x < battery.pos_x:
        while house_pointer.pos_x != battery.pos_x:
            loop = k % len(cable_list)
            if cable_list[loop].pos_x is house_pointer.pos_x and cable_list[loop].pos_y is house_pointer.pos_y:
                # print(cable_list[k].pos_x, house_pointer.pos_x, cable_list[k].pos_y, house_pointer.pos_y)
                cable_list.remove(cable_list[loop])
                # print(cable_list[k].pos_x, house_pointer.pos_x, cable_list[k].pos_y, house_pointer.pos_y)
                house_pointer.pos_x += 1


            k += 1
            # print(loop)
            # print(len(cable_list))

    elif house_pointer.pos_x > battery.pos_x:
        while house_pointer.pos_x != battery.pos_x:
            loop = k % len(cable_list)
            if cable_list[loop].pos_x is house_pointer.pos_x and cable_list[loop].pos_y is house_pointer.pos_y:
                # print(cable_list[k].pos_x, house_pointer.pos_x, cable_list[k].pos_y, house_pointer.pos_y)
                cable_list.remove(cable_list[loop])
                # print(cable_list[k].pos_x, house_pointer.pos_x, cable_list[k].pos_y, house_pointer.pos_y)
                house_pointer.pos_x -= 1

            k += 1




            # cable loops through y
    q = 0
    if house_pointer.pos_y < battery.pos_y:
        while house_pointer.pos_y != battery.pos_y:
            loop = k % len(cable_list)
            if cable_list[loop].pos_x is house_pointer.pos_x and cable_list[loop].pos_y is house_pointer.pos_y:
                # print(cable_list[k].pos_x, house_pointer.pos_x, cable_list[k].pos_y, house_pointer.pos_y)
                cable_list.remove(cable_list[loop])
                house_pointer.pos_y += 1

            k += 1



    elif house_pointer.pos_y > battery.pos_y:
        while house_pointer.pos_y != battery.pos_y:
            loop = k % len(cable_list)
            if cable_list[loop].pos_x is house_pointer.pos_x and cable_list[loop].pos_y is house_pointer.pos_y:
                # print(cable_list[k].pos_x, house_pointer.pos_x, cable_list[k].pos_y, house_pointer.pos_y)
                cable_list.remove(cable_list[loop])
                house_pointer.pos_y -= 1

            k += 1


    # if house_pointer.pos_y == battery.pos_y and house_pointer.pos_x == battery.pos_x:
    connected -= 1
    battery.capacity += house.output




def switch_houses(house, second_house, battery, second_battery, cable_list, batteries):

    connected = 0

    # full_houses = readcsv("wijk1_huizen.csv")
    # matchCount=0
    # for a in full_houses:
    #     if a.pos_x == house.pos_x and a.pos_y == house.pos_y:
    #         house.output = a.output
    #         matchCount+=1
    #     elif a.pos_x == second_house.pos_x and a.pos_y == second_house.pos_y:
    #         second_house.output = a.output
    # if matchCount==0:
    #         print("ERROR")
    #         # print(house.pos_x, house.pos_y)




    if battery.capacity + house.output - second_house.output > 0 and second_battery.capacity + second_house.output - house.output > 0:
        # print(house.output, second_house.output, battery.capacity, second_battery.capacity)
        disconnect_from_battery(house, battery, cable_list)
        disconnect_from_battery(second_house, second_battery, cable_list)
        reserve = house.battery
        # print(house.output, second_house.output, battery.capacity, second_battery.capacity)
        connect_to_battery(house, second_battery, cable_list, second_house.battery)
        connect_to_battery(second_house, battery, cable_list, reserve)
        # print(house.output, second_house.output, battery.capacity, second_battery.capacity)
        # print("switched")

        return True
    else:
        return False




def distance_sort(batteries, houses):
    distances = []
    distance = {}
    for j in range(len(houses)):
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
                cl = connect_to_battery(house, key, cable_list)
                connected += 1
                break
    return cl

def connection_score(sorted_houses, distance, batteries, houses):
    score = 150
    connected = 0
    for house in sorted_houses:
        for key in distance[house[0]]:
            if match_with_house(houses[house[0]], batteries[key[0]]) and houses[house[0]].output > 0:
                score += update_score(houses[house[0]], batteries[key[0]])
                connected += 1
                break
    return score



def reset_batteries(batteries):
    for bat in batteries:
        bat.capacity = 1507.0


def swap(battery):
    # amount = random(1-5)
    direction = randint(1, 4)
    if direction == 1:
        battery.pos_x += 1
    elif direction == 2:
        battery.pos_x -= 1
    elif direction == 3:
        battery.pos_y += 1
    elif direction == 4:
        battery.pos_y -= 1
