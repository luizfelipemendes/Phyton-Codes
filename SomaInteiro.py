'''
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Graduando em Sistemas de Informação
IF968 - Programação 1

Autor: Luiz Felipe Borges de Melo Mendes
Email: lfbmm@cin.ufpe.br

Copyright(c) 2018 Luiz Felipe Borges de Melo Mendes
'''

#SOMA DE DOIS VALORES

contador = 1
soma = 0
number1 = 0

while number1 != contador:
    number1 = int(input("Digite o primeiro número"))

    if number1 == 0:
        contador = 0
        print(" Voccê digitou 0")
        print(" A soma dos valores é:", soma)

    else:
        soma = number1 + soma
        print(" A soma dos valores é:", soma)
        

