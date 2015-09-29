# get two inputs
user_string = input("What's your word? ")
user_num = input("What's your number? ")

# convert the strings into numbers
try:
    our_num = int(user_num)

except:
    our_num = float(user_num)

# use if, so we know the direction of our code once we have a number
if "." not in user_num:
    print(user_string[our_num])
else:
    ratio = round(len(user_string)*our_num)
    print(user_string[ratio])

"""
try - A keyword that marks a block of code to be tried that will watch for exceptions to happen.
len - gets the length of something like a string
except - A keyword that catches exceptions and runs some other code when one happens.
Exception - A catchable/predictable mistake in code, like trying to turn the string 'a' into a number, which would throw a ValueError exception.
not - A keyword that negates whatever follows it.
in - A keyword that checks if something is in something else
round() - A function that rounds a float to the nearest integer(whole number).
Index - The position of something inside of something else. This will be a number and counting starts at zero.
"""
