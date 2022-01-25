def feladat8(lista):
    print("8. Van-e a sorozatban olyan negatív szám, amelyet újabb negatív követ?")
    i = 0
    van = False
    while i < len(lista)-1 and not van:
        if int(lista[i]) < 0 and int(lista[i+1]) < 0:
            van = True
        i += 1
    print("Van ilyen számkombináció" if van else "Nincs ilyen számkombináció")