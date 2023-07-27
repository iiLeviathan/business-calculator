def inserir():
    valor_escolhido = float(input("What's the value? "))
    frascos = float(input("How many bottles are you going to sell? "))
    frete = float(input("How much is the shipping? "))

    valor_parcial = valor_escolhido * frascos
    valor_consumidor = valor_parcial + (frete + 4)
    valor_empresa = frascos * 175 + (frete + 4)
 # "+4" is the added value because of the shipping package. "175" is the amount that the bottle is purchased.
    valor_final = valor_consumidor - (frascos * 175) - (frete + 4)

    return valor_final, valor_consumidor, valor_empresa

def resultado(valor_final, valor_consumidor, valor_empresa):
    print("--------------------------------------------")
    print(f"The amount that the consumer will pay is: ${valor_consumidor:.2f}")
    print("--------------------------------------------")
    print(f"The amount you will send to the company is: ${valor_empresa:.2f}")
    print("--------------------------------------------")
    print(f"The final amount you will receive is: ${valor_final:.2f}")
    print("--------------------------------------------")

def main():
    while True:
        valor_final, valor_empresa, valor_consumidor = inserir()
        resultado(valor_final, valor_empresa, valor_consumidor)

        opcao = input("Do you want to redo (R) or do you want to quit (Q)? ").strip().upper()
        if opcao != 'R':
            break
    
main()