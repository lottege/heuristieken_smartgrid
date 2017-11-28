'''
 / Makes a cable between a house and a battery in 2 ways:
 / 1: making new cables all alongside each other
 / 2: connecting cables all together
 / plot met mat plot lib
'''
import experimentimportTXT


cable_list = []
cl = []
connected = 0
random = 0
optimaal = 0
tweede_optimaal = 0
derde_optimaal = 0
vierde_optimaal = 0

batteries = experimentimportTXT.readtxt("wijk1_batterijen.txt")
houses = experimentimportTXT.readcsv("wijk1_huizen.csv")


for j in range(len(houses)):
    distance = []
    for i in range(len(batteries)):
        dis = abs((houses[j].pos_x - batteries[i].pos_x) + (houses[j].pos_y - batteries[i].pos_y))
        distance.append(dis)

    closest = min(distance)

    for i in range(len(batteries)):
        dis = abs((houses[j].pos_x - batteries[i].pos_x) + (houses[j].pos_y - batteries[i].pos_y))
        if dis == closest:
            if experimentimportTXT.match_with_house(houses[j], batteries[i]) and houses[j].output > 0:

                cable = experimentimportTXT.Cable(houses[j].pos_x, houses[j].pos_y, i)
                cable_list.append(cable)

                cl = experimentimportTXT.connect_to_battery(j, i, cable_list, batteries, houses)
                connected += 1
                optimaal += 1

            else:
                distance = []
                for i in range(len(batteries)):
                    dis = abs((houses[j].pos_x - batteries[i].pos_x) + (houses[j].pos_y - batteries[i].pos_y))
                    distance.append(dis)
                second = experimentimportTXT.second_smallest(distance)

                for i in range(len(batteries)):
                    dis = abs((houses[j].pos_x - batteries[i].pos_x) + (houses[j].pos_y - batteries[i].pos_y))
                    if dis == second:
                        if experimentimportTXT.match_with_house(houses[j], batteries[i]) and houses[j].output > 0:

                            cable = experimentimportTXT.Cable(houses[j].pos_x, houses[j].pos_y, i)
                            cable_list.append(cable)

                            cl = experimentimportTXT.connect_to_battery(j, i, cable_list, batteries, houses)
                            connected += 1
                            tweede_optimaal += 1
                        else:
                            distance = []
                            for i in range(len(batteries)):
                                dis = abs((houses[j].pos_x - batteries[i].pos_x) + (houses[j].pos_y - batteries[i].pos_y))
                                distance.append(dis)

                            third = experimentimportTXT.third_smallest(distance)

                            for i in range(len(batteries)):
                                dis = abs((houses[j].pos_x - batteries[i].pos_x) + (houses[j].pos_y - batteries[i].pos_y))
                                if dis == third:
                                    if experimentimportTXT.match_with_house(houses[j], batteries[i]) and houses[j].output > 0:

                                        cable = experimentimportTXT.Cable(houses[j].pos_x, houses[j].pos_y, i)
                                        cable_list.append(cable)

                                        cl = experimentimportTXT.connect_to_battery(j, i, cable_list, batteries, houses)
                                        connected += 1
                                        derde_optimaal += 1
                                else:
                                    distance = []
                                    for i in range(len(batteries)):
                                        dis = abs((houses[j].pos_x - batteries[i].pos_x) + (houses[j].pos_y - batteries[i].pos_y))
                                        distance.append(dis)

                                    fourth = experimentimportTXT.fourth_smallest(distance)

                                    for i in range(len(batteries)):
                                        dis = abs((houses[j].pos_x - batteries[i].pos_x) + (houses[j].pos_y - batteries[i].pos_y))
                                        if dis == fourth:
                                            if experimentimportTXT.match_with_house(houses[j], batteries[i]) and houses[j].output > 0:

                                                cable = experimentimportTXT.Cable(houses[j].pos_x, houses[j].pos_y, i)
                                                cable_list.append(cable)

                                                cl = experimentimportTXT.connect_to_battery(j, i, cable_list, batteries, houses)
                                                connected += 1
                                                vierde_optimaal += 1


for i in range(len(batteries)):
    print(batteries[i].capacity)

kosten = len(cl) * 9
totaal = kosten + (5 * 5000)

print(connected)

print(optimaal)
print(tweede_optimaal)
print(derde_optimaal)
print(vierde_optimaal)

print(len(cl))
print(kosten)
print(totaal)
