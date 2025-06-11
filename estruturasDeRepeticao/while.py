'''print(4%2)

i = 0
pares = 0
num = int(input(f"Digite o {i+1}° número:"))

if num%2 == 0:
    print(f"{num} é par!!")
    pares = pares + 1
else:
    print(f"{num} é impar")

i = 0
pares = 0
while i < 5:
    num = int(input(f"Digite o {i+1}° número:"))
    if num%2 == 0:
        pares = pares + 1
    i = i + 1

print(f"Você digitou {pares} números pares e {i - pares} números ímpares")

senha = "1234"
tentativa = input("Digite a senha")
quant = 0
while tentativa != senha and quant < 2:
    tentativa = input("Senha errada. Digite a senha:")
    quant = quant + 1

if tentativa == senha:
    print("liberado")
else:
    print("bloqueado")

sex = input("digite o seu sexo \n - Fem \n - Masc\n->")
while sex != "Fem" and sex != "Masc":
    sex = input("Sexo inválido, fico d xerecs 🤢🤢🤢🤢 \ndigite o seu sexo novamente \n - Fem \n - Masc\n- >")
print(f"seu sexo eh {sex}")

sex = input("digite o seu sexo \n - Fem \n - Masc\n->")
while not (sex == "Fem" or sex == "Masc"):
    sex = input("Sexo inválido, fico d xerecs 🤢🤢🤢🤢 \ndigite o seu sexo novamente \n - Fem \n - Masc\n- >")
print(f"seu sexo eh {sex}")

#jeito melhor
valor = input("Digita algo")

while not valor.isnumeric():
    valor = input("não eh um numero. digita um numero de vdd")
print(f"boa lek, {valor} é um numero")

#jeito bonm tambem
valor = input("Digita algo")

while valor.isnumeric() == False:
    valor = input("não eh um numero. digita um numero de vdd")
print(f"boa lek, {valor} é um numero")
'''

num = input("Digite um valor:\n")
while not num.isnumeric():
    num = input("Digite um valor real:\n")
#conversão da string para inteiro
num = int(num)
print(f"{num} * 4 = {num * 4}")