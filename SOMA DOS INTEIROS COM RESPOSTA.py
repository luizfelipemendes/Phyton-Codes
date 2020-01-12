'''
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Graduando em Sistemas de Informação
IF968 - Programação 1

Autor: Luiz Felipe Borges de Melo Mendes
Email: lfbmm@cin.ufpe.br

Copyright(c) 2018 Luiz Felipe Borges de Melo Mendes
'''

#SOMA DOS INTEIROS COM RESPOSTA

soma = 0
resposta = "s"
number = 0


while resposta == "s":
    number = int(input("Digite um numero"))
    soma = number + soma
    resposta = input("Deseja continuar?")

while resposta != "s" or resposta!= "n":
    if resposta == "s":
        number = int(input("Digite um numero"))
        soma = number + soma
        resposta = input("Deseja continuar?")
    else:
        resposta == "n"
        
print("A soma dos valores é:", soma)
    
    
    
