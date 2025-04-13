import random

print('welcome To your password Generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@E$%^&*().,?0123456789'

number = input('Amount of passwords to generate: ')
number = int(number)

lenght = input('Your password lenght: ')
lenght = int(lenght)

print('\nhere are your paswords:')

for pwd in range(number):
  passwords = ''
  for c in range(lenght):
    passwords += random.choice(chars)
  print(passwords)
