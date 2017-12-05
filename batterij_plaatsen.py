'''
 / connects houses to the closest battery if it has enough capacity, starting with the furthest houses from the centre
'''
import helpers
from random import randint


batteries = helpers.readtxt("wijk1_batterijen.txt")
houses = helpers.readcsv("wijk1_huizen.csv")

# distance = helpers.distance_sort(batteries, houses)
# sorted_houses = helpers.sort_houses(houses)

previous = 10000
# cl = helpers.connection(sorted_houses, distance, batteries, houses)
score = 8000
for a in range(2000):
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

    # print(batteries[0].pos_x)
    # while score < previous:
    #     temp = score
    #     print(batteries[0].capacity)
    #     batteries = helpers.reset_batteries(batteries)
    #     batteries[0].pos_x += 1
    #     cl = helpers.connection(sorted_houses, distance, batteries, houses)
    #     score = len(cl)
    #     print("score : {}, prev: {}, score: {}".format(score, previous, score))
    #     winning = cl
    #     previous = temp


print(previous)



