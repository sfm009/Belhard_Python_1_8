class Tomato:
    index: int
    ripeness: str
    states = ("Отсутствует", "Цветение", "Зеленый", "Красный")

    def __init__(self, index, ripeness=states[0]):
        self.index = index
        self.ripeness = ripeness

    def growl(self):
        for i in range(1, len(self.states)):
            self.ripeness = self.states[i]

    def is_ripe(self):
        if self.ripeness == self.states[-1]:
            return True
        else:
            return False
