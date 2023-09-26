amount_of_trousers = int(input('trousers: '))
amount_of_tshirts = int(input('T-shirt: '))
amount_of_waistcoat = int(input('waistcoat: '))

print(f'*** Welcome to the checkout system.\nHow many trousers have been bought? {amount_of_trousers}\nHow many T-shirts have been bought? {amount_of_tshirts}\nHow many vests have been bought? {amount_of_waistcoat}\nTotal amount to pay: {amount_of_trousers * 70.5 + amount_of_tshirts * 20.89 + amount_of_waistcoat * 100.3}')