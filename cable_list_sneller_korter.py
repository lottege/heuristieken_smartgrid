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

distance = experimentimportTXT.distance_sort(batteries, houses)

for i in range(len(houses)):



for key, value in distance[10]:
    print(key, value)

