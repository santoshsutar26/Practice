import random

rock = ''' ✊'''
paper = '''✋'''
sessor = '''✋'''

choice = int(input('what do you choice ?\n(type "1" for ROCK, "2" for paper and "3" for sessor)\n'))
if choice==1:
    print(rock)
elif choice==2:
    print(paper)
elif choice==3:
    print(sessor)

print('Computer choice : ')
computer_choice=[rock,paper,sessor]
cc=random.choice(computer_choice)
print(cc)
if choice==1 and cc==1:
    print("you win!!!!!")
elif choice==1 and cc==0:
    print('it\'s a draw!! try again')
elif choice==2 and cc==2:
    print('you win!!!!')
elif choice==2 and cc==1:
    print('its a draw!! try again')
elif choice==3 and cc==0:
    print('you win!!!!')
elif choice==3 and cc==2:
    print('its a draw!! try again')
else:
    print('you losse!!')

