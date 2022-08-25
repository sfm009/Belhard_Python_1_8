class Gardener:
    name: str
    plants: list

    def __init__(self, name, *args):
        self.name = name
        self.plants = list(args)

    def work(self):
        print('Садовник работает')

    def harvest(self):
        if
