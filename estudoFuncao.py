
funcao = input("Entre com função:")

type = input("Digite o tipo da função")

if type == "Polinomial" or type == "Exponencial":
    print("São contínuas em R")
if type == "Logarítma":
    print("São contínuas em R+")
else:
    print("São contínuas em seu domínio")

print(type)

