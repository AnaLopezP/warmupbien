
def bitcoinToEuros (bitcoin_amountn, bitcoin_value_euros):
    euros_value = bitcoin_amountn * bitcoin_value_euros
    return euros_value
bitcoins = 30
valor_bitcoin = 1000
invest = bitcoinToEuros (bitcoins, valor_bitcoin)
if invest < 30000:
    print("El precio del bitcoin está bajando")
else:
    print("El precio del bitcoin está subiendo")