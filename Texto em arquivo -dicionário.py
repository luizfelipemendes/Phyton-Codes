#Texto em arquivo -dicionário


dicionario ={}
acessoarq = open("poema_phyton.txt", "r")

for palavra in acessoarq:
    for chave in dicionario:
        if palavra in dicionario:
            print("Palavra ja contém no dicionario")
            contador = contador +1
        else:
            dicionario['palavra'] = '1'


print(dicionario)
