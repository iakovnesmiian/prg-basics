pin = '0805'
attempts = 0
pin_ok = False

while attempts < 3:
    entered_pin = input('Enter the PIN code: ')
    attempts += 1
    if entered_pin == pin:
        pin_ok = True
        break
    else:
        print('Incorrect...')

if pin_ok:
    print('PIN correct. Payment accepted.')
else:
    print('Sorry, your payment card has been blocked.')
