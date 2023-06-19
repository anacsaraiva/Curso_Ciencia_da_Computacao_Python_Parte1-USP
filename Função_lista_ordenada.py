def ordenada(lista):
    
    menor = lista[0]

    for i in range(len(lista)):
        if menor > lista[i]:
            return False
        else:
            menor = lista[i]
    return True
