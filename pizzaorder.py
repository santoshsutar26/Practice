#pizzaorder
print('WELCOME TO PIZZA STATION!!')
print('Small pizza = $15\nMediun pizza = $20\nLarge pizza = $25')
print('pepperoni for Small pizza: +$2\npepperoni for Medium or Large pizza: +$3')
print('extra cheese for any size pizza: +$1')
bill = 0
size=input('what size pizza you want to have ?(S , M or L)\n')
if size=='S':
    bill+=15
elif size=='M':
    bill+=20
elif size=='L':
    bill+=25

pepperoni=input('do you want to add pepporoni ?(yes/no)\n')
if pepperoni=='yes':
    if size=='S':
        bill+=2
    elif size=='M':
        bill+=3
    elif size=='L':
        bill+=3

cheese=input('do want extra pizza ?(yes/no)\n')
if cheese=='yes':
    bill+=1
print(f'your total bill is ${bill}')
