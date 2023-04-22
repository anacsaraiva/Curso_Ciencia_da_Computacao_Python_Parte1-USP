largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))
i = 1
j = 1
while i <= altura:
    while j <= largura:
        if i == 1 or i == altura:
            print("#",end="")
        else:
            if  j == 1 or j == largura:
                print("#",end="")
            else:
                print(end=" ")
        j +=1
    print()
    j = 1
    i += 1
