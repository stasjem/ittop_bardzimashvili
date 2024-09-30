
from time import time, sleep

def measure_time(func):


    def decorator(*args, **kwargs):
        t1 = time()
        func(*args, **kwargs)
        t2 = time()
        delta = t2 - t1
        return delta # возвращаем время работы функции

    return decorator

# Определение функций, время работы которых мы хотим измерить
def f1():
    """ Функция 1 """
    sleep(0.5)
    return 'f1 result'

def f2():

    sleep(0.5)
    return 'f2 result'

def f3():

    sleep(1)
    return 'f3 result'


f1_decorated = measure_time(f1)
f2_decorated = measure_time(f2)
f3_decorated = measure_time(f3)


time_of_f1 = f1_decorated()
time_of_f2 = f2_decorated()
time_of_f3 = f3_decorated()

# Вывод времени работы функций
print('Время работы f1:', round(time_of_f1, 2))
print('Время работы f2:', round(time_of_f2, 2))
print('Время работы f3:', round(time_of_f3, 2))
