'''
 / connects houses to the closest battery if it has enough capacity
'''
import experimentimportTXT


cable_list = []
cl = []
connected = 0

batteries = experimentimportTXT.readtxt("wijk1_batterijen.txt")
houses = experimentimportTXT.readcsv("wijk1_huizen.csv")

distance = experimentimportTXT.distance_sort(batteries, houses)

for i in range(len(houses)):
    for key in distance[i]:
        if experimentimportTXT.match_with_house(houses[i], batteries[key[0]]) and houses[i].output > 0:
            cable = experimentimportTXT.Cable(houses[i].pos_x, houses[i].pos_y, i)
            cable_list.append(cable)
            cl = experimentimportTXT.connect_to_battery(i, key[0], cable_list, batteries, houses)
            connected += 1
            break

print(len(cl))
print(connected)

