print('calculator')

#add
def add(num1,num2):
    return num1+num2

#sub
def sub(num1,num2):
    return num1-num2

#multiply
def multiply(num1,num2):
    return num1*num2

#devide
def devide(num1,num2):
    return num1/num2



operations = {
    "+": add,
    "-": sub,
    "*": multiply,
    "/": devide
}

def calculator():
    num1 = float(input('enter the first number:\n'))

    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        operation_symbol = input('select the operator from the above!')
        num2 = float(input('enter the next number:\n'))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f'{num1}{operation_symbol}{num2} = {answer}')

        repeat = input(f'type "y" to continue with {answer} or type "n" to start new calculator or type "e" to exit')
        if repeat == 'y':
            num1 = answer
        elif repeat == 'n':
            should_continue = False
            calculator()
        else:
            print('thanks for using calculator')
            should_continue = False

calculator()