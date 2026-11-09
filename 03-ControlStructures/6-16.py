time24 = input('Enter time (24-hour format): ')
hours = int(time24[0:2])
minutes = time24[3:5]

if hours == 0:
    print(f'Time in 12-hour format: 12:{minutes}am')
elif hours < 12:
    print(f'Time in 12-hour format: {hours}:{minutes}am')
elif hours == 12:
    print(f'Time in 12-hour format: 12:{minutes}pm')
else:
    print(f'Time in 12-hour format: {hours - 12}:{minutes}pm')
