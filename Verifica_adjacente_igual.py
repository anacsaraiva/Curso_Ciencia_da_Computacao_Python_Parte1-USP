#Recebe um número inteiro e verifica se o número recebido possui ao menos um dígito com um dígito adjacente igual a ele.

n = int(input("Digite um número inteiro"))

anterior = n%10
existe = False

while n==0 or existe==True:
        
        n = (n-anterior)/10
        div = n%10
	
        if div==anterior:
                existe=True
        else:
                anterior = div
                existe = False
	
if existe:
        print("sim")
else:
        print("não")
