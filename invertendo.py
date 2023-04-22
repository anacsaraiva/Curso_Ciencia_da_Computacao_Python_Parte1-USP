
recebe = 1
lista = []

while recebe != 0:
    recebe = int(input("Digite um número: "))

    if recebe != 0:
        lista.append(recebe)
        
tam = len(lista)-1

for i in lista:
    print(lista[tam])
    tam -= 1
    

        
