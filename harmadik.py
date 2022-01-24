# 3. Mennyi a sorozatban található legkisebb szám?

from logging import exception


def feladat3(lista) -> int:
    min = int(lista[0])
    for a in lista:
        if min < int(a):
            min = int(a)
    return min
