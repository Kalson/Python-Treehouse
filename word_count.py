new_string = "I am that I am"


def word_count(some_string):
    string_dict = {}
    string_list = new_string.lower().split()
    for word in string_list:
        if word in string_dict.keys():
            string_dict[word] += 1
        else:
            string_dict[word] = 1
    return string_dict

print(word_count(new_string))
