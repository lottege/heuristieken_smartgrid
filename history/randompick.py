'''
/ Makes a cable between a house and a battery in 2 ways:
 / 1: making new cables all alongside each other
 / 2: connecting cables all together
 / plot met mat plot lib
'''
import experimentimportTXT
import visualisatie as vis 
import classes
import random  
# from buitennaarbinnen import cost_bb

cable_list = []
new_cable_list = []
connected = 0





old_cost = 6000 * 9

for a in range(20000):
    batteries = experimentimportTXT.readtxt("wijk1_batterijen.txt")
    houses = experimentimportTXT.readcsv("wijk1_huizen.csv")
    houses_random = []
    cable_list = []
    while len(houses_random) < len(houses):
        random_house = random.choice(houses)
        if random_house not in houses_random:
            houses_random.append(random_house)


# Option 1: places cables alongside others (longer dict, no dict checks)
    for battery in range(len(batteries)):
        for house in range(len(houses_random)): 
            if experimentimportTXT.match_with_house(houses_random[house], batteries[battery]) and houses_random[house].output > 0:
                cable = classes.Cable(houses_random[house].pos_x, houses_random[house].pos_y, battery)
                cable_list.append(cable)
                experimentimportTXT.connect_to_battery(house, battery, cable_list, batteries, houses_random)
                connected += 1



    

    new_cost = len(cable_list) * 9

    # print(new_cost)
    if new_cost < old_cost:

        connected_new = connected
        old_cost = new_cost
        new_cable_list = cable_list
        print(len(new_cable_list))        
    
    else:
        connected = 0






vis.visualisation(houses_random, batteries, new_cable_list)