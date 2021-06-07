while True:

    input_value = input('Please enter a whole number value:')

    try:
        int(input_value)
    except ValueError:
        print("Try again you must enter a whole number")
    else:
        converted_input_value = int(input_value)

        if (converted_input_value % 2 == 0) and (converted_input_value > 5):
            print(f'Entered value: {converted_input_value} is divisible by 2 and greater than 5')
        elif (converted_input_value % 2 == 0) or (converted_input_value > 5):
            print('Entered value: ' + str(converted_input_value) + ' is either divisible by 2 or greater than 5')
        else:
            print('Entered value is neither divisbile by 2 or greater than 5')
        break


concatstate ='''
def concatfunc(int):
    return 'The number is ' + str(int)
'''


fstringstate =
'''
def fstringfunc(int):
    f'The number is {int}'
    '''

t.timeit('a + str(b)', setup='a, b = "This number is", 10', number=10000)
t.timeit('f"{a}{b}"', setup='a, b = "This number is", 10', number=10000)


from random import randint as r


loop = 1

while loop == 1:
    number_one = r(0, 9)
    number_two = r(0, 9)

    sum_result = number_one + number_two
    sum_answer = int(input(f"What is {number_one} + {number_two}? :"))

    if sum_answer == number_one + number_two:
        loop = int(input("Well done. Type 1 to do another one or 0 to stop: "))
    else:
        loop = int(input("Sorry. Type 1 to try again or 0 to stop: "))