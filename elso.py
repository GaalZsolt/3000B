# 1. Van-e a sorozatban pozitív szám?

def feladat1(lista):
    print("1. Van-e a sorozatban pozitív szám?")
    for a in lista:
        if 0 < int(a):
            return True
    return False