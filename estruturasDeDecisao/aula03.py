'''a = 2
b = 3

print(f"{a} < {b} and {a} != {b}, ou seja, {a<b} and {a!=b}, resulta {a<b and a!=b}")
idoso = input("Você é idoso? \n->")
cartao = input("VocÊ possui cartão do idoso?")
if idoso == 'sim' and cartao == 'sim':
    print("estaciona paizao!")
else:
    print('mete marcha!!!!')

deficiente = input("Você é deficiente?")

if idoso == "sim" or deficiente == "sim":
    print("estaciona paizao!")
else:
    print('mete marcha!!!!')

# Exercícios
# 1. Vogais
insert = input("Insira uma letra")
if insert == "a" or insert == "e" or insert == "i" or insert == "o" or insert == "u":
    print("é uma vogalll!!!")
else:
    print("é uma consoanteeee")

# em valores preenchidos, é lido como verdadeiro.
if -89 or 1 or "a":
    print("oie")

# em valores nulos, é lido como falso.
if 0 or "":
    print("tchay")

# 2. Times

time = input("Diga o time que você torce! \n->")
if time == "Sãu Paulo":
    print("ki nojoooooo!!! 🤣🤣🤢🤢🤮🤮")
elif time == "Palmeiras":
    print("Faz o pix tia leila")
elif time == "Corinthians":
    print("2005 foi lindo 😛😛, vai curintia")
elif time == "Santos":
    print("o maior da série b!!!")
else:
    print("vai p bahia paizaokkk")

#3. Imposto de Renda
salario = float(input("Digite o seu salário"))
calculo = float

if salario <= 2259.20:
    print("Você não paga imposto, boa pobrete!")

elif salario <= 2826.65:
    calculo = salario * 0.075

elif salario <= 3751.05:
    calculo = salario * 0.15

elif salario <= 4664.68:
    calculo = salario * 0.225

else:
    calculo = salario * 0.275

salario = salario - calculo
print(f"Você precisa pagar {calculo} de IRFP e seu salário restante será de {salario}")
nome = input("qual ter vulgo cria 😛😛😝🖖🤘")
entrar = input(f"{nome}, você deseja entrar na calculadora?")
if entrar == "sim":
    num1 = int(input("Digite o primeiro número\n->"))
    num2 = int(input("Digite o segundo número\n->"))

    operacao = int(input("Digite o número da operação desejável:\n-> 1. Soma \n-> 2. Subtração\n-> 3. Multiplicação \n-> 4. Divisão\n->"))
    resultado = "inválido"

    if operacao == 1:
        resultado = num1 + num2
    elif operacao == 2:
        resultado = num1 - num2
    elif operacao == 3:
        resultado = num1 * num2
    elif operacao == 4:
        resultado = num1 / num2
    else:
        print("A operação digitada não é válida")

    print(f"O resultado da operação é {resultado}")
else:
    print("falo fera")'''