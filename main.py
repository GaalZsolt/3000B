
from elso import feladat1
from harmadik import feladat3

lista = []
with open('input.txt', 'r', encoding='utf8') as f:
    for sor in f:
        lista.append(sor)

elso_feladat = feladat1(lista)
print("igen" if elso_feladat else "nem")
print(feladat3(lista))
