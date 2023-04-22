#Recebe um número inteiro, calcula e imprime a soma dos dígitos deste número.

n = int(input("Digite um número inteiro"))
div =0
soma =0

while n != 0:
	div = n%10
	soma += div
	n = (n-div)/10
	
print(soma) 
