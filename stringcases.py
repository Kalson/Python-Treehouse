# Create a function named stringcases that takes a string and returns a tuple
# of four versions of the string: uppercased, lowercased, titlecased
# (where every word's first letter is capitalized), and a reversed version of
# the string.
a_string = "Make School"


def stringcases(my_string):
    upper_string = my_string.upper()
    lower_string = my_string.lower()
    title_string = my_string.title()
    reversed_string = my_string[::-1]
    my_tuple = upper_string, lower_string, title_string, reversed_string
    return my_tuple

print(stringcases(a_string))
