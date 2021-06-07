import random
# import random module to generate random numbers to use

def mathpractice():
# create a function to house the math game
    i = random.randint(1,10)
    x = random.randint(1,10)
# generate two random integers to play the game
    keepgoing = True
# set  variable for the while loop and to continue playing at the end
    while keepgoing == True:
        try:
            answer = int(input(f'Lets practice some maths! What is {i} + {x}?'))
# f string to input values into the input statement
            if answer == i + x:
                print('Well Done')
                q = input('Play again?: yes / no')
# ask if they'd like to play again
                if q.lower() == 'yes':
                    break
# if yes break to return back to the start of while loop
                else:
                    keepgoing = False
# if any other answer then it will break the loop and end the game
            else:
                print('Try again')
        except:
            print('invalid entry try again')
# try except to catch incorrect inputs into the number answer