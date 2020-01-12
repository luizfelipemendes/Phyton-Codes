#MEDIA LISTA

lista = []
tamanholista = 0
numlista = "000"
soma = 0
contador = 0
media = 0

while numlista != "":
    print("Digire um número")
    numlista = input()
    if numlista != "":
        lista.append(int(numlista))
        tamanholista = tamanholista + 1
    
while contador < tamanholista:
    soma = soma + lista[contador]
    contador = contador + 1

media = soma / tamanholista


print(lista)
print(soma)
print(media)



