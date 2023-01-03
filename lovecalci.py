#love calculator
print('WELCOME!! find out your love percentage')

name1 = input('enter your name:\n')
name2 = input('eneter your partner name:\n')

a=name1.lower()
b=name2.lower()

both_name=name1+name2
t=(both_name.count('t'))
r=(both_name.count('r'))
u=(both_name.count('u'))
e=(both_name.count('e'))

l=(both_name.count('l'))
o=(both_name.count('o'))
v=(both_name.count('v'))
y=(both_name.count('e'))

true = t+r+u+e
love = l+o+v+y
calc = int(str(true)+str(love))

if calc<=10 or calc>=90:
    print(f'your score is {calc}%, you go together like coke and mentos !!')
elif calc>=40 and calc<=50:
    print(f'your score is {calc}%, you are alright together !')
else:
    print(f'your score is {calc}%')