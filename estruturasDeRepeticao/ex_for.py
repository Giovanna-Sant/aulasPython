'''vogais = 0
for char in "danilo":
    if char in {'a', 'e', 'i', 'o', 'u'}:
        vogais += 1
print(vogais)


lista = [3, True, 7, 2, "nome", []]
for elem in lista:
    print(elem)

for i in range(len(lista)):
    lista[i] = 1
print(lista)

lista = [3, True, 7.2, "nome", []]
for i in range(len(lista)):
    print(f"Lista[{i}] = {lista[i]}")

#somar numeros de  uma lista
numeros = [3, 5, 1, 67, 3, 2]
soma = 0

for num in numeros:
    soma += num
print(soma)

soma = 0
for i in range(len(numeros)):
    soma +=numeros[i]
print(soma)

alunos = ['Lucas Sena', 'Vinicius', 'Matheus Santos', 'Giovanna']
notas = [2, 6, 8, 5]
for i in range(len(notas)):
    if notas[i]>=6:
        print(f"O {alunos[i]} passou com {notas[i]}")

def verificaNum(msg):
    numero = input(msg)
    while not numero.isnumeric():
        numero = input(msg)
    numero = int(numero)
    return numero
    #variavel numero so existe dentro da função
quant = verificaNum("Quantos números você vai colocar na lista?")
ano =  verificaNum("Qual seu ano de nascimento?")
lista = []
while len(lista) < quant:
    num = verificaNum(f"Diga o {len(lista)+1}° número")
    lista.append(num)
print(lista)

while True:
    vinhos = ["Pérgola", "Sangue de boi", "Salton"]
    def forcaOpcao(msg, lista_opcoes):
        escolha = input(msg)
        while not escolha in lista_opcoes:
            escolha = input(msg)
        return escolha

    vinho = forcaOpcao("Qual vinho você quer?", vinhos)

    opcoes = ['s', 'n']
    continuar = forcaOpcao("Você deseja continuar? (s/n) ", opcoes)
    if continuar == "n":
        print("Encerrando programa...")
        break

vinhos = ["Pérgola", "Sangue de boi", "Salton"]

def forcaOpcao(msg, lista_opcoes):
    opcoes = join(lista_opcoes)
    escolha = input(msg)
    while not escolha in lista_opcoes:
        escolha = input(msg)
    return escolha


lista = [4, 6, 1, 3, 10]

def calcMedia(lista_num):
    soma = 0
    for num in lista_num:
        soma =+ num
    media = soma/len(lista_num)
    return media

media = calcMedia(lista)
print(media)

lista2 = [1, 2 ,3]
media = calcMedia(lista)
print(media)

lista = [8, 1, 6, 4 ,9]

def contarPares(lista_num):
    par = 0
    for num in lista_num:
        if num % 2 == 0:
            par += 1
    return par

pares = contarPares(lista)
print(pares)

lista = [1, 12, 4, 9, 4, 42]

def encontrarMaior(lista_num):
    maior = lista[0]

    for i in lista:
        print(f"{i} é maior que {maior}?")
        if i > maior:
            print(f"- Sim. vou trocar {maior} por {i}")
            maior = i
        else:
            print("- não é")
    return maior
maioral = encontrarMaior(lista)
print(f"o maior número é {maioral}")
'''
def join(lista_str, sep):
    ajuntado = lista_str[0]
    for i in range(len(lista_str)):
        ajuntado += sep + lista_str[i]
    return ajuntado

def forcaOpcao(msg, lista_opcoes):
    opcoes = join(lista_opcoes, "\n")
    escolha = input(msg)
    while not escolha in lista_opcoes:
        escolha = input(msg)
    return escolha

carros = ['gol bolinha', 'gol quadrado', 'mclaren senna']
precos = [12000, 15000, 1000000]
escolha = forcaOpcao("Qual carro te interessa?", carros)

def acha_index(lista, elem):
    for i in range(len(lista)):
        if lista[i] == elem:
            return i

indice_escolha = acha_index(carros, escolha)
print(f"O {escolha} custa {precos[indice_escolha]}")