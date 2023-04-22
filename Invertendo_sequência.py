#Recebe uma sequência de números inteiros e imprime todos os valores em ordem inversa. A sequência deve terminar pelo número 0. Note que 0 não deve fazer parte da sequência.

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
    

        
