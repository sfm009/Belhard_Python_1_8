"""
Написать декоратор класса class_benchmark, который будет проводить
бенчмарк (замер времени выполнения) всех публичных методов класса
(те, которые не начинаются с _).

Чтобы у методов класса изменить поведение - дополнительно написать
декоратор функции def_benchmark.

До выполнения метода должен быть вывод в консоль:
Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}
Время начала: {start_time}

После выполнения метода должен быть вывод в консоль:
Выполнено {func.__name__}
Время окончания: {end_time}
Всего затрачено времени на выполнение: {end_time - start_time}
"""
import time


def def_benchmark(func):
    def wrapper(*args, ** kwargs):
        start_time = time.time()
        print(f'Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}\n'
              f'Время начала: {start_time}')
        result = func(*args, **kwargs)
        end_time = time.time()
        difference = end_time - start_time
        print(f'Выполнено {func.__name__}\n'
              f'Время окончания: {end_time}\n'
              f'Всего затрачено времени на выполнение: {difference}')
        return result
    return wrapper


def class_benchmark(cls):
    call_atr = {k: v for k, v in cls.__dict__.items() if k.find('_')}
    for name, val in call_atr.items():
        decorated = def_benchmark(val)
        setattr(cls, name, decorated)
    return cls
