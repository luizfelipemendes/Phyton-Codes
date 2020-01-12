#PROGRAMA LISTA DE PASSAGENS RECIFE#

controle = 1

print("Tabela de Destino e Preços")

print("   Destino    Código   Preços")
print("Salvador        1   R$", 126.30)
print("João Pessoa     2   R$", 67.00)
print("Fortaleza       3   R$", 164.87)
print("São Paulo       4   R$", 264.00)
print("Rio de Janeiro  5   R$", 282.34)
print("Porto Alegre    6   R$", 365.90)


while controle != 0:
    print("Digite o código respectivo ao destino escolhido acima")
    codigo = int(intput())
    print("Digtite o valor recebido pelo passageiro")
    vlrecebido = int(input())
    if codigo < 1 or codigo > 6:
        controle = 0
    else:
        if codigo == 1:
        elif vlrecebido < 126.30:
            controle = 0
        elif vlrecebido > 126.30:
            troco = vlrecebido - 126.30
            controle = 0
         elif vlrecbido == 126.30:
            troco = 0.0
            print("Seu troco é", troco)
            controle = 0
        if codigo == 2:
        elif vlrecebido < 67.00:
            controle = 0
        elif vlrecebido > 67.00:
            troco = vlrecebido - 67.00
            controle = 0
        elif vlrecbido == 67.00:
            troco = 0.0
            print("Seu troco é", troco)
            controle = 0
        if codigo == 3:
        elif vlrecebido < 164.87:
            controle = 0
        elif vlrecebido > 164.87:
            troco = vlrecebido - 164.87
            controle = 0
        elif vlrecbido == 164.87:
            troco = 0.0
            print("Seu troco é", troco)
            controle = 0
        if codigo == 4:
        elif vlrecebido < 264.00:
            controle = 0
        elif vlrecebido > 264.00:
            troco = vlrecebido - 264.00
            controle = 0
        elif vlrecbido == 264.00:
            troco = 0.0
            print("Seu troco é", troco)
            controle = 0
        if codigo == 5:
        elif vlrecebido < 282.34:
            controle = 0
        elif vlrecebido > 282.34:
            troco = vlrecebido - 282.34
            controle = 0
        elif vlrecbido == 282.34:
            troco = 0.0
            print("Seu troco é", troco)
            controle = 0
        if codigo == 6:
        elif vlrecebido < 365.90:
            controle = 0
        elif vlrecebido > 365.90:
            troco = vlrecebido - 365.90
                controle = 0
        elif vlrecbido == 365.90:
            troco = 0.0
            print("Seu troco é", troco)
            controle = 0
            
        
        
                
            
    

