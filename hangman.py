import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

names = ['santosh', 'sagar','ram','jayesh','tushar']
choice = random.choice(names)
print(f'it is {choice}')

display = []
for i in choice:
    display += '_'
print(display)

end_of_game = False
lives = 6

while not end_of_game:
    guess = input('guess a letter:\n').lower()

    for i in range(len(choice)):
        letter = choice[i]
        if letter == guess:
            display[i] = letter
    print(display)


    if guess not in choice:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print('you loose')


    if '_' not in display:
        print('you win!!!')
        end_of_game = True



