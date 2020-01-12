#Adivinha número#

controle = 3

print("Jogador 1 digite o número")
numero = int(input())
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")

while controle > 0 or palpite == numero:
    print("Jogador 2 digite o seu palpite")
    palpite = int(input())
    if palpite > numero:
        print("Seu palpite é maior que o número indicado, tente novamente")
        controle = controle - 1
    if palpite < numero:
        print("Seu palpite é menor que o número indicado, tente novamente")
        controle = controle - 1
    if palpite == numero:
        print("Parabéns o seu palpite igual ao número informado")
        controle = controle - 1
        print(palpite)


exit 

        
            







    
    


