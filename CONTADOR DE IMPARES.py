'''
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Graduando em Sistemas de Informação
IF968 - Programação 1

Autor: Luiz Felipe Borges de Melo Mendes
Email: lfbmm@cin.ufpe.br

Copyright(c) 2018 Luiz Felipe Borges de Melo Mendes
'''

#CONTADOR DE IMPARES

numero = 0
contador = 0
soma = 0

while contador !=5:
    numero = int(input("Digite o numero"))
    rest= numero %2

    if rest !=0:
        soma = soma + numero
        contador = contador + 1
print("A soma dos números ímpares é:  ", soma)

