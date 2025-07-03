print('Bem-vindo a Copiadora do Matheus Henrique!!')
print('Escolha um serviço!!')

# Função que pergunta e retorna o serviço escolhido com o preço por página
def escolha_servico():
    while True:
        print("\nTipos de serviço disponíveis:")
        print("DIG - Digitalização (R$1.10/página)")
        print("ICO - Impressão Colorida (R$1.00/página)")
        print("IPB - Impressão Preto e Branco (R$0.40/página)")
        print("FOT - Fotocópia (R$0.20/página)")
        servico = input("Digite o código do serviço desejado (dig/ico/ipb/fot): ").strip().lower()

        if servico == "dig":
            return 1.10
        elif servico == "ico":
            return 1.00
        elif servico == "ipb":
            return 0.40
        elif servico == "fot":
            return 0.20
        else:
            print("Escolha inválida, entre com o tipo do serviço novamente.\n")

# Função que pergunta e retorna o número de páginas com desconto aplicado
def num_pagina():
    while True:
        try:
            paginas = int(input("Entre com o número de páginas: "))
            if paginas >= 20000:
                print("Não aceitamos tantas páginas de uma vez..\n")
            elif paginas >= 2000:
                return paginas * 0.75  # 25% de desconto
            elif paginas >= 200:
                return paginas * 0.80  # 20% de desconto
            elif paginas >= 20:
                return paginas * 0.85  # 15% de desconto
            elif paginas > 0:
                return paginas  # sem desconto
            else:
                print("Por favor, digite um número positivo de páginas.\n")
        except ValueError:
            print("Digite um número válido!\n")

# Função que pergunta e retorna o valor do serviço adicional
def servico_extra():
    while True:
        print("\nDeseja adicionar algum serviço?: ")
        print("0 - Sem adicional (R$0)")
        print("1 - Encadernação simples (R$15)")
        print("2 - Encadernação capa dura (R$40)")
        extra = input("Digite a opção desejada (0/1/2): ").strip()

        if extra == "0":
            return 0
        elif extra == "1":
            return 15
        elif extra == "2":
            return 40
        else:
            print("Opção inválida! Digite 0, 1 ou 2.\n")

# Parte principal do programa (fora das funções)
try:
    preco_servico = escolha_servico()
    paginas_com_desconto = num_pagina()
    valor_extra = servico_extra()

    # Cálculo final
    total = (preco_servico * paginas_com_desconto) + valor_extra

    # Exibição do valor total
    print(f'Total: R$ {total:.2f} (serviço: {preco_servico:.2f} * páginas: {paginas_com_desconto:.2f} + extra: {valor_extra:.2f}')


except Exception as e:
    print("Ocorreu um erro inesperado:", e)


