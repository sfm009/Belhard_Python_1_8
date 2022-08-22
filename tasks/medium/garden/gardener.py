from tasks.medium.garden.tomato_bush import TomatoBush


class Gardener(TomatoBush):
    name: str
    plants: list

    def __init__(self, name, plants, *args):
        self.name = name
        self.plants = plants
        args =

    @staticmethod
    def work(self):
        print('Садовник работает')