# Caleb Chan, 1831296
password = input()

password = password.replace('i', '!').replace('a', '@')\
    .replace('m', 'M').replace('B', '8').replace('o', '.')

password = password + 'q*s'

print(password)
