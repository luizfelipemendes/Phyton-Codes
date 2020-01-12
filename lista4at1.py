#Lista de palavras String


def transforma_string_emlistade_palavras(texto):
    listaPalavras = []
    palavra = ""

    for x in texto:
        if(x!= ""):
            palavra+= x
        else:
            listaPalavras.append(palavra)
            palavra=""
    listaPalavras.append(palavra)
    return listaPalavras
