import matplotlib.pyplot as plt
import csv
import cable_list as cable 

def readcsv(csvfile):
    with open(csvfile) as wijk1:
        readCSV = csv.reader(wijk1, delimiter=',')
        next(readCSV)

        house_list = []
        for row in readCSV:
            house = [int(row[0]), int(row[1])]
            house_list.append(house)
        return house_list

def readtxt(txtfile):
    with open(txtfile, newline='') as batterijen1:
        readCSV = csv.reader(batterijen1, delimiter=']')
        next(readCSV, None)

        battery_list = []
        for row in readCSV:
            parts = row[0].split(',')
            battery = [int(parts[0].strip()[1:]), int(parts[1].strip())]
            battery_list.append(battery)
        return battery_list

houses = readcsv("wijk1_huizen.csv")
batteries = readtxt("wijk1_batterijen.txt")
cables = cable.cable_list

plt.axis([-2, 52, -2, 52])
for i in range(len(cables)):
    if cables[i].battery_nr is 0:
        plt.plot(cables[i].pos_x, cables[i].pos_y, color = 'r', marker = '.', alpha=0.5)
    elif cables[i].battery_nr is 1:
        plt.plot(cables[i].pos_x, cables[i].pos_y, color = 'b', marker = '.', alpha=0.5)
    elif cables[i].battery_nr is 2:
        plt.plot(cables[i].pos_x, cables[i].pos_y, color = 'g', marker = '.', alpha=0.5)
    elif cables[i].battery_nr is 3:
        plt.plot(cables[i].pos_x, cables[i].pos_y, color = 'm', marker = '.', alpha=0.5)
    elif cables[i].battery_nr is 4:
        plt.plot(cables[i].pos_x, cables[i].pos_y, color = 'y', marker = '.', alpha=0.5)

for house in houses: 
    plt.plot(house[0], house[1], color='k', marker='p') 

for battery in range(len(batteries)): 
    if battery is 0:
        plt.plot(batteries[battery][0], batteries[battery][1], color='r', marker='s') 
    elif battery is 1:
        plt.plot(batteries[battery][0], batteries[battery][1], color='b', marker='s') 
    elif battery is 2:
        plt.plot(batteries[battery][0], batteries[battery][1], color='g', marker='s') 
    elif battery is 3:
        plt.plot(batteries[battery][0], batteries[battery][1], color='m', marker='s') 
    elif battery is 4:
        plt.plot(batteries[battery][0], batteries[battery][1], color='y', marker='s') 
plt.show()