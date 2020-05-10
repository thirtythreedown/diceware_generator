#! python3

##https://ssd.eff.org/en/module/animated-overview-how-make-super-secure-password-using-dice
##https://www.eff.org/deeplinks/2016/07/new-wordlists-random-passphrases
##https://www.tutorialspoint.com/How-to-create-a-Python-dictionary-from-text-file

import sys, pyperclip
from random import randint

random_numbers_list = []
stored_words = []
i = 0

def number_generator():
    '''Generates a five-digits random numbers using digits between 1 and 6'''
    generated_list = []
    counter = 0
    random_digit = []
    five_digits = []

    while counter < 5:
        random_digit = randint(1,6)
        counter = counter + 1
        five_digits.append(str(random_digit))
    clean_number = ''.join(five_digits)
    return clean_number

def words_lookup(random_numbers_list):
    '''Looks up words in the eff wordlist against generated random numbers'''
    stored_words = []
    i = 0
    d = {}

    with open('eff.txt') as f:
        for line in f:
            (key, val) = line.split()
            d[int(key)] = val
        ##print(d)

    local_random_number_list = random_numbers_list
    ##print(random_numbers_list)
    for number in random_numbers_list:
        ##print(number)
        for key, value in d.items():
            if key == int(number):
                ##print(key, value)
                stored_words.append(value)
    print("The words for your final password are " + str(stored_words) + ".")
    final_password = ''.join(stored_words)
    return(final_password)

while i < 5:
    index = number_generator()
    random_numbers_list.append(index)
    i = i+1

##print(random_numbers_list)
print("Welcome to the Diceware Password Generator 3000!")
print("We got some pseudo-random numbers ready for you.")

final_password = words_lookup(random_numbers_list)
pyperclip.copy(final_password)
print("Your new password has been copied to the clipboard!")
