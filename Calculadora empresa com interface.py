import PySimpleGUI as pg

# NÃO USE ISSO COMO CALCULADORA, A NÃO SER QUE SAIBA COMO CONFIGURAR APROPRIADAMENTE.

def inserir():
    layout = [
        [pg.Text("Calculadora")],
        [pg.Text("Qual o valor escolhido para vender? "), pg.InputText(key="valor_escolhido")],
        [pg.Text("Quantos frascos irá vender? "), pg.InputText(key="frascos")],
        [pg.Text("Qual é o valor do frete? "), pg.InputText(key="frete")],
        [pg.Button("Calcular")],
        [pg.Text()],
    ]

    janela = pg.Window("Calculadora", layout)

    while True:
        evento, valores = janela.read()
        if evento == pg.WIN_CLOSED:
            break
        elif evento == "Calcular":
            valor_escolhido = float(valores["valor_escolhido"])
            frascos = float(valores["frascos"])
            frete = float(valores["frete"])

            valor_parcial = valor_escolhido * frascos
            valor_consumidor = valor_parcial + (frete + 4)
            valor_empresa = frascos * 175 + (frete + 4)
            valor_final = valor_consumidor - (frascos * 175) - (frete + 4)

            janela.close()
            return valor_final, valor_consumidor, valor_empresa
    
def resultado(valor_final, valor_consumidor, valor_empresa):
    pg.popup(
        f"O valor que o consumidor irá pagar é: R${valor_consumidor:.2f}",
        f"O valor que você mandará para a empresa é: R${valor_empresa:.2f}",
        f"O valor final que você receberá é: R${valor_final:.2f}",
        title="Resultado"
    )

def main():
    while True:
        valor_final, valor_consumidor, valor_empresa = inserir()
        if valor_final is None:
            break
        resultado(valor_final, valor_consumidor, valor_empresa)

       

if __name__ == "__main__":
    main()