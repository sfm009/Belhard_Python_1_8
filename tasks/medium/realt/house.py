class House:
    def __init__(self, address, area, cost):
        self.address = address
        self.area = area
        self.cost = cost

    def increase_cost(self, incr_val):
        self.cost += incr_val

    def decrease_cost(self, decr_val):
        self.cost -= decr_val
