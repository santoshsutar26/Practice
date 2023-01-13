
import random

from art import main_logo , vs_logo
from game_data import data
import os



def formating(account):
    account_name = account['name']
    account_discrption = account['description']
    account_country = account['country']
    return f'{account_name},a {account_discrption} from {account_country}'

def check_answer(guess,a_follower,b_follower):
    if a_follower > b_follower:
        return guess == 'a' 
    else:
        return guess ==  'b'

score = 0
game_should_continue = True
account_b = random.choice(data)
while game_should_continue:
    

    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f'Compare A: {formating(account_a)}')
    print(vs_logo)
    print(f'Compare B: {formating(account_b)}')

    guess = input('who has more follower? (type A or B): ').lower()

    a_follower = account_a['follower_count']
    b_follower = account_b['follower_count']

    is_correct = check_answer(guess,a_follower,b_follower)
    os.system("cls")
    print(main_logo)
    if is_correct:
        score += 1
        print(f'you got it, your corrent score is {score}')
        
    else:
        print(f'Sorry you got it wrong. your final score is {score}')
        game_should_continue = False





