'''
 / connects houses to the closest battery if it has enough capacity, starting with the furthest houses from the centre
'''
import random
import classes
import helpers
import helpers3
import helpers2
# import visualisatie as vis
final_houses = []
battery_locations = []
winner = []
winwin = []


batteries = helpers.readtxt("wijk1_batterijen.txt")
houses = helpers.readcsv("wijk1_huizen.csv")

for battery in range(len(batteries)):
    batteries[battery].number = battery


previous = 20000
score = 8000
# tries = 0
for a in range(1000):
    # tries += 1
    # if (tries % 100) == 0:
        # print(tries)
    helpers2.reset_batteries(batteries)
    for bat in batteries:
        bat.pos_x = random.randint(0, 50)
        bat.pos_y = random.randint(0, 50)

    distance = helpers2.distance_sort(batteries, houses)
    sorted_houses = helpers2.sort_houses(houses)
    score = helpers2.connection_score(sorted_houses, distance, batteries, houses)

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

for b in range(100):
    for i in range(len(battery_locations)):
        battery_locations[i].pos_x = final_batteries[i].pos_x
        battery_locations[i].pos_y = final_batteries[i].pos_y
    helpers2.reset_batteries(battery_locations)
    helpers2.swap(battery_locations[random.randint(0, 4)], battery_locations)

    distance = helpers2.distance_sort(battery_locations, houses)
    sorted_houses = helpers2.sort_houses(houses)
    score = helpers2.connection_score(sorted_houses, distance, battery_locations, houses)

    if score < previous:
        print(score)
        previous = score
        helpers2.reset_batteries(battery_locations)
        hill = helpers2.connection(sorted_houses, distance, battery_locations, houses)
        final_batteries = []
        for bat in battery_locations:
            battery = helpers.Battery(bat.pos_x, bat.pos_y, bat.capacity)
            final_batteries.append(battery)
        final_houses = sorted_houses
        winner = hill

for battery in battery_locations:
    print(battery.number, battery.pos_x, battery.pos_y, battery.capacity)

        # print(len(winner))

print("random en hill batt winner:", len(winner))

for house in houses:
    if house.output > 0:
        print(house.number, house.output)


# for battery in batteries:
#     print(battery.number, battery.pos_x, battery.pos_y, battery.capacity)

cable_list = []
connected = 0
tries = 10000
i = 0
q = 0
score = 150


batteries = battery_locations

for battery in batteries:
    print(battery.number, battery.pos_x, battery.pos_y, battery.capacity)
print(connected)
helpers2.reset_batteries(batteries)


x=0
a = 150
for house in range(len(houses)):
    x = helpers.update_battery_score(houses[house], batteries[houses[house].battery])
    helpers.sure_drain_capacity(houses[house], batteries[houses[house].battery])
    a += x
    print(house, houses[house].battery, x, a)




# # Option 1: places cables alongside others (longer dict, no dict checks)
# for x in range(len(batteries)):
#     # batteries[battery].number = battery
#     for house in houses:
#         # print(batteries, house.battery)
#         if helpers.match_with_house(house, batteries[house.battery]) and house.output > 0:
#             helpers.sure_drain_capacity(house, batteries[house.battery])
#             house.output -= house.output
#             score += helpers.update_score(house, batteries[house.battery])
#             connected += 1


score = a
print("True length: ", score)

# for battery in range(len(batteries)):
#     print(batteries[battery].number)
# for house in range(len(houses)):
#     print(houses[house].battery)

for battery in batteries:
    print(battery.number)

for z in range(tries):
    l = 5
    q += 1


    houses2 = helpers.readcsv("wijk1_huizen.csv")
    for house in range(len(houses2)):
        houses[house].output = houses2[house].output

    for k in range(l):
        a = random.choice(houses)
        b = random.choice(houses)


        while batteries[a.battery] is batteries[b.battery]:
            a = random.choice(houses)
            b = random.choice(houses)



        for m in range(5 % q):
            if helpers.check_switch(a, b, batteries[a.battery], batteries[b.battery]):
                # print("batteries before:", a.battery, b.battery)
                score = helpers.switch_score(a, b, batteries[a.battery], batteries[b.battery], score)
                print("best", i ,", cables used = ", score)
                # print ("batteries after: ", a.battery, b.battery)
                # print(batteries[a.battery].capacity)
                i += 1


u = 0

for house in houses:
    # u += helpers.check_score(house, batteries[house.battery])
    # print(house.pos_x, house.pos_y, batteries[house.battery].pos_x, batteries[house.battery].pos_y, helpers.check_score(house, batteries[house.battery]), u)
    helpers.connect_to_battery(house, batteries, cable_list)
    connected += 1

# print(connected)
# for battery in range(len(batteries)):
    # print(batteries[battery].capacity)


for battery in batteries:
    print(battery.capacity)
for house in houses:
    if house.output > 0:
        print(house.number, house.output)

x=0
a = 150
for house in range(len(houses)):
    x = helpers.check_score(houses[house], batteries[houses[house].battery])
    a += x
    # print(house, houses[house].battery, x, a)

print("length", len(cable_list), q)
# # vis.visualisation(houses, batteries, new_cable_list)
