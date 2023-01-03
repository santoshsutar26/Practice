#roller coaster
print('WELCOME TO ROLLER COASTER')
print('minimu height to enjoy the ride is 120 cm')

height = int(input('what is your height ?\n'))
if height>=120:
    print("YAY!! you can ride the roller coaster")
    age = int(input('what is your age ?\n'))
    if age<12:
        bill = 5
        print('children ticket charge is $5')
    elif age<18:
        bill = 7
        print('youth ticket charge is $7')
    elif age>18:
        bill = 12
        print('adult ticket charge is $12')
    photos = input('do you want photos ? yes/no\n')
    if photos=='yess':
        bill +=3
        print(f'your total charge is {bill} ')
    else:
        print(f'your ticket charge is {bill}')
else:
    print('SORRY!!! you cant ride the roller coaster')