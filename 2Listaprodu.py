#Lista de produtos


contador = 0
quantidade = 0
rejeitados = 0
produto = "aaa"
listaprod = []


while produto != "FIM":
    print("Digite a sua lista de produtos")
    produto = input()
    if produto in listaprod:
        print("Produto já cadastrado na lista, tente novamente")
        rejeitados = rejeitados + 1
    else:
        if produto != "FIM":
            listaprod.append(produto)
            quantidade = quantidade + 1
               
print(listaprod)
print("Produtos cadastrados na lista:", quantidade)
print("Produtos rejeitados na lista:", rejeitados)
