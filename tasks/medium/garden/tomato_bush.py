class TomatoBush:
    tomato_list: list

    def __init__(self, *args):
        self.tomato_list = list(args)

    def grow_all(self):
        for i in range(len(self.tomato_list)):
            self.ripeness = self.states[i]

    def all_are_ripe(self):
        for i in range(len(self.tomato_list)):
            if self.tomato_list[i] == self.states[-1]:
                return True
            else:
                return False

    def give_away_all(self):
        for i in range(len(self.tomato_list)):
            if self.tomato_list[i] == self.states[i]:
                self.tomato_list.pop(i)
        return self.tomato_list

