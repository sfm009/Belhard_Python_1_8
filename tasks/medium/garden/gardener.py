class Gardener:
    name: str
    plants: list

    def __init__(self, name, *args):
        self.name = name
        self.plants = list(args)

    def work(self):
        for plant in self.plants:
            plant.grow_all()

    def harvest(self):
        all_tomato = []
        for plant in self.plants:
            if plant.all_are_ripe() is False:
                break
            all_tomato.extend(plant.tomato_list)
            plant.give_away_all()
        else:
            return all_tomato
        print('Томаты не созрели')
