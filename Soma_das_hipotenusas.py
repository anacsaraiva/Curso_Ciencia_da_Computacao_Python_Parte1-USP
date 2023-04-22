# Recebe como parâmetro um número inteiro positivo n e devolva a soma de todos os inteiros entre 1 e n que são comprimento da hipotenusa de algum triângulo retângulo com catetos inteiros.

def é_hipotenusa(a, b):
    return ((a*a) + (b*b))

def soma_hipotenusas(n):
    c = 1
    soma = 0
    while (c <= n):
        _c = (c*c)       
        a = 1
        b = 1
        while (a < n):
            while (b < n):
                if (_c == é_hipotenusa(a, b)):
                    soma = soma + c
                    a = n
                    break
                b += 1
            a += 1
            b = a
        c += 1
  
    return soma
        
