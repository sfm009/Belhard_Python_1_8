from tasks.medium.realt.house import House


class Townhouse(House):
    def __init__(self, address, cost=60):
        super().__init__(address)
        self.cost = cost

