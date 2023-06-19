#Recebe 2 matrizes e devolve uma matriz que represente sua soma caso as matrizes tenham dimensões iguais. Caso contrário, a função deve devolver False.

def dimensoes(matriz):
    linha = len(matriz)
    coluna = len(matriz[0])

    return linha,coluna

def soma_matrizes(m1,m2):

    matriz = []

    if dimensoes(m1) == dimensoes(m2):
        for i in range(len(m1)):
            linha = []
            for j in range(len(m1[0])):
                linha.append(m1[i][j] + m2[i][j])
            matriz.append(linha)

    else:
        return False
    return matriz

    
