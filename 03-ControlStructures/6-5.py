hours = int(input('Enter number of parking hours: '))

if hours <= 2:
    fee = 5
elif hours <= 6:
    fee = 15
else:
    fee = 20

print(f'Parking fee: {fee} PLN')
