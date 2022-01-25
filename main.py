
from elso import feladat1
from masodik import feladat2
from harmadik import feladat3
from negyes import feladat4
from otodik import feladat5
from hatos import feladat6

lista = []
with open('input.txt', 'r', encoding='utf8') as f:
    for sor in f:
        lista.append(sor)

elso_feladat = feladat1(lista)
print("igen" if elso_feladat else "nem")
feladat2(lista)
print(feladat3(lista))
feladat4(lista)
print(feladat5(lista))
feladat6(lista)
