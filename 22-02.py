#Вам даётся список учеников.
#Напишите программу для игры в «тайного друга».
#Она должна случайным образом назначить каждому ученику тайного друга, который
#будет незаметно делать для этого ученика что-то хорошее.
#Обратите внимание, что нельзя быть тайным другом самому себе и нельзя быть
#тайным другом для нескольких учеников

def all_perms(arr):
    n = len(arr)
    if (n == 1):
        return [arr]
    else:
        tmp = all_perms(arr[1:])
        a = arr[0]
        res = []
        for b in tmp:
            for i in range(n):
                z = b
                res = res + [z[0:i] + [a] + z[i:]]
        return res


def check(lst):
    for pair in lst:
        if pair[0] == pair[1]:
            return False
    return True


def all_sec_friends(s):
    perms = all_perms(s)
    raw = list(map(lambda p: list(zip(s, p)), perms))
    return list(filter(check, raw))


print(all_sec_friends(["Иван Иванов", "Саша Самойлов", "Юля Северная"]))
