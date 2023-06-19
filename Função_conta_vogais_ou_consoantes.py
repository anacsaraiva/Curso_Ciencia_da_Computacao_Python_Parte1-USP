#Recebe primeiro uma string contendo uma frase e como segundo parâmetro uma outra string como "vogais" ou "consoantes" e retorna a contagem referente ao segundo parametro inserido.

def conta_letras(frase,contar="vogais"):

    count = 0
    frase = frase.replace(" ",'')

    for i in range(len(frase)):
        if frase[i] == 'a' or frase[i] == 'e' or frase[i] =='i' or frase[i] == 'o' or frase[i] == 'u':
            count +=1

    if contar == "consoantes":
        return len(frase) - count
    else:
        return count
    
            
