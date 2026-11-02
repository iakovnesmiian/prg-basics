phone = input('Enter phone number: ')
formatted = phone[0:3] + '-' + phone[3:6] + '-' + phone[6:9]
print(f'Phone number: {formatted}')