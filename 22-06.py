#Требуется по запросу выдавать N различных паролей длиной M символов, состоящих
#из строчных и прописных латинских букв и цифр, кроме тех, которые легко перепутать
#между собой: «l» (L маленькое), «I» (i большое), «1» (цифра), «o» и «O» (большая и
#маленькая буквы) и «0» (цифра).
#Дополнительное условие: в каждом пароле обязательно должна присутствовать хотя
#бы одна цифра и как минимум по одной букве в верхнем и нижнем регистре.
#Решение должно содержать две функции: вспомогательную generate_password(m),
#возвращающую случайный пароль длиной m символов, и основную main(n, m),
#возвращающую список из n различных паролей, каждый длиной m символов.
#Будем считать, что параметры n и m всегда таковы, что требуемые пароли возможно
#сгенерировать.

import secrets

symbols = 'ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz23456789'
a = int(input("Сколько символов в паролей? "))
b = int(input("Сколько паролей? "))
count = 0
passlist = []
while count < b:
    while True:
        password = ''.join(secrets.choice(symbols) for i in range(a))

        if (any(c.islower() for c in password) and any(c.isupper() for c in password)
                and any(c.isdigit() for c in password)):
            break
    count += 1
    passlist.append(password)
print(passlist)