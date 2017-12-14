'''
 / connects houses to the closest battery if it has enough capacity, starting with the furthest houses from the centre
'''
from random import randint

import helpers2

# import visualisatie as vis
final_houses = []
winner = []
winwin = []
randwin = []
for loop in range(1):
    batteries = helpers2.readtxt("wijk1_batterijen.txt")
    houses = helpers2.readcsv("wijk1_huizen.csv")

    previous = 10000
    score = 8000
    # tries = 0
    for a in range(1000):
        # tries += 1
        # if (tries % 100) == 0:
            # print(tries)
        helpers2.reset_batteries(batteries)
        for bat in batteries:
            bat.pos_x = randint(0, 50)
            bat.pos_y = randint(0, 50)

        distance = helpers2.distance_sort(batteries, houses)
        sorted_houses = helpers2.sort_houses(houses)
        score = helpers2.connection_score(sorted_houses, distance, batteries, houses)

        if score < previous:
            cl = helpers2.connection(sorted_houses, distance, batteries, houses)
            print("score", score)
            print("len(cl):", len(cl))
            print("previous", previous)
            previous = score
            battery_locations = []
            for bat in batteries:
                battery = helpers2.Battery(bat.pos_x, bat.pos_y, bat.capacity)
                battery_locations.append(battery)
            final_houses = sorted_houses
            winner = cl

    randwin.append(len(winner))

    hill = []
    # tries = 0
    final_batteries = battery_locations
    for b in range(1):
        # while len(hill) <= previous:
        #     tries += 1
        #     if (tries % 100) == 0:
        #       print(tries)

            for i in range(len(battery_locations)):
                battery_locations[i].pos_x = final_batteries[i].pos_x
                battery_locations[i].pos_y = final_batteries[i].pos_y
            helpers2.reset_batteries(battery_locations)
            helpers2.swap(battery_locations[randint(0, 4)], battery_locations)
            distance = helpers2.distance_sort(battery_locations, houses)
            sorted_houses = helpers2.sort_houses(houses)
            hill = helpers2.connection(sorted_houses, distance, battery_locations, houses)

            if len(hill) < previous:
                previous = len(hill)
                final_batteries = []
                for bat in battery_locations:
                    battery = helpers2.Battery(bat.pos_x, bat.pos_y, bat.capacity)
                    final_batteries.append(battery)
                final_houses = sorted_houses
                winner = hill
                # print(len(winner))

    print(len(winner))
    # price = (len(winner) * 9) + (len(batteries) * 5000)
    # print(price)
    # vis.visualisation(houses, final_batteries, winner)

    winwin.append(len(winner))

# print(winwin)
# print(float(sum(winwin))/len(winwin))
# print(float(sum(randwin))/len(randwin))

