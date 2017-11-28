'''
 / connects houses to the closest battery if it has enough capacity
'''
import experimentimportTXT


cable_list = []
cl = []
connected = 0

batteries = experimentimportTXT.readtxt("wijk3_batterijen.txt")
houses = experimentimportTXT.readcsv("wijk3_huizen.csv")

distance = experimentimportTXT.distance_sort(batteries, houses)
sorted_houses = experimentimportTXT.sort_houses(houses)

for house in sorted_houses:
    for key in distance[house[0]]:
        if experimentimportTXT.match_with_house(houses[house[0]], batteries[key[0]]) and houses[house[0]].output > 0:
            cable = experimentimportTXT.Cable(houses[house[0]].pos_x, houses[house[0]].pos_y, house[0])
            cable_list.append(cable)
            cl = experimentimportTXT.connect_to_battery(house[0], key[0], cable_list, batteries, houses)
            connected += 1
            break

print(len(cl))
print(len(cable_list))
print(connected)
