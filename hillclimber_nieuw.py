'''
/ Makes a cable between a house and a battery in 2 ways:
 / 1: making new cables all alongside each other
 / 2: connecting cables all together
 / plot met mat plot lib
'''
import experimentimportTXT
# import visualisation as vis
import classes
import helpers
import random
# from buitennaarbinnen import cost_bb

cable_list = []
new_cable_list = []
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

batteries = helpers.readtxt("wijk1_batterijen.txt")
houses = helpers.readcsv("wijk1_huizen.csv")



# Option 1: places cables alongside others (longer dict, no dict checks)
for battery in range(len(batteries)):
    batteries[battery].number = battery
    for house in range(len(houses)):
        if helpers.match_with_house(houses[house], batteries[battery]) and houses[house].output > 0:
            helpers.drain_capacity(houses[house], batteries[battery])
            houses[house].output -= houses[house].output
            score += helpers.update_score(houses[house], batteries[battery])
            connected += 1

print(score)

# for battery in range(len(batteries)):
#     print(batteries[battery].number)
# for house in range(len(houses)):
#     print(houses[house].battery)

for a in range(10):

    score = 150
    cable_list = []
    batteries = experimentimportTXT.readtxt("wijk1_batterijen.txt")
    houses = experimentimportTXT.readcsv("wijk1_huizen.csv")
    random_houses = []
    while len(random_houses) < len(houses):
        random_house = random.choice(houses)
        if random_house not in random_houses:
            random_houses.append(random_house)

    # Option 1: places cables alongside others (longer dict, no dict checks)
    for battery in range(len(batteries)):
        batteries[battery].number = battery
        for house in range(len(random_houses)):
            if helpers.match_with_house(random_houses[house], batteries[battery]) and random_houses[house].output > 0:
                helpers.drain_capacity(random_houses[house], batteries[battery])
                random_houses[house].output -= random_houses[house].output
                score += helpers.update_score(random_houses[house], batteries[battery])
                connected += 1


    houses2 = helpers.readcsv("wijk1_huizen.csv")
    for house in range(len(houses2)):
        random_houses[house].output = houses2[house].output

    for k in range(tries):
        a = random.choice(random_houses)
        b = random.choice(random_houses)

        while batteries[a.battery] is batteries[b.battery]:
            a = random.choice(random_houses)
            b = random.choice(random_houses)


        for m in range(5 % tries):
            if helpers.check_switch(a, b, batteries[a.battery], batteries[b.battery]):
                score = helpers.switch_score(a, b, batteries[a.battery], batteries[b.battery], score)
                # print("best", i ,", cables used = ", score)
                # print(batteries[a.battery].capacity)
                i += 1
                tries2 -= percentage

    if score < best_score:
        best_score = score
        print("best score: ", best_score)
# print(connected)
# for battery in range(len(batteries)):
    # print(batteries[battery].capacity)
        for house in range(len(random_houses)):
            cable = classes.Cable(random_houses[house].pos_x, random_houses[house].pos_y, battery)
            cable_list.append(cable)
            helpers.connect_to_battery(random_houses[house], batteries[random_houses[house].battery], cable_list)
            connected += 1
            best_list = cable_list
        print(len(best_list))
    # print(houses[house].battery)

# for cable in best_list:
#     print(cable.pos_x, cable.pos_y)



print("length", len(best_list))
print("best score: ", best_score)
# # vis.visualisation(houses, batteries, new_cable_list)
