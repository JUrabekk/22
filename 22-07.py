#Существует предположение о существовании трех биологических ритмов человека:
#физического, эмоционального и интеллектуального.
#Согласно этому предположению, человек как часть природы представляется
#связанным с разными небесными телами, которые его окружают: звездами, Солнцем,
#Луной и, конечно же, Землей.
#Считается, что физический биоритм формируется за счет магнитного поля Земли с
#длительностью периода примерно 23 дня, эмоциональный зависит от лунных циклов и
#вращения Луны вокруг Земли с периодом примерно 28 суток, интеллектуальный с
#периодом 33 дня зависит от вращения Земли по своей орбите вокруг Солнца.
#Пусковым механизмом для всех трех биоритмов является рождение человека.
#Графики биоритмов представляют собой синусоиды. Значение биоритма в любой день
#для каждого человека можно рассчитать по формуле:
#B = sin((2 ∗ pi ∗ T)∕P) ∗ 100%,
#где P - период биоритма в сутках, T - количество дней, прошедших с рождения
#человека до момента расчета.
#Напишите программу, которая производит расчет биоритмов по введенным датам.

import datetime
from math import sin, pi


def bio_rhythm(P, T):
    return sin(2.0 * pi * T / P) * 10


date_entry = input('Введите дату рождения в формате dd.mm.YYYY ')
year0, month0, day0 = map(int, date_entry.split('.'))
date0 = datetime.date(day0, month0, year0)

date_entry = input('Введите дату расчета в формате dd.mm.YYYY ')
year, month, day = map(int, date_entry.split('.'))
date = datetime.date(day, month, year)

T = (date - date0).days

print(bio_rhythm(23, T))
print(bio_rhythm(28, T))
print(bio_rhythm(33, T))
