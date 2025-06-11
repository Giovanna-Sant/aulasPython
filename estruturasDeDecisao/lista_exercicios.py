'''#1. Dois valores
print("Descubra o maior valor!")
num1 = int(input("Insira o primeiro valor"))
num2 = int(input("Insira o segundo valor"))

if num1 == num2:
    print("Operação inválida, insira dois números diferentes")
elif num1 > num2:
    maior = num1
else:
    maior = num2

print(f"O maior número é {maior}")


#2. Voto
print("Será que você pode votar esse ano?")
ano = int(input("Digite o ano que você nasceu:\n->"))

if ano <= 2006:
    print("tira o título logo p votar q vc eh obrigado pai 👮‍♀️👮‍♀️")
elif ano <= 2008:
    print("se quiser pode votar lindao, mas eh opcional")
else:
    print("segura o dedao da urna, vc nn vota ainda nao 💂‍♂️💂‍♂️💂‍♂️")


#3. Senha
senha = "1234"
tentativa = input("Digite a senha")

if tentativa == senha:
    print("Acesso liberado!!!")
else:
    print("Senha incorreta!!!! BLOQUEADO🎅")


#4. Maçãs
maca = 0.25
quant = int(input("Quantas maçãs você quer comprar?"))

if quant < 12:
    maca = quant * 0.30

print(f"Comprando {quant} maçãs, você pagará R${maca:.2f}")
'''

#5. Ordem crescente
num1 = int(input("Digite o primeiro número:\n->"))
num2 = int(input("Digite o segundo número:\n->"))
num3 = int(input("Digite o terceiro número:\n->"))

if num1 == num2 or num2 == num3 or num3 == num1:
    print("burrooo!!!!kkkkk.. digita número diferente né pae... 👨‍🦰")

else:
    menor, medio, maior = num1, num2, num3

    if medio > maior:
        medio, maior = maior, medio
    if menor > maior:
        menor, maior = maior, menor
    if menor > medio:
        menor, medio = medio, menor

print(f"a ordem crescente eh {menor}, {medio} e {maior}")
f'''
##outra formoris 1 
num1 = int(input("Digite o primeiro número:\n->"))
num2 = int(input("Digite o segundo número:\n->"))
num3 = int(input("Digite o terceiro número:\n->"))

if num1 == num2 or num2 == num3 or num3 == num1:
    print("burrooo!!!!kkkkk.. digita número diferente né pae... 👨‍🦰")

else:
    if num1 > num2 and num1 > num3:
        aux = num1
        num1 = num3
        num3 = aux
    elif num2 > num3:
        aux = num2
        num2 = num3
        num3 = aux
    if num2 < num1:
        aux = num1
        num1 = num2
        numb = aux
    print(f"{num1}, {num2}, {num3})

##outra formoris 2
num1 = int(input("Digite o primeiro número:\n->"))
num2 = int(input("Digite o segundo número:\n->"))
num3 = int(input("Digite o terceiro número:\n->"))

if num1 == num2 or num2 == num3 or num3 == num1:
    print("burrooo!!!!kkkkk.. digita número diferente né pae... 👨‍🦰")

else:
    maior = a
    if b > maior:
        maior = b        
    menor = num1
    print(f"{num1}, {num2}, {num3})

#6. Peso Ideal
sex = int(input("Digite o número que corresponde ao seu sexo:\n-> 1. Feminino \n-> 2. Masculino\n->"))
alt = float(input(("Qual a sua altura em metros?\n->")))
if sex == 1:
    calculo = 62.1 * alt - 44.7
elif sex == 2:
    calculo = 72.7 * alt - 58
else:
    print("O valor digitado não é válido.")

print(f"O seu peso ideal é {calculo:.2f}kg")


#7 e 8. Polígonos
print("Bem vindo ao identificador de polígonos e calculadora de perímetro!")
lados = int(input("Informe o número de lados da sua forma\n"))

if lados <= 2:
    print("Não é um polígono!!")
elif lados > 5:
    print("Polígono não identificado, favor procure outro programa melhor!!!!")
else:
    cms = float(input("Agora, informe a medida do lado em centímetros\n"))
    per = cms * lados
    if lados == 3:
        poligono = "triângulo"
    elif lados == 4:
        poligono = "quadrado"
    else:
        poligono = "pentágono"

    print(f"O poligono informado é um {poligono} e seu perímetro é de {per}")


#9. Três maiores
num1 = int(input("Digite o primeiro número:\n->"))
num2 = int(input("Digite o segundo número:\n->"))
num3 = int(input("Digite o terceiro número:\n->"))

if num1 == num2 or num2 == num3 or num3 == num1:
    print("looooserrrr digita diferente")

elif num1 > num2 and num1 > num3:
    print(f"O maior número é o {num1}")
elif num2 > num3:
    print(f"O maior número é o {num2}")
else:
    print(f"O maior número é o {num3}")


#10. Medidas dos triângulos
print("Será que seu triângulo é isóceles, equilátero ou escaleno?🔮")
lado1 = float(input("Insira a medida do primeiro lado:\n->"))
lado2 = float(input("Insira a medida do segundo lado:\n->"))
lado3 = float(input("Insira a medida do terceiro lado:\n->"))
tri = ""

if lado1 == lado2 and lado1 == lado3:
    tri = "equilátero"
elif lado1 != lado2 and lado1 != lado3:
    tri = "escaleno"
else:
    tri = "isóceles"

print(f"O triângulo informado é {tri}!!")


#11. Ângulos dos triângulos
print("Será que seu triângulo é acutângulo, retângulo ou obtusangulo?\n* Lembrando que a soma dos ângulos de um triângulo sempre deve dar 180°!🔮🫴")
ang1 = float(input("Insira o primeiro ângulo (somente números):\n->"))
ang2 = float(input("Insira o segundo ângulo (somente números):\n->"))
ang3 = float(input("Insira o terceiro ângulo (somente números):\n->"))
tri = ""
if ang1 + ang2 + ang3 != 180:
    print("Isso não é um triangulo!!!!!")
else:
    if ang1 == 90 or ang2 == 90 or ang3 == 90:
        tri = "retângulo"
    elif ang1 > 90 or ang2 > 90 or ang3 > 90:
        tri = "obtusângulo"
    else:
        tri = "acutângulo"

print(f"O triângulo informado é um {tri}!!!!")
'''