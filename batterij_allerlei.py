'''
 / connects houses to the closest battery if it has enough capacity, starting with the furthest houses from the centre
'''
import helpers
from random import randint
# import visualisatie as vis


houses = helpers.readcsv("wijk1_huizen.csv")
batteries = []

previous = 10000
score = 8000
for a in range(200000):

    for i in range(5):
        bat = helpers.Cable(randint(0, 50), randint(0, 50), 900)
        batteries.append(bat)
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



