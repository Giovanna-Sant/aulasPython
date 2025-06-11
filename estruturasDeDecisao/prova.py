# RM566301 - Giovanna da Silva Santos

print("Olá, seja bem vindo(a) à Vinheria Agnello!")
end = input("Para começar as compras, insira seu endereço \n->")
ano = int(input("Agora, digite o ano de seu nascimento\n->"))

if 2025 - ano <= 18:
    print("A venda e consumo de bebidas alcoolicas para menores de 18 é proibida. Encerrando programa...")
else:
    print("Catálogo de vinhos:\n1. Vinho Seco de Ameixa - R$49,90 \n2. Vinho Branco do Himalaia - R$65,00\n3. Vinho Zeca Baleiro - R$39,90")
    vinho = int(input("Digite o número correspondente ao vinho que deseja comprar:\n->"))
    if vinho != 1 and vinho != 2 and vinho != 3:
        print("O valor digitado é inválido, tente novamente.")
    else:
        quant = int(input("Agora, digite a quantidade de garrafas desejadas:\n->"))

        if vinho == 1:
            preco = 49.90
            nome = "Vinho Seco de Ameixa"
        elif vinho == 2:
            preco = 65
            nome = "Vinho Branco do Himalaia"
        else:
            preco = 39.90
            nome = "Vinho Zeca Baleiro"

        valor = quant * preco
        if valor > 100:
            print(f"* Você ganhou frete grátis! *\nObrigado por comprar na Vinheria Agnello!\n---------------------------- \n {quant} unidade(s) do {nome} \n Valor final: {valor:.2f}\n----------------------- \n O pedido será enviado para o endereço {end}.")
        else:
            valor_frete = preco + 30
            print(f"\nObrigado por comprar na Vinheria Agnello!\n---------------------------- \n {quant} unidade(s) do {nome} \n Valor dos produtos: R${valor:.2f}\n Frete: R$30,00 \n Valor final: R${valor_frete:.2f}\n----------------------- \nO pedido será enviado para o endereço {end}.")