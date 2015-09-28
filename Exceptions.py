# get two inputs
user_string = input("What's your word?")
user_num = input("What's your number?")

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
