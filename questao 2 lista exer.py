# Lista Supermercado



lista=[]
contador = 0
cadastrados = 0
var="start"


while(var=="start"):
    N="la"
    produto = input("Digite o produto: ")
    if produto == "FIM":
        var="FIM"
    for elemento in lista:
        if produto == elemento:
            N = "achei"
    if (N=="achei"):
        contador=contador +1
    else:
        lista.append(produto)
        cadastrados = cadastrados + 1
        
    
        


cadastrados = cadastrados - 1
lista.remove(lista[-1])
print(lista)
print(cadastrados)
print(contador)



        
    
