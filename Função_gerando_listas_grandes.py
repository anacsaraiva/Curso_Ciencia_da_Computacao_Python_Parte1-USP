def lista_grande(n):

    lista = []

    for i in range(n):

        if i%2 == 0:
            lista.append((i+2)**(i+1))
        else:
            lista.append((i+1)**(i+2))
    return lista
