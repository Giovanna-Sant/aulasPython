'''frase = "Hello world"

for i in range(10):
    print(frase)

plv1 = "Olá"
plv2 = "mundo"
print(plv1 + plv2)
frase = plv1 + plv2
print(frase)

frase = 'Eu'
print(frase)
frase = frase + " sou"
print(frase)
frase = frase + " a"
print(frase)
frase = frase + " Giovanna"
print(frase)

pal1 = input("Diga a primeira palavra: ")
pal2 = input("Diga a segunda palavra: ")

frase = pal1 + " " + pal2
print(frase)

frase = input("Diga a primeira palavra: ")
print(frase)
frase = frase + " " + input("Diga a segunda palavra: ")
print(frase)
frase = frase + " " + input("Diga a terceira palavra: ")
print(frase)
frase = frase + " " + input("Diga a quarta palavra: ")
print(frase)
frase = frase + " " + input("Diga a quinta palavra: ")
print(frase)

a = 3
b = 2
print(type(a))
soma = a + b
sub = a - b
divisao = a / b
mult = a * b
quad = a ** b
print(soma, sub, divisao, mult, quad)
nome = input("Digite seu nome:")
valor1 = int(input(f"Seja bem-vindo {nome}! Digite o primeiro número: "))
valor2 = int(input("Digite o segundo número: "))

soma = valor1 + valor2
sub = valor1 - valor2
divisao = valor1 / valor2
mult = valor1 * valor2
quad = valor1 ** valor2
print(f"A soma de {valor1} e {valor2} é {soma}")
print(f"A subtração de {valor1} e {valor2} é {sub}")
print(f"A divisão de {valor1} e {valor2} é {divisao}")
print(f"A multiplicação de {valor1} e {valor2} é {mult}")
print(f"O número de {valor1} elevado a {valor2} é {quad}")

a = 3
b = 6
print(f"O resultado de {a} > {b} é {a > b}")
print(f"O resultado de {a} < {b} é {a < b}")
print(f"O resultado de {a} >= {b} é {a >= b}")
print(f"O resultado de {a} <= {b} é {a <= b}")
print(f"O resultado de {a} == {b} é {a == b}")
print(f"O resultado de {a} != {b} é {a != b}")

print(True and False)
print(3>1 and 5>3)

a = 3
b = 5

print(f"{a} > {b} and {a} == {b}, ou seja, {2 > 3} and {3 == 2} dá {2 > 3 and 3 == 2}")
print(f"{a} > {b} and {a} < {b}, ou seja, {2 > 3} and {3 > 2} dá {2 > 3 and 3 < 2}")
print(f"{a} >= {b} and {a} != {b}, ou seja, {2 >= 3} and {3 != 2} dá {2 >= 3 and 3 != 2}")
print(f"{a} != {b} and {a} > {b}, ou seja, {2 != 3} and {3 > 2} dá {2 != 3 and 3 > 2}")

print(f"{a} > {b} or {a} == {b}, ou seja, {2 > 3} or {3 == 2} dá {2 > 3 or 3 == 2}")
print(f"{a} < {b} or {a} < {b}, ou seja, {2 < 3} or {3 < 2} dá {2 < 3 or 3 < 2}")
print(f"{a} >= {b} or {a} != {b}, ou seja, {2 >= 3} or {3 != 2} dá {2 >= 3 or 3 != 2}")
print(f"{a} != {b} or {a} > {b}, ou seja, {2 != 3} or {3 > 2} dá {2 != 3 or 3 > 2}"

idade = int(input("Digite sua idade:"))
if idade >= 18:
    print('aoooba')
else:
    print('esconde pae')'''

'''idoso = input("Você é idoso?\n->")
deficiente = input("Você possui deficência?\n->")

if idoso == 'sim' or deficiente == 'sim':
    print("Estacione aqui🤩")
else:
    print("vaza fiot 🤢🤢😲😲☹☹")'''

idoso = input("Você é idoso?")
cartao = input("Você possui o cartão de idoso?")

if idoso == 'sim' and cartao == 'sim':
    print('pode botar o fusca veinho 👩🏻‍🤝‍🧑🏻👩🏻‍🤝‍🧑🏻🕷🕷🐌🤓')
else:
    print("mete marcha mlk 🤬🤬🤬🤬")