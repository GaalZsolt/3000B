def feladat6(lista):
    print("6. Igaz-e, hogy minden szám pozitív?")
    i = 0
    igen = True
    while i < len(lista) and igen:
        if int(lista[i]) % 2 == 0:
            igen = False
    print("Igen az összes pozitív"if igen else "Nem, van negatív is")