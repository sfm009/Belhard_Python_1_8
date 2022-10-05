from tasks.medium.garden.gardener import Gardener
from tasks.medium.garden.tomato import Tomato
from tasks.medium.garden.tomato_bush import TomatoBush

if __name__ == '__main__':

    tomato_1 = Tomato(1)
    tomato_2 = Tomato(2)
    tomato_3 = Tomato(3)
    tomato_4 = Tomato(4)
    tomato_5 = Tomato(5)
    tomato_6 = Tomato(6)

    bush_1 = TomatoBush(tomato_1, tomato_2, tomato_3)
    bush_2 = TomatoBush(tomato_4, tomato_5, tomato_6)

    gardener_1 = Gardener('Maksim', bush_1, bush_2)

    print(gardener_1.work())
    print(gardener_1.harvest())
    print(gardener_1.work())
    print(gardener_1.work())
    print(gardener_1.harvest())
    print(gardener_1.plants)
