roupa = True
while roupa :
    roupa = False
    nome = int(input("Escreva um numero"))
    if nome == 5 :
        print("um numero que voce escrever e igual a 5")
    elif nome == 10 :
        print("o numero que voce escrever e igual a 10 ")
    else :
        print("o numero não é 5 e nem 10")

    sim = print ("digite sim para continuar e digite nao para parar")

    if sim == "sim":
        roupa = True
    elif sim == "não" or sim == "nao":
        roupa = False
