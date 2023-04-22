#Função que recebe uma lista com números inteiros, verifica se tal lista possui elementos repetidos e os remove.

def remove_repetidos(lista):

    lista2 = []
    
    for i in lista:
        if i not in lista2:
            lista2.append(i)
            
    lista2.sort()
    return lista2
        
    
