from tasks.medium.realt.house import House


class Person:
    name: str
    age: int
    money: int
    realty: list

    def __init__(self, name, age, money=0, realty=[]):
        self.name = name
        self.age = age
        self.money = money
        self.realty = realty

    def info(self):
        print(self.name)
        print(self.age)
        print(self.money)
        print(self.age)

    def earn_money(self, earn_val=20):
        self.money += earn_val

    def make_deal(self, val):
        house_2.cost = val
        if val < self.money:
            self.money -= val
            self.realty.append(house_2)

