class Battery:
    number = 0

    def __init__(self, pos_x, pos_y, capacity):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.capacity = capacity
        Battery.number += 1

class House:
    number = 0

    def __init__(self, pos_x, pos_y, output):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.output = output
        House.number += 1

class Cable:
    def __init__(self, pos_x, pos_y, battery_nr):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.battery_nr = battery_nr

