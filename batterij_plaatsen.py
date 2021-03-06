'''
 / connects houses to the closest battery if it has enough capacity, starting with the furthest houses from the centre
'''
import helpers
from random import randint
# import visualisatie as vis


batteries = helpers.readtxt("wijk1_batterijen.txt")
houses = helpers.readcsv("wijk1_huizen.csv")

previous = 10000
score = 8000
for a in range(200000):
    batteries = helpers.reset_batteries(batteries)
    for bat in batteries:
        bat.pos_x = randint(0, 50)
        bat.pos_y = randint(0, 50)

    distance = helpers.distance_sort(batteries, houses)
    sorted_houses = helpers.sort_houses(houses)
    cl = helpers.connection(sorted_houses, distance, batteries, houses)

    if len(cl) < previous:
        previous = len(cl)
        battery_locations = []
        for bat in batteries:
            battery = helpers.Battery(bat.pos_x, bat.pos_y, bat.capacity)
            battery_locations.append(battery)
        final_houses = sorted_houses
        winner = cl

print(previous)
# vis.visualisation(houses, battery_locations, winner)



