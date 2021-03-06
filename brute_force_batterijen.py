import helpers2


batteries = helpers2.readtxt("wijk1_batterijen.txt")
houses = helpers2.readcsv("wijk1_huizen.csv")
final_houses = []
winner = []

previous = 10000
score = 8000
# tries = 0

for i0 in range(50):
    print("0")
    for j0 in range(50):
        print("0")
        helpers2.reset_batteries(batteries)
        batteries[0].pos_x = i0
        batteries[0].pos_y = j0

        distance = helpers2.distance_sort(batteries, houses)
        sorted_houses = helpers2.sort_houses(houses)
        score, connected = helpers2.connection_score(sorted_houses, distance, batteries, houses)

        if score < previous:
            print("i0")
            previous = score
            helpers2.reset_batteries(batteries)
            cl = helpers2.connection(sorted_houses, distance, batteries, houses)
            battery_locations = []
            for baty in batteries:
                battery = helpers2.Battery(baty.pos_x, baty.pos_y, baty.capacity)
                battery_locations.append(battery)
            final_houses = sorted_houses
            winner = cl

        for i1 in range(50):
            print("1")
            for j1 in range(50):
                helpers2.reset_batteries(batteries)
                batteries[1].pos_x = i1
                batteries[1].pos_y = j1

                distance = helpers2.distance_sort(batteries, houses)
                sorted_houses = helpers2.sort_houses(houses)
                score, connected = helpers2.connection_score(sorted_houses, distance, batteries, houses)

                if score < previous:
                    print("i1")
                    previous = score
                    helpers2.reset_batteries(batteries)
                    cl = helpers2.connection(sorted_houses, distance, batteries, houses)
                    battery_locations = []
                    for baty in batteries:
                        battery = helpers2.Battery(baty.pos_x, baty.pos_y, baty.capacity)
                        battery_locations.append(battery)
                    final_houses = sorted_houses
                    winner = cl

            for i2 in range(50):
                print("2")
                for j2 in range(50):
                    helpers2.reset_batteries(batteries)
                    batteries[2].pos_x = i2
                    batteries[2].pos_y = j2

                    distance = helpers2.distance_sort(batteries, houses)
                    sorted_houses = helpers2.sort_houses(houses)
                    score, connected = helpers2.connection_score(sorted_houses, distance, batteries, houses)

                    if score < previous:
                        print("i2")
                        previous = score
                        helpers2.reset_batteries(batteries)
                        cl = helpers2.connection(sorted_houses, distance, batteries, houses)
                        battery_locations = []
                        for baty in batteries:
                            battery = helpers2.Battery(baty.pos_x, baty.pos_y, baty.capacity)
                            battery_locations.append(battery)
                        final_houses = sorted_houses
                        winner = cl

                for i3 in range(50):
                    print("3")
                    for j3 in range(50):
                        helpers2.reset_batteries(batteries)
                        batteries[3].pos_x = i3
                        batteries[3].pos_y = j3

                        distance = helpers2.distance_sort(batteries, houses)
                        sorted_houses = helpers2.sort_houses(houses)
                        score, connected = helpers2.connection_score(sorted_houses, distance, batteries, houses)

                        if score < previous:
                            print("i3")
                            previous = score
                            helpers2.reset_batteries(batteries)
                            cl = helpers2.connection(sorted_houses, distance, batteries, houses)
                            battery_locations = []
                            for baty in batteries:
                                battery = helpers2.Battery(baty.pos_x, baty.pos_y, baty.capacity)
                                battery_locations.append(battery)
                            final_houses = sorted_houses
                            winner = cl

                    for i4 in range(50):
                        print("4")
                        for j4 in range(50):
                            helpers2.reset_batteries(batteries)
                            batteries[4].pos_x = i4
                            batteries[4].pos_y = j4

                            distance = helpers2.distance_sort(batteries, houses)
                            sorted_houses = helpers2.sort_houses(houses)
                            score, connected = helpers2.connection_score(sorted_houses, distance, batteries, houses)

                            if score < previous:
                                print("i5")
                                previous = score
                                helpers2.reset_batteries(batteries)
                                cl = helpers2.connection(sorted_houses, distance, batteries, houses)
                                battery_locations = []
                                for baty in batteries:
                                    battery = helpers2.Battery(baty.pos_x, baty.pos_y, baty.capacity)
                                    battery_locations.append(battery)
                                final_houses = sorted_houses
                                winner = cl

print(len(winner))


