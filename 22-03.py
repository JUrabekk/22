#Требуется по запросу выдавать N различных паролей длиной M символов, состоящих
#из строчных и прописных латинских букв и цифр, кроме тех, которые легко перепутать
#между собой: «l» (L маленькое), «I» (i большое), «1» (цифра), «o» и «O» (большая и
#маленькая буквы) и «0» (цифра).
#Решение должно содержать две функции: вспомогательную generate_password(m),
#возвращающую случайный пароль длиной m символов, и основную main(n, m),
#возвращающую список из n различных паролей, каждый длиной m символов.
#Будем считать, что параметры n и m всегда таковы, что требуемые пароли возможно
#сгенерировать.

import random

st1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'p', 'a', 's', 'd', 'f', 'g',
       'h', 'j', 'k', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
st2 = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'P', 'A', 'S', 'D', 'F', 'G', 'H',
       'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
st3 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
st4 = st1 + st2 + st3


def generate_password(m):
    pas = []
    pas.append(random.choice(st1))
    pas.append(random.choice(st2))
    pas.append(random.choice(st3))
    for i in range(0, m - 3):
        pas.append(random.choice(st4))
    random.shuffle(pas)
    return ''.join(pas)


def main(n, m):
    list_passw = set()
    while len(list_passw) < n:
        list_passw.add(generate_password(m))
    return list_passw


print("Случайный пароль из 7 символов: %s" % generate_password(7))
print("10 случайных паролей длиной 15 символов: ")
print(*main(10, 15), sep="\n")