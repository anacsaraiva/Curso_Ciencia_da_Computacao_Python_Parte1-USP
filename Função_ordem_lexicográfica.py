#Recebe uma lista de strings como parâmetro e devolve o primeiro string na ordem lexicográfica.

def primeiro_lex(lista):

    resultado = lista[0]

    for i in lista:
        if ord(i[0]) <ord(resultado[0]):
            resultado = i

    return resultado
