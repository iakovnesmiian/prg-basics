facebook = True
twitter = False
instagram = True

accounts = 0
if facebook:
    accounts += 1
if twitter:
    accounts += 1
if instagram:
    accounts += 1

print(f'facebook = {facebook}')
print(f'twitter = {twitter}')
print(f'instagram = {instagram}')
if accounts >= 2:
    print('You are a good influencer!')
else:
    print('You are not a good influencer.')
