#Programa para dropadores#

contagem = 0

p1 = "Daniel tem um cabelo com a franja lambida?"
resposta1 = "Sim"

p2 = "Qual o maior pivô de Recife?"
resposta2 = "Italo"

p3 = "Você gosta de suco de Caju gelado?"
resposta3 = "Sim"

#Vamos começar#

print(p1)
resposta = input()
if resposta == resposta1:
    print("Você acertou, Daniel peida na salsicha")
    contagem = contagem + 1
else: print("Você errou, claramente ele tem cabelo de clara de ovo")

print(p2)
resposta = input()
if resposta == resposta2:
    print("Você acertou, Ítalo mais conhecido como Zé Comeia segura bola para os outros")
    contagem = contagem + 1
else: print("Você errou, um rei se identifica pelo seu anel de ouro")

print(p3)
resposta = input()
if resposta == resposta3:
    print("Você acertou, Gosto de suco de caju gelado na jarra")
    contagem = contagem + 1
else: print("Você errou, Caju é vida meu bem")

print("Sua pontuação é:")
print(contagem)



