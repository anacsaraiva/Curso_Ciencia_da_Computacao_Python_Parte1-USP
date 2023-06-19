#Recebe uma frase como parâmetro e devolve uma string com as letras maiúsculas que existem nesta frase, na ordem em que elas aparecem.

def maiusculas(frase):

    lista = ''
    aux = frase

    for i in range(len(frase)):
        if ord(aux[i]) >= 65 and ord(aux[i]) <= 90:
            lista += aux[i]

    
    return lista
