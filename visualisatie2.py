import matplotlib.pyplot as plt

def visualisation(houses, batteries, cables):
    # houses = houses
    # batteries = batteries
    # cables = cables

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
        elif cables[i].battery_nr is 5:
            plt.plot(cables[i].pos_x, cables[i].pos_y, color = '#808000', marker = '.', alpha=0.5)
        elif cables[i].battery_nr is 6:
            plt.plot(cables[i].pos_x, cables[i].pos_y, color = '#F08080', marker = '.', alpha=0.5)
        elif cables[i].battery_nr is 7:
            plt.plot(cables[i].pos_x, cables[i].pos_y, color = '#008080', marker = '.', alpha=0.5)
        elif cables[i].battery_nr is 8:
            plt.plot(cables[i].pos_x, cables[i].pos_y, color = '#800080', marker = '.', alpha=0.5)

    for e in range(len(houses)):
        plt.plot(houses[e].pos_x, houses[e].pos_y, color='k', marker='p')

    for a in range(len(batteries)):
        if a is 0:
            plt.plot(batteries[a].pos_x, batteries[a].pos_y, color='r', marker='s')
        elif a is 1:
            plt.plot(batteries[a].pos_x, batteries[a].pos_y, color='b', marker='s')
        elif a is 2:
            plt.plot(batteries[a].pos_x, batteries[a].pos_y, color='g', marker='s')
        elif a is 3:
            plt.plot(batteries[a].pos_x, batteries[a].pos_y, color='m', marker='s')
        elif a is 4:
            plt.plot(batteries[a].pos_x, batteries[a].pos_y, color='y', marker='s')
        elif a is 5:
            plt.plot(batteries[a].pos_x, batteries[a].pos_y, color='#808000', marker='s')
        elif a is 6:
            plt.plot(batteries[a].pos_x, batteries[a].pos_y, color='#F08080', marker='s')
        elif a is 7:
            plt.plot(batteries[a].pos_x, batteries[a].pos_y, color='#008080', marker='s')
        elif a is 8:
            plt.plot(batteries[a].pos_x, batteries[a].pos_y, color='#800080', marker='s')
    plt.show()
