n = int(input("Digite um número inteiro positivo"))
i=1
primo=True

while i<=n:
        if n%i==0:
                if i == 1 or i == n:
                        i += 1
                else:
                        primo = False
                        break
        i+=1

if primo:
	print("primo")
else:
	print("nao primo")
