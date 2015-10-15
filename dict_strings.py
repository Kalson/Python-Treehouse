dicts = [
    {'name': 'Michelangelo',
     'food': 'PIZZA'},
    {'name': 'Garfield',
     'food': 'lasanga'},
    {'name': 'Walter',
     'food': 'pancakes'},
    {'name': 'Galactus',
     'food': 'worlds'}
]

string = "Hi, I'm {name} and I love to eat {food}!"


def string_factory(some_list, some_string):
    new_list = []
    count = 0
    for item in dicts:
        new_string = some_string.format(**item)
        new_list.append(new_string)
        count += 1

    return new_list

print(string_factory(dicts, string))
