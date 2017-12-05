'''
 / connects houses to the closest battery if it has enough capacity,
 / starting with the house with the biggest distance from a battery
'''
import experimentimportTXT


cable_list = []
cl = []
connected = 0

batteries = experimentimportTXT.readtxt("wijk1_batterijen.txt")
houses = experimentimportTXT.readcsv("wijk1_huizen.csv")

distance = experimentimportTXT.sort_on_battery_distance(batteries, houses)

print(distance)
for house in distance:
    for batt in house:
        if experimentimportTXT.match_with_house(houses[batt[2]], batteries[batt[1]]) and houses[batt[2]].output > 0:
            print(batt)
            cable = experimentimportTXT.Cable(houses[batt[2]].pos_x, houses[batt[2]].pos_y, batt[1])
            cable_list.append(cable)
            cl = experimentimportTXT.connect_to_battery(batt[2], batt[1], cable_list, batteries, houses)
            connected += 1
            break

print(len(cl))
print(connected)
