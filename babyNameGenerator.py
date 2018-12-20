import string, random

# getting the user input to distinguish between vowel, consonant, and letter
letter_input1 = input('Choose a letter "v" for a vowels, "c" for consonants, "l" for any other letters: ')
letter_input2 = input('Choose a letter "v" for a vowels, "c" for consonants, "l" for any other letters: ')
letter_input3 = input('Choose a letter "v" for a vowels, "c" for consonants, "l" for any other letters: ')
letter_input4 = input('Choose a letter "v" for a vowels, "c" for consonants, "l" for any other letters: ')
letter_input5 = input('Choose a letter "v" for a vowels, "c" for consonants, "l" for any other letters: ')

# declaring variables
vowels = 'aeiouy'
consonants = 'bcdfghjklmnpqurstvwxz'
letters = string.ascii_lowercase


# defining our function which tells the machine what to do with the user input
def generator():
    if letter_input1 == 'v':
        letter1 = random.choice(vowels)
    elif letter_input1 == 'c':
        letter1 = random.choice(consonants)
    elif letter_input1 == 'l':
        letter1 = random.choice(letters)
    else:
        # allow user to enter their own letter
        letter1 = letter_input1

    if letter_input2 == 'v':
        letter2 = random.choice(vowels)
    elif letter_input2 == 'c':
        letter2 = random.choice(consonants)
    elif letter_input2 == 'l':
        letter2 = random.choice(letters)
    else:
        # allow user to enter their own letter
        letter2 = letter_input2

    if letter_input3 == 'v':
        letter3 = random.choice(vowels)
    elif letter_input3 == 'c':
        letter3 = random.choice(consonants)
    elif letter_input3 == 'l':
        letter3 = random.choice(letters)
    else:
        # allow user to enter their own letter
        letter3 = letter_input3

    if letter_input4 == 'v':
        letter4 = random.choice(vowels)
    elif letter_input4 == 'c':
        letter4 = random.choice(consonants)
    elif letter_input4 == 'l':
        letter4 = random.choice(letters)
    else:
        # allow user to enter their own letter
        letter4 = letter_input4

    if letter_input5 == 'v':
        letter5 = random.choice(vowels)
    elif letter_input5 == 'c':
        letter5 = random.choice(consonants)
    elif letter_input5 == 'l':
        letter5 = random.choice(letters)
    else:
        # allow user to enter their own letter
        letter5 = letter_input5

    name = letter1 + letter2 + letter3 + letter4 + letter5
    return name


# telling the machine to run the function 10 times
for i in range(10):
    print(generator())

