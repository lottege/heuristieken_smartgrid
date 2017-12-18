'''
 / connects houses to the closest battery if it has enough capacity, starting with the furthest houses from the centre
'''
from random import randint

import helpers2

# import visualisatie as vis
final_houses = []
battery_locations = []
winner = []
winwin = []


batteries = helpers2.readtxt("wijk1_batterijen.txt")
houses = helpers2.readcsv("wijk1_huizen.csv")

previous = 20000
score = 8000

for a in range(10000):
    helpers2.reset_batteries(batteries)
    for bat in batteries:
        bat.pos_x = randint(0, 50)
        bat.pos_y = randint(0, 50)

    distance = helpers2.distance_sort(batteries, houses)
    sorted_houses = helpers2.sort_houses(houses)
    score, connected = helpers2.connection_score(sorted_houses, distance, batteries, houses)

    if score < previous:
        helpers2.reset_batteries(batteries)
        cl = helpers2.connection(sorted_houses, distance, batteries, houses)
        previous = score
        battery_locations = []
        for bat in batteries:
            battery = helpers2.Battery(bat.pos_x, bat.pos_y, bat.capacity)
            battery_locations.append(battery)
        final_houses = sorted_houses
        winner = cl

hill = []
final_batteries = battery_locations

for b in range(10000):
    for i in range(len(battery_locations)):
        battery_locations[i].pos_x = final_batteries[i].pos_x
        battery_locations[i].pos_y = final_batteries[i].pos_y
    helpers2.reset_batteries(battery_locations)
    helpers2.swap(battery_locations[randint(0, 4)], battery_locations)

    distance = helpers2.distance_sort(battery_locations, houses)
    sorted_houses = helpers2.sort_houses(houses)
    score, connected = helpers2.connection_score(sorted_houses, distance, battery_locations, houses)

    if score < previous:
        print(score)
        previous = score
        helpers2.reset_batteries(battery_locations)
        hill = helpers2.connection(sorted_houses, distance, battery_locations, houses)
        print(len(hill))
        final_batteries = []
        for bat in battery_locations:
            battery = helpers2.Battery(bat.pos_x, bat.pos_y, bat.capacity)
            final_batteries.append(battery)
        final_houses = sorted_houses
        winner = hill

        print(len(winner))

print(len(winner))
prijs = len(winner * 9) + 5 * 1500

# vis.visualisation(houses, final_batteries, winner)




