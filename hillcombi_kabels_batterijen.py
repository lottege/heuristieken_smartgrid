'''
 / connects houses to the closest battery if it has enough capacity, starting with the furthest houses from the centre
'''
import random
import classes
import helpers3
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
            battery = helpers2.Battery(bat.pos_x, bat.pos_y, bat.capacity)
            final_batteries.append(battery)
        final_houses = sorted_houses
        winner = hill

        # print(len(winner))

print("random en hill batt winner:", len(winner))

cable_list = []
new_cable_list = []
best_list = []
connected = 0
tries = 50000
tries2 = tries
i = 0
q = 0
score = 150
percentage = tries // 1000
best_score = 10000

old_cost = 6000 * 9
new_cost = old_cost

batteries = final_batteries
houses = helpers3.readcsv("wijk1_huizen.csv")

# Option 1: places cables alongside others (longer dict, no dict checks)
for battery in range(len(batteries)):
    batteries[battery].number = battery
    for house in range(len(houses)):
        if helpers3.match_with_house(houses[house], batteries[battery]) and houses[house].output > 0:
            helpers3.drain_capacity(houses[house], batteries[battery])
            houses[house].output -= houses[house].output
            score += helpers3.update_score(houses[house], batteries[battery])
            connected += 1

for a in range(10):

    score = 150
    cable_list = []
    batteries = final_batteries
    houses = helpers3.readcsv("wijk1_huizen.csv")
    random_houses = []
    while len(random_houses) < len(houses):
        random_house = random.choice(houses)
        if random_house not in random_houses:
            random_houses.append(random_house)

    # Option 1: places cables alongside others (longer dict, no dict checks)
    for battery in range(len(batteries)):
        batteries[battery].number = battery
        for house in range(len(random_houses)):
            if helpers3.match_with_house(random_houses[house], batteries[battery]) and random_houses[house].output > 0:
                helpers3.drain_capacity(random_houses[house], batteries[battery])
                random_houses[house].output -= random_houses[house].output
                score += helpers3.update_score(random_houses[house], batteries[battery])
                connected += 1

    houses2 = helpers3.readcsv("wijk1_huizen.csv")
    for house in range(len(houses2)):
        random_houses[house].output = houses2[house].output

    for k in range(tries):
        a = random.choice(random_houses)
        b = random.choice(random_houses)

        while batteries[a.battery] is batteries[b.battery]:
            a = random.choice(random_houses)
            b = random.choice(random_houses)

        for m in range(5 % tries):
            if helpers3.check_switch(a, b, batteries[a.battery], batteries[b.battery]):
                score = helpers3.switch_score(a, b, batteries[a.battery], batteries[b.battery], score)
                i += 1
                tries2 -= percentage

    if score < best_score:
        best_score = score
        for house in range(len(random_houses)):
            cable = classes.Cable(random_houses[house].pos_x, random_houses[house].pos_y, battery)
            cable_list.append(cable)
            helpers3.connect_to_battery(random_houses[house], batteries[random_houses[house].battery], cable_list)
            connected += 1
            best_list = cable_list

print("length", len(best_list))


# # vis.visualisation(houses, batteries, new_cable_list)
