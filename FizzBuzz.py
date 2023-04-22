# Recebe um número inteiro e verifica se é divisível por 3 e por 5, se sim imprimi FizzBuzz caso contrário imprime o mesmo número que foi dado na entrada.

numero = int(input("Digite um numero"))

if numero%3 == 0 and numero%5==0:
	print("FizzBuzz")
else:
	print(numero)
