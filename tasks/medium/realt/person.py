from tasks.medium.realt.house import House


class Person:
    name: str
    age: int
    money: int
    realty: list

    def __init__(self, name, age, money=0):
        self.name = name
        self.age = age
        self.money = money
        self.realty = []

    def info(self):
        print(self.name)
        print(self.age)
        print(self.money)
        print(self.age)

    def earn_money(self, earn_val):
        self.money += earn_val
        print(f'Увеличиваем количество денег на {earn_val}')

    def make_deal(self, obj):
        if obj.cost < self.money:
            self.money -= obj.cost
            self.realty.append(House)
            print(f'Приобретен {obj}')
