class TomatoBush:
    tomato_list: list

    def __init__(self, *args):
        self.tomato_list = list(args)

    def grow_all(self):
        for tomato in self.tomato_list:
            tomato.grow()

    def all_are_ripe(self):
        for tomato in self.tomato_list:
            tomato.is_ripe()

    def give_away_all(self):
        print(f'Собрано {len(self.tomato_list)} томатов\nКуст очищен')
        self.tomato_list.clear()
