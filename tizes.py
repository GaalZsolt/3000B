def feladat10(lista):
    print("10. Írjuk ki a sorozatban található 5-tel osztható számokat!")
    for sor in lista:
        if sor % 5 == 0:
            print(sor)