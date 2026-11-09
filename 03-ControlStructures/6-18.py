print('SURVEY')
computer_science = input('Are you interested in computer science? (y/n): ') == 'y'
games = input('Do you like playing computer games? (y/n): ') == 'y'
instagram = input('Do you have an Instagram account? (y/n): ') == 'y'

print()
print('SURVEY RESULTS')
if computer_science:
    print('Interested in computer science: Yes')
else:
    print('Interested in computer science: No')
if games:
    print('Playing computer games: Yes')
else:
    print('Playing computer games: No')
if instagram:
    print('Has an Instagram account: Yes')
else:
    print('Has an Instagram account: No')
