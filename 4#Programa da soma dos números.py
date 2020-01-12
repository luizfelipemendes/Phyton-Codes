#Programa da soma dos números


soma = 0

while soma == 0:
    print("Digite um número")
    num1 = int(input())
    if num1 == 0:
        print(soma)
        break
    else:
        print("Digite outro número")
        num2 = int(input())
        soma = num1 + num2
        print(soma)


