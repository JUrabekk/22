#Напишите функцию make_bingo(), которая возвращает кортеж кортежей с карточкой
#для игры бинго.
#Это карточка 5x5 с пустой центральной клеткой (она заполняется автоматически, пусть
#там будет 0).
#В остальных клетках — числа от 1 до 75
#Все числа должны быть разными.

import numpy.random as rnd
print(rnd.randint(1,75, size=(5,5)))
