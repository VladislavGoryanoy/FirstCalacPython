def welcome():
    print('''
    Welcome to Calculator:
    ''')

def calculate():

    operation = input('''
    Please type in the math operation you would like to complete:
    + for addition
    - for subtraction
    * for multiplication
    / for division
    ''' "> ")

    number_1 = float(input('Enter your first number: '))
    number_2 = float(input('Enter your second number: '))

    # Addition
    if operation == '+':
            print(number_1 + number_2)

    # Subtraction
    elif operation == '-':
            print(number_1 - number_2)


    # Multiplication
    elif operation == '*':
            print(number_1 * number_2)

    # Division
    elif operation == '/':
        try:
            number_1 / 0
        except ZeroDivisionError:
             print("You cannot divide by zero!")
        print(number_1 * number_2)

           
    else:
            print('You have not typed a valid operator, please run the program again.')

    again()
def again():
    calc_again = input('''
    Do you want to calculate again?
    Please type Y for YES or N for NO.
    ''')
# Accept 'y' or 'Y' by adding str.upper()
    if calc_again.upper() == 'Y':
        calculate()
# Accept 'n' or 'N' by adding str.upper()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()
welcome()
calculate()

