import random
letters = ['A','B','C''D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9']
symbol = ['!','@','#','$','%','^',"&",'*','(',')','+']
characters = int(input('how many characters you want in password:\n'))
num = int(input('how many numbers you want in password:\n'))
symb = int(input('how many symbol you want in password:\n'))
password = []
for char in range(0,characters):
    password += random.choice(letters)


for num in range(0,num):
    password += random.choice(numbers)


for sym in range(0, symb):
    password += random.choice(symbol)


random.shuffle(password)

uniquepass = ''
for i in password:
    uniquepass+=i

print(f'ypur unique password is:\n {uniquepass}')
