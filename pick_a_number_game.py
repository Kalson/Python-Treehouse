import random

guess_nums = []
allowed_guesses = 5

run = True
while run and len(guess_nums) < allowed_guesses:
    random_num = random.randint(1, 10)
    new_number = int(input("Guess a number from 1 to 10: "))
    print("The random number is {}, your number is {}".format(random_num, new_number))
    if new_number < 1 or new_number > 10:
        guess_nums.append(new_number)
        print("Wrong guess, that guess isn't between 1 and 10")
        run = False

    if len(guess_nums) == 5:
        run = False
        print("Game Over! You have no more chances!")
    elif random_num == new_number and new_number < 10:
        print("Great guess, CONGRATULATIONS! You Won!")
        print("It took you {} tries!".format(len(guess_nums)))
        run = False
    else:
        guess_nums.append(new_number)
        print("Wrong guess, but you got {} chances left".format(allowed_guesses - len(guess_nums)))
