import random

guess_nums = []
allowed_guesses = 5


def show_help():
    print("Guess a number from 1 to 10. Choose wisely, you only get 5 chances.")


show_help()

run = True
while run and len(guess_nums) < allowed_guesses:
    random_num = random.randint(1, 10)
    new_number = int(input(">> "))
    print("The random number is {}, your number is {}".format(random_num, new_number))
    if new_number > 10:
        print("Wrong guess, it's too high! Guess a number b/w 1 and 10")
    elif len(guess_nums) == 5:
        run = False
        print("Game Over! You have no more chances!")
    elif random_num == new_number and new_number < 10:
        print("Great guess, CONGRATULATIONS! You Won! You guess a number b/w 1 and 10")
        run = False
    else:
        guess_nums.append(new_number)
        print(len(guess_nums))
        print("Wrong guess, but you got {} chances left".format(allowed_guesses - len(guess_nums)))