# 1. Van-e a sorozatban pozitív szám?

def feladat1(lista):
    for a in lista:
        if 0 < int(a):
            return True
    return False