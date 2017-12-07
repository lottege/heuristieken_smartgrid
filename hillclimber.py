'''
/ Makes a cable between a house and a battery in 2 ways:
 / 1: making new cables all alongside each other
 / 2: connecting cables all together
 / plot met mat plot lib
'''
import experimentimportTXT
# import visualisation as vis
import classes
import random
# from buitennaarbinnen import cost_bb

cable_list = []
new_cable_list = []
connected = 0
tries = 20
i = 0



old_cost = 6000 * 9

batteries = experimentimportTXT.readtxt("wijk1_batterijen.txt")
houses = experimentimportTXT.readcsv("wijk1_huizen.csv")

cable_list = []

# Option 1: places cables alongside others (longer dict, no dict checks)
for battery in range(len(batteries)):
    for house in range(len(houses)):
        if experimentimportTXT.match_with_house(houses[house], batteries[battery]) and houses[house].output > 0:
            cable = classes.Cable(houses[house].pos_x, houses[house].pos_y, battery)
            cable_list.append(cable)
            experimentimportTXT.connect_to_battery(house, battery, cable_list, batteries, houses)
            connected += 1

old_cost = len(cable_list)

q = 0

for a in range(tries):
    random_houses = []
    k = 0
    l = 30
    q += 1


    houses2 = experimentimportTXT.readcsv("wijk1_huizen.csv")
    for house in houses:
        house.output = houses2[k].output
        k+=1
    for k in range(l):
        a = random.choice(houses)
        b = random.choice(houses)
        while a.battery > 4:
            a = random.choice(houses)
        while b.battery > 4:
            b = random.choice(houses)


    # print(a.battery)
    # print(a.output)
    # print(a)
    # print(batteries[a.battery])
    # print(batteries)


        for m in range(1):
            if experimentimportTXT.switch_houses(a, b, batteries[a.battery], batteries[b.battery], cable_list, batteries, connected) == True:

                new_cost = len(cable_list)
                # print(new_cost)
                if new_cost < old_cost:
                    i += 1
                    connected_new = connected
                    old_cost = new_cost
                    new_cable_list = cable_list
                    print("best", i ,", cables used = ", len(new_cable_list))




# vis.visualisation(houses, batteries, new_cable_list)
