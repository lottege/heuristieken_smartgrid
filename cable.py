'''
 / Makes a cable between a house and a battery in 2 ways:
 / 1: making new cables all alongside each other
 / 2: connecting cables all together
'''


import experimentimportTXT

print("hallo")
class Cable:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y


cable_dict = {}

batteries = experimentimportTXT.readtxt("wijk1_batterijen.txt")
houses = experimentimportTXT.readcsv("wijk1_huizen.csv")

# Option 1: places cables alongside others (longer dict, no dict checks)
for battery in batteries:
    for house in houses:
        if experimentimportTXT.match_with_house(house, battery):

        Cable.pos_x = house.pos_x
        Cable.pos_y = house.pos_y

        # cable loops through x
        for Cable.pos_x != Battery.pos_x:
            if Cable.pos_x < Battery.pos_x:
                Cable.pos_x += 1
                cable_dict[Cable.pos_x, Cable.pos_y] = true

            elif Cable.pos_x > Battery.pos_x:
                Cable.pos_x -= 1
                cable_dict[Cable.pos_x, Cable.pos_y] = true

        # cable loops through y
        for Cable.pos_y != Battery.pos_y:
            if Cable.pos_y < Battery.pos_y:
                Cable.pos_y += 1
                cable_dict[Cable.pos_x, Cable.pos_y] = true

            elif Cable.pos_y > Battery.pos_y:
                Cable.pos_y -= 1
                cable_dict[Cable.pos_x, Cable.pos_y] = true

print(cable_dict)


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
#                 if cable_dict[Cable.pos_x, Cable.pos_y] == true:
#                     break
#                 else:
#                     cable_dict[Cable.pos_x, Cable.pos_y] = true
#
#             elif Cable.pos_x > Battery.pos_x:
#                 Cable.pos_x -= 1
#                 if cable_dict[Cable.pos_x, Cable.pos_y] == true:
#                     break
#                 else:
#                     cable_dict[Cable.pos_x, Cable.pos_y] = true
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
