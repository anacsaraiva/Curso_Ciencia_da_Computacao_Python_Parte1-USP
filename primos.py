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
