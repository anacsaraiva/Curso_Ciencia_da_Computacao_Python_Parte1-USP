#Recebe duas matrizes como parâmetro e devolve True se as matrizes forem multiplicavéis.

def sao_multiplicaveis(m1,m2):
    coluna1 = len(m1[0])
    linha2 = len(m2)

    if coluna1==linha2:
        return True
    else:
        return False
    
