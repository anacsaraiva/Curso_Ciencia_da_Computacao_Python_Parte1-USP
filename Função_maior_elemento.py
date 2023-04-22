#Recebe uma lista com números inteiros e devolve um número inteiro correspondente ao maior valor presente na lista recebida.

def maior_elemento(lista):

    maior = lista[0]

    for i in lista:
        if i >= maior:
            maior = i
    return maior
