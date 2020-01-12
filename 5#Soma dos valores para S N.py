#Soma dos valores para S/N

soma = 0
continuar = True
val = 0
while val != "s" or val != "n" or continuar == True:
    print("Digite uma valor")
    val = input()
    print("Deseja continuar?")
    val = input()
    if val == "s":
        continuar = True
    else:
        val == "n"
        break

    
