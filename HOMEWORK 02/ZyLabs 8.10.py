# Caleb Chan, 1831296
usr_text = input()
word_a = ''
word_b = ''

for i in usr_text:
    if i != "":
        word_a = word_a + i.replace(' ', '')
        word_b = i.replace(' ', '') + word_b
print(word_a)
print(word_b)

if word_a == word_b:
    print('{} is a palindrome'.format(usr_text))

else:
    print('{} is not a palindrome'.format(usr_text))
