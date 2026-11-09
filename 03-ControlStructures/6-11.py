products = int(input('Number of products purchased: '))
price = float(input('Product price: '))

if products <= 2:
    amount = products * price
else:
    amount = 2 * price + (products - 2) * price * 0.75

print(f'Amount to pay: {amount:.2f}')
