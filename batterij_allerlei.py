'''
 / connects houses to the closest battery if it has enough capacity, starting with the furthest houses from the centre
'''
from random import randint

import helpers2

# import visualisatie as vis


houses = helpers2.readcsv("wijk1_huizen.csv")
winner = []
batteries = []

previous = 10000
score = 8000
for a in range(1000):
    batteries = []
    for i in range(9):
        bat = helpers2.Battery(randint(0, 50), randint(0, 50), 900)
        batteries.append(bat)
    distance = helpers2.distance_sort(batteries, houses)
    sorted_houses = helpers2.sort_houses(houses)
    cl = helpers2.connection(sorted_houses, distance, batteries, houses)

    if len(cl) < previous:
        previous = len(cl)
        battery_locations = []
        for bat in batteries:
            battery = helpers2.Battery(bat.pos_x, bat.pos_y, bat.capacity)
            battery_locations.append(battery)
        final_houses = sorted_houses
        winner = cl
print("winner: ", len(winner))
print("hoeraa")

hill = []
tries = 0
for b in range(1000):
    # while len(hill) <= previous:
    tries += 1
    if (tries % 100) == 0:
        print(tries)
    for bat in battery_locations:
        bat.capacity = 900
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
        print(len(winner))

print(previous)
# vis.visualisation(houses, final_batteries, winner)

price = (len(winner) * 9) + (len(batteries) * 900)
print(price)

