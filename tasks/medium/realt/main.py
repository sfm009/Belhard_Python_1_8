from tasks.medium.realt.house import House
from tasks.medium.realt.person import Person
from tasks.medium.realt.townhouse import Townhouse

if __name__ == '__main__':
    house_1 = House('London', 200, 300)
    house_2 = House('Minsk', 150, 100)

    townhouse_1 = Townhouse('Berlin', 80)
    townhouse_2 = Townhouse('Warsaw', 100)

    person_1 = Person('Maksim', 33, 50)

    while person_1.money < house_2.cost:
        Person.earn_money(person_1)

    Person.make_deal(person_1)


