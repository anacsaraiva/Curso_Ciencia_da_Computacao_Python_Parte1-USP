#Recebe 3 números inteiros e verifica se eles foram dados em ordem crescente.

n1= int(input())
n2 = int(input())
n3 = int(input())

if n1<=n2 and n2<=n3:
	print("crescente")
else:
	print("não está em ordem crescente")
