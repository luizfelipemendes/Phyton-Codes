#Adivinha Numero Maior ou Menor#


palpites = True

while palpites == True:
    print("Digite o primeiro número")
    n1 = int(input())
    if n1 > 0 and n1 < 100:
        palpite == True
    else:
        print("Digite um  valor entre 0 e 100")
        print("Digite o primeiro número")
        n1 = int(input())
        if n1 > 0 and n1 < 100:
            paplpite == True
        else:
            palpites = False
            print("Você errou novamente, jogo encerrado")
    print("Digite o o segundo número")
    n2 = int(input())
    if n2 > 0 and n2 < 100:
        palpite == True
    else:
        print("Digite um  valor entre 0 e 100")
        print("Digite o segundo número")
        n2 = int(input())
        if n2 > 0 and n2 < 100:
            paplpite == True
        else:
            palpites = False
            print("Você errou novamente, jogo encerrado")
    print("Digite o primeiro palpite")
    palpite1 = int(input())
    if palpite1 > n1 or palpite1 > n2:
        print("Seu paplpite é maior que os números indicados")
    elif palpite1 < n1 or palpite1 < n2:
        print("Seu palpite é menor que os números indicados")
    elif palpite1 == n1 or palpite1 == n2:
        print("Seu palpite é igual a um dos números indicados")
    elif palpite1 > n1 and palpite1 < n2:
        print("Seu palpite esta entre os números indicados")
    elif palpite1 > n2 and palpite1 < n1:
        print("Seu palpite esta entre os números indicados")
    elif palpite1 == n1 and palpite == n2:
        print("Você ja digitou esse palpite, tente novamente")
    print("Digite o segundo palpite")
    palpite2 = int(input())
    if palpite2 > n1 or palpite2 > n2:
        print("Seu paplpite é maior que os números indicados")
    elif palpite2 < n1 or palpite2 < n2:
        print("Seu palpite é menor que os números indicados")
    elif palpite2 == n1 or palpite2 == n2:
        print("Seu palpite é igual a um dos números indicados")
    elif palpite2 > n1 and palpite2 < n2:
        print("Seu palpite esta entre os números indicados")
    elif palpite2 > n2 and palpite2 < n1:
        print("Seu palpite esta entre os números indicados")
    elif palpite2 == n1 and palpite2 == n2:
        print("Você ja digitou esse palpite, tente novamente")

print("Fim de Jogo")
