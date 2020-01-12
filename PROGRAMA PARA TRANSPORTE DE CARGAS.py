#PROGRAMA PARA TRANSPORTE DE CARGAS#


#Códigos dos dias da semana#

controle = 1 

while controle != 0:
    print("Digite seu código relacionado ao dia da semana")
    codigo = int(input())
    
    if codigo < 1 or codigo > 7:
        controle = 0
        print("Dia da semana invalido")

    else:
        print("Quantas caixas serão transportadas?")
        caixas = int(input())
        qtcaixas = (0.7 * 0.8 * 0.6) * caixas
        qtcaminhoes = qtcaixas // 20
        if qtcaminhoes == qtcaixas // 20:
           qtcaminhoes = qtcaminhoes + 1 
        if codigo == 1 or codigo == 2 or codigo == 3:
           preco = qtcaixas * 25
           controle = 0
        elif codigo == 4 or codigo == 5:
            preco = qtcaixas * 30
            controle = 0
        elif codigo == 5 or codigo == 6:
            preco = qtcaixas * 40
            controle = 0
        print("A quantida de caminhões utilizada para transporte foi de:", qtcaminhoes)
        print("O custo para o transporte no dia indicado é", preco)


print("End")

   



    
    
    
    
    









