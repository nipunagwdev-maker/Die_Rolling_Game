import random

while True:

    user_input = input("Roll the dice(y/n) : ").lower() #Make the input to lowercase

    if user_input == 'y':

        a = random.randint(1,6)
        b = random.randint(1,6)
        # print(a,b)    # noraml Print

        print(f'( {a} , {b} )')     #print in a given format

    elif user_input == 'n':
        print("Thanks for playing")
        break

    else:
        print("Invalid Input, Try again")


