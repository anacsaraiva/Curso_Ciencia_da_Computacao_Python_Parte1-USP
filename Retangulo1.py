# Recebe dois números inteiros correspondendtes à largura e à altura de um retângulo, respectivamente. O programa deve imprimir uma cadeia de caracteres que represente o retângulo informado com caracteres '#' na saída. 
largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))
i = 0
j = 0
while i < altura:
    while j < largura:
        print("#",end="")
        j +=1
    print()
    j = 0
    i += 1
