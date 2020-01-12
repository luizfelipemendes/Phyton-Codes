#Imprime inverso#

def invert(numero):
    alg1 = (numero - (numero % 100)) // 100
    alg2 = numero % 100 // 10
    alg3 = numero % 10
    return (alg3*100 + alg2* 10 + alg1)

print("Digite um número com 3 algarismos")
numero = int(input())
resultado = invert(numero)
print(resultado)

