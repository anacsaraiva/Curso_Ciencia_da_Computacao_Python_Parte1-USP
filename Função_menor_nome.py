#Recebe uma lista de strings com nome de pessoas como parâmetro e devolve o nome mais curto presente na lista.

def menor_nome(nomes):

    parametro = nomes[0].strip().capitalize()

    for i in range(len(nomes)):
        if len(nomes[i].strip()) < len(parametro):
            parametro = nomes[i].strip().capitalize()

    return parametro
            
