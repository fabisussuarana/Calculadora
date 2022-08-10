from codecs import oem_decode
from string import octdigits

def calculate():
    operation = input('''\nPlease type in the math operation you would like to complete: 
+ for addition
- for subtraction
* for multiplication
/ for division\n\n Chosen operation: ''')

    number_1 = int(input('\nEnter your first number: '))
    number_2 = int(input('\nEnter your second number: '))

    if operation == '+':
        print(f'\n{number_1} + {number_2} =', number_1 + number_2)

    elif operation == '-':
        print(f'\n{number_1} - {number_2} =', number_1 - number_2)

    elif operation == '*':
        print(f'\n{number_1} * {number_2} =', number_1 * number_2)

    elif operation == '/':
        print(f'\n{number_1} / {number_2} =', number_1 / number_2)
        
    else:
        print('\nYou have not typed a valid operator, please run the program again!')

    # Add again() function to calculate() function
    again()

def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later!')
    else:
        again()

calculate()