import PySimpleGUI as pg

# DO NOT USE IT AS YOUR BUSINESS CALCULATOR UNLESS YOU KNOW HOW TO PROPERLY CONFIGURE IT.

def inserir():
    layout = [
        [pg.Text("Business Calculator")],
        [pg.Text("What's the value? "), pg.InputText(key="valor_escolhido")],
        [pg.Text("How many bottles are you going to sell? "), pg.InputText(key="frascos")],
        [pg.Text("How much is the shipping? "), pg.InputText(key="frete")],
        [pg.Button("Calculate")],
        [pg.Text()],
    ]

    janela = pg.Window("Business Calculator", layout)

    while True:
        evento, valores = janela.read()
        if evento == pg.WIN_CLOSED:
            break
        elif evento == "Calculate":
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
        f"The amount that the consumer will pay is: ${valor_consumidor:.2f}",
        f"The amount you will send to the company is: ${valor_empresa:.2f}",
        f"The final amount you will receive is: ${valor_final:.2f}",
        title="Result"
    )

def main():
    while True:
        valor_final, valor_consumidor, valor_empresa = inserir()
        if valor_final is None:
            break
        resultado(valor_final, valor_consumidor, valor_empresa)

       

if __name__ == "__main__":
    main()