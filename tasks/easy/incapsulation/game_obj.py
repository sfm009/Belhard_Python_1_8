"""
Напишите класс GameObject, в котором будут храниться координаты объекта.

- private атрибут x (тип int)
- private атрибут y (тип int)
- магический метод __init__, который принимает начальные x и y

Координаты должны быть доступны для чтения (сделать property), а их изменение
должно происходить в методе move(delta_x, delta_y). (изменение - это +=)
"""


class GameObject:
    __x: int
    __y: int

    def __init__(self, __x, __y):
        self.__x = __x
        self.__y = __y

    @property
    def move(self):
        return self.__x, self.__y

    @move.setter
    def move(self, val):
        self.__x += delta_x
        self.__y += delta_y


obj_1 = GameObject()
