


def anagrama(palavra1, palavra2):
    if len(palavra1) == len(palavra2):
        lista = []
        for i in range(len(palavra2)):
            lista.append(palavra2[i])
        print(lista)
        for i in range(len(lista)):
            for m in range(len(palavra1)):
                if palavra1[i] == palavra2[m]:
                    lista.remove(palavra2[m])
        if len(lista) == 0:
            return "OK"
        else:
            return "Não são anagrama"
    else:
        return "Não são"

print(anagrama('cao2','oac2'))




