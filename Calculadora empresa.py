def inserir():
    valor_escolhido = float(input("Qual o valor escolhido para vender? "))
    frascos = float(input("Quantos frascos irá vender? "))
    frete = float(input("Qual o valor do frete? "))

    valor_parcial = valor_escolhido * frascos
    valor_consumidor = valor_parcial + (frete + 4)
    valor_empresa = frascos * 175 + (frete + 4)
    # "175" é o valor que cada frasco é comprado. "+4" é o valor de empacotamento do produto adicionado ao frete
    valor_final = valor_consumidor - (frascos * 175) - (frete + 4)

    return valor_final, valor_consumidor, valor_empresa

def resultado(valor_final, valor_consumidor, valor_empresa):
    print("--------------------------------------------")
    print(f"O valor que o consumidor irá pagar é: R${valor_consumidor:.2f}")
    print("--------------------------------------------")
    print(f"O valor que você mandará para a empresa é: R${valor_empresa:.2f}")
    print("--------------------------------------------")
    print(f"O valor final que você receberá é: R${valor_final:.2f}")
    print("--------------------------------------------")

def main():
    while True:
        valor_final, valor_empresa, valor_consumidor = inserir()
        resultado(valor_final, valor_empresa, valor_consumidor)

        opcao = input("Deseja refazer (R) ou deseja sair (S)? ").strip().upper()
        if opcao != 'R':
            break
    
main()