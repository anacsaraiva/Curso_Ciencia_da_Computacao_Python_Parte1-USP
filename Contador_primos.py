#Recebe como argumento um número inteiro maior ou igual a 2 como parâmetro e devolve a quantidade de números primos que existem entre 2 e n.

def éPrimo(x):

    Primo = True
    i = 2

    while i < x:

        if x % i == 0:

            Primo=False
            break
        
        else:
            i +=1
            
    return Primo

def n_primos(n):

    cont = 0

    while n >= 2:
        primalidade = éPrimo(n)

        if primalidade:
            cont +=1
            n -=1
        else:
            n-=1
    return cont
