#Imprime inverso#

print("Digite um número com 3 algarismos")
numero = int(input())

alg1 = (numero - (numero % 100)) // 100
alg2 = numero % 100 // 10
alg3 = numero % 10


print(alg3, alg2, alg1)


    
