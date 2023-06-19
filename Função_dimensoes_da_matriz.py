#Recebe uma matriz como parâmetro e imprime as dimensões da matriz recebida, no formato iXj.

def dimensoes(matriz):

    linhas = len(matriz)
    coluna = len(matriz[0])

    return print("{}X{}".format(linhas,coluna))
