'''
 / Makes a cable between a house and a battery in 2 ways:
 / 1: making new cables all alongside each other
 / 2: connecting cables all together
'''

import experimentimportTXT

cable_dict = {}

batteries = experimentimportTXT.readtxt("wijk1_batterijen.txt")
houses = experimentimportTXT.readcsv("wijk1_huizen.csv")

# Option 1: places cables alongside others (longer dict, no dict checks)
for battery in range(len(batteries)):
    i = 0
    for house in range(len(houses)):
        if experimentimportTXT.match_with_house(house, battery) and houses[house].output > 0:

            cable_pos_x = houses[house].pos_x
            cable_pos_y = houses[house].pos_y


            # cable loops through x
            while cable_pos_x != batteries[battery].pos_x:
                if cable_pos_x < batteries[battery].pos_x:
                    cable_pos_x += 1
                    cable_dict[cable_pos_x, cable_pos_y] = True

                elif cable_pos_x > batteries[battery].pos_x:
                    cable_pos_x -= 1
                    cable_dict[cable_pos_x, cable_pos_y] = True

        # cable loops through y
            while cable_pos_y != batteries[battery].pos_y:
                if cable_pos_y < batteries[battery].pos_y:
                    cable_pos_y += 1
                    cable_dict[cable_pos_x, cable_pos_y] = True

                elif cable_pos_y > batteries[battery].pos_y:
                    cable_pos_y -= 1
                    cable_dict[cable_pos_x, cable_pos_y]= True

            #debug: locates battery and house
            print("")
            print(battery, ": ", house)
            print("")
            #debug

            #updates output
            batteries[battery].capacity -= houses[house].output
            print(houses[house].output)

            #debug: adds total output on batteries and substracts from connected house
            i += houses[house].output
            houses[house].output -= houses[house].output
            print(i)
            print("")

        else:

            # locates battery and house that returns false on MWH or has output of 0
            print(battery, house,  end="x, ")
            #debug


for battery in range(len(batteries)):
    print(batteries[battery].capacity)


# # # Option 2: connects cables to other cables (shorter dict, more dict-checks)
# for battery in range(len(batteries)):
#     i = 0
#     for house in range(len(houses)):
#         if experimentimportTXT.match_with_house(house, battery):

#             cable_pos_x = houses[house].pos_x
#             cable_pos_y = houses[house].pos_y

#         # cable loops through x
#         while cable_pos_x != batteries[battery].pos_x:
#             if cable_pos_x < batteries[battery].pos_x:
#                 cable_pos_x += 1
#                 if cable_dict[cable_pos_x, cable_pos_y] == True:
#                     break
#                 else:
#                     cable_dict[cable_pos_x, cable_pos_y] = True

#             elif cable_pos_x > batteries[battery].pos_x:
#                 cable_pos_x -= 1
#                 if cable_dict[cable_pos_x, cable_pos_y] == True:
#                     break
#                 else:
#                     cable_dict[cable_pos_x, cable_pos_y] = True

#         # cable loops through y
#         while cable_pos_y != batteries[battery].pos_y:
#             if cable_pos_y < batteries[battery].pos_y:
#                 cable_pos_y += 1
#                 if cable_dict[cable_pos_x, cable_pos_y] == True:
#                     break
#                 cable_dict[cable_pos_x, cable_pos_y] = True

#             elif cable_pos_y > batteries[battery].pos_y:
#                 cable_pos_y -= 1
#                 if cable_dict[cable_pos_x, cable_pos_y] == True:
#                     break
#                 cable_dict[cable_pos_x, cable_pos_y] = True

        # print(house)
        # batteries[battery].capacity -= houses[house].output
        # print(houses[house].output)

        # i += houses[house].output
        # houses[house].output -= houses[house].output
        # print(i)




