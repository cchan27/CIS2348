# Hero Chan, 1831296

lemon = float(input('Enter amount of lemon juice (in cups):\n'))
water = float(input('Enter amount of water (in cups):\n'))
agave = float(input('Enter amount of agave nectar (in cups):\n'))
serv = float(input('How many servings does this make?\n'))

print('\nLemonade ingredients - yields {:.2f} servings'.format(serv))
print('{:.2f} cup(s) lemon juice'.format(lemon))
print('{:.2f} cup(s) water'.format(water))
print('{:.2f} cup(s) agave nectar'.format(agave))

desired_serv = float(input('\nHow many servings would you like to make?\n'))

print('\nLemonade ingredients - yields {:.2f} servings'.format(desired_serv))
print('{:.2f} cup(s) lemon juice'.format(lemon*desired_serv/serv))
print('{:.2f} cup(s) water'.format(water*desired_serv/serv))
print('{:.2f} cup(s) agave nectar'.format(agave*desired_serv/serv))
# gallon conversion
print('\nLemonade ingredients - yields {:.2f} servings'.format(desired_serv))
print('{:.2f} gallon(s) lemon juice'.format(lemon*desired_serv/serv/16))
print('{:.2f} gallon(s) water'.format(water*desired_serv/serv/16))
print('{:.2f} gallon(s) agave nectar'.format(agave*desired_serv/serv/16))
