def feladat5(lista):
    print('5. Mennyi a sorozatban található számok átlagának a fele?')
    sum = 0
    for e in lista:
        sum+=int(e)
    return (sum/len(lista))/2
        

