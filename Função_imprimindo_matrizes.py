#Recebe uma matriz como parâmetro e imprime a matriz, linha por linha.

def imprime_matriz(matriz):

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end ="")
            if j != (len(matriz[0]))-1:
                print(" ",end="")
        print()
