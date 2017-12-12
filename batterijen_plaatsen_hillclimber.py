'''
 / connects houses to the closest battery if it has enough capacity, starting with the furthest houses from the centre
'''
import helpers2
from random import randint
# import visualisatie as vis


batteries = helpers2.readtxt("wijk1_batterijen.txt")
houses = helpers2.readcsv("wijk1_huizen.csv")
final_houses = []
winner = []

previous = 10000
score = 8000
for a in range(20000):
    helpers2.reset_batteries(batteries)
    for bat in batteries:
        bat.pos_x = randint(0, 50)
        bat.pos_y = randint(0, 50)

    distance = helpers2.distance_sort(batteries, houses)
    sorted_houses = helpers2.sort_houses(houses)
    cl = helpers2.connection(sorted_houses, distance, batteries, houses)

    if len(cl) < previous:
        print('yay')
        previous = len(cl)
        battery_locations = []
        for bat in batteries:
            battery = helpers2.Battery(bat.pos_x, bat.pos_y, bat.capacity)
            battery_locations.append(battery)
        final_houses = sorted_houses
        winner = cl

print("hoeraa")
hill = []
tries = 0
for b in range(10000):
    # while len(hill) <= previous:
        tries += 1
        if (tries % 100) == 0:
            print(tries)
        helpers2.reset_batteries(battery_locations)
        helpers2.swap(battery_locations[randint(0, 4)])
        distance = helpers2.distance_sort(battery_locations, houses)
        sorted_houses = helpers2.sort_houses(houses)
        hill = helpers2.connection(sorted_houses, distance, battery_locations, houses)

        if len(hill) < previous:
            previous = len(hill)
            final_batteries = []
            for bat in batteries:
                battery = helpers2.Battery(bat.pos_x, bat.pos_y, bat.capacity)
                final_batteries.append(battery)
            final_houses = sorted_houses
            winner = hill
            print(len(winner))

print(previous)
print(len(winner))
