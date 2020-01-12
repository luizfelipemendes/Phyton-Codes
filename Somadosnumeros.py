#SOMA DOS ALGARISMOS#

soma = 0

print("Digite um número")
n = int(input())


while n > 0:
    resto = n %10
    n = (n - resto) // 10
    soma = soma + resto
print(soma)
    
    
