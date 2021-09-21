# Hero Chan, 1831296

print('\n(Input integers only, please.)')

currentMonth = int(input('What is the current month?\n'))
currentDay = int(input('What is the current day?\n'))
currentYear = int(input('What is the current year?\n'))
birthMonth = int(input('What is your birth month?\n'))
birthDay = int(input('What day of the month were you born?\n'))
birthYear = int(input('What is your birth year?\n'))

print('**BIRTHDAY CALCULATOR**')
print('Current Month: {}'.format(currentMonth))
print('Current Day: {}'.format(currentDay))
print('Current Year: {}\n'.format(currentYear))

print('Birth Month: {}'.format(birthMonth))
print('Birth Day: {}'.format(birthDay))
print('Birth Year: {}\n'.format(birthYear))

if birthMonth == currentMonth and birthDay == currentDay:
    print('\nHAPPY BIRTHDAY ~ !!!')
    print('You are {} years old.'.format(currentYear-birthYear))
elif birthMonth >= currentMonth and birthDay > currentDay:
    print('\nHappy belated birthday!')
    print('You are {} years old.'.format(currentYear - birthYear))
else:
    print('\nYou are {} years old.'.format(currentYear - birthYear - 1))


