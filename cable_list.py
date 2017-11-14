'''
 / Makes a cable between a house and a battery in 2 ways:
 / 1: making new cables all alongside each other
 / 2: connecting cables all together
 / plot met mat plot lib
'''
import experimentimportTXT


class Cable:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y


cable_list = []
connected = 0

batteries = experimentimportTXT.readtxt("wijk1_batterijen.txt")
houses = experimentimportTXT.readcsv("wijk1_huizen.csv")

# Option 1: places cables alongside others (longer dict, no dict checks)
for i in range(len(batteries)):
    for j in range(len(houses)):
        if experimentimportTXT.match_with_house(houses[j], batteries[i]) and houses[j].output > 0:

            cable = Cable(houses[j].pos_x, houses[j].pos_y)
            cable_list.append(cable)

            # cable loops through x
            while cable_list[-1].pos_x != batteries[i].pos_x:
                if cable_list[-1].pos_x < batteries[i].pos_x:
                    cable = Cable(cable_list[-1].pos_x + 1, cable_list[-1].pos_y)
                    cable_list.append(cable)

                elif cable_list[-1].pos_x > batteries[i].pos_x:
                    cable = Cable(cable_list[-1].pos_x - 1, cable_list[-1].pos_y)
                    cable_list.append(cable)

            # cable loops through y
            while cable_list[-1].pos_y != batteries[i].pos_y:
                if cable_list[-1].pos_y < batteries[i].pos_y:
                    cable = Cable(cable_list[-1].pos_x, cable_list[-1].pos_y + 1)
                    cable_list.append(cable)

                elif cable_list[-1].pos_y > batteries[i].pos_y:
                    cable = Cable(cable_list[-1].pos_x, cable_list[-1].pos_y - 1)
                    cable_list.append(cable)

            if cable_list[-1].pos_y == batteries[i].pos_y and cable_list[-1].pos_x == batteries[i].pos_x:
                connected += 1
                batteries[i].capacity -= houses[j].output
                houses[j].output -= houses[j].output
        else:

            # locates battery and house that returns false on MWH or has output of 0
            print(i, j, end="x, ")
            #debug

for i in range(len(batteries)):
    print(batteries[i].capacity)


print(len(cable_list))
print(connected)

# # Option 2: connects cables to other cables (shorter dict, more dict-checks)
# for battery in batteries:
#     for house in houses:
#         if match_with_house(house, battery):
#
#         Cable.pos_x = house.pos_x
#         Cable.pos_y = house.pos_y
#
#         # cable loops through x
#         for Cable.pos_x != Battery.pos_x:
#             if Cable.pos_x < Battery.pos_x:
#                 Cable.pos_x += 1
#                 if cable_dict[Cable.pos_x, Cable.pos_y] == True:
#                     break
#                 else:
#                     cable_dict[Cable.pos_x, Cable.pos_y] = True
#
#             elif Cable.pos_x > Battery.pos_x:
#                 Cable.pos_x -= 1
#                 if cable_dict[Cable.pos_x, Cable.pos_y] == True:
#                     break
#                 else:
#                     cable_dict[Cable.pos_x, Cable.pos_y] = True
#
#         # cable loops through y
#         for Cable.pos_y != Battery.pos_y:
#             if Cable.pos_y < Battery.pos_y:
#                 Cable.pos_y += 1
#                 if cable_dict[Cable.pos_x, Cable.pos_y] == true:
#                     break
#                 cable_dict[Cable.pos_x, Cable.pos_y] = true
#
#             elif Cable.pos_y > Battery.pos_y:
#                 Cable.pos_y -= 1
#                 if cable_dict[Cable.pos_x, Cable.pos_y] == true:
#                     break
#                 cable_dict[Cable.pos_x, Cable.pos_y] = true
