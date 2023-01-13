from random import randint

print('WELCOME TO GUESS THE NUMBER GAME')

answer = randint(1,100)



mode = input('Type the mode of game.("easy","medium","hard")\n')


def easy():
    print('You have 10 attempts to guess the number: \n')
    global answer

    a = 1
    while (a<=10):
        user = int(input(f'guess the number between 1-100 (attempt {a}):\n'))
        if user == answer:
            print('correct guess.You win!!')
            break
        elif user < answer:
            print('too low guess!!')
        else:
            print('too high guess!!')
        a+=1
    if a==11:
        print(f'your 10 attempts are over.Correct guess was {answer}. You loose!!!')

def medium():
    print('You have 5 attempts to guess the number: \n')
    global answer

    a = 1
    while (a<=5):
        user = int(input(f'guess the number between 1-100 (attempt {a}):\n'))
        if user == answer:
            print('correct guess.You win!!')
            break
        elif user < answer:
            print('too low guess!!')
        else:
            print('too high guess!!')
        a+=1
    if a==6:
        print(f'your 6 attempts are over.Correct guess was {answer}. You loose!!!')

def hard():
    print('You have 3 attempts to guess the number: \n')
    global answer

    a = 1
    while (a<=3):
        user = int(input(f'guess the number between 1-100 (attempt {a}):\n'))
        if user == answer:
            print('correct guess.You win!!')
            break
        elif user < answer:
            print('too low guess!!')
        else:
            print('too high guess!!')
        a+=1
    if a==4:
        print(f'your 3 attempts are over.Correct guess was {answer}. You loose!!!')
if mode == 'easy':
    easy()
elif mode == 'medium':
    medium()
elif mode == 'hard':
    hard()
else:
    print('please enter correct mode')






