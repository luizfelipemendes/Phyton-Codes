#Perguntas e Repostas#

perguntaAtual = 0
respostaAtual = 0
pontos = 0

p1 = "Qual a capital da Croácia?"
p2 = "Em que ano Python 1.0 tornou-se disponível?"
p3 = "Qual o nome do segundo álbum do Vampire Weekend?"
p4 = "Quantos lados tem um dado"
p5 = "Quantas copas do mundo tem o Brasil?"

rp1 = "Zagreb"
rp2 = "1994"
rp3 = "Contra"
rp4 = "6"
rp5 = "5"

perguntas = [p1, p2, p3, p4, p5]
respostas = [rp1, rp2, rp3, rp4, rp5]

while perguntaAtual < len(perguntas):
    print(perguntas[perguntaAtual])
    rp = input()
    if rp == respostas[respostaAtual]:
        perguntaAtual = perguntaAtual + 1
        respostaAtual = respostaAtual + 1
        pontos = pontos + 1
        print("Você acertou, parabéns txio")
    else:
        print("Você errou burro, tente de novo")
        perguntaAtual = perguntaAtual + 1
        respostaAtual = respostaAtual + 1

print("Sua pontuação é", pontos)

        
      
