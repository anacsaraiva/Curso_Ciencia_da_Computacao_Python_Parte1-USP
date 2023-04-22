#Recebe um número inteiro maior ou iguall a 2 como parâmetro e devolve o maior número primo menos ou igual ao número passado à função.

def éPrimo(n):

    Primo = 1
    i = 2

    while i < n:

        if n % i == 0:

            Primo=0
            break
        
        else:
            i +=1
    return Primo

def maior_primo(x):

    primalidade = 0

    while primalidade == 0:
        
        primalidade = éPrimo(x)

        if primalidade == 1:
            return x
        else:
            x -=1
