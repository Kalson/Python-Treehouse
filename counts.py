# Write a function named members that takes two arguments, a dictionary and
# a list of keys. Return a count of how many of the items in the list are
# also keys in the dictionary.

my_dict = {'apples': 1, 'bananas': 2, 'coconuts': 3}
my_list = ['apples', 'coconuts', 'grapes', 'strawberries']


def members(some_dict, some_list):
    count = 0
    for list_index in some_list:
        print(some_dict.keys())
        if list_index in some_dict.keys():
            print(some_dict.keys())
            count += 1
        else:
            count += 0
    # compare first value in list with keys in dictionary
    # if it's the same, then give it a count (+= 1)
    # otherwise, don't give it a count (+= 0 or skip)
    # count = 1 + 1 + 0 + 0
    return count

print(members(my_dict, my_list))
