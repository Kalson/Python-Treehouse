shopping_list = list()

print("What do you want from the store?")
print("Enter 'DONE' to stop adding items")

run = True
while run:  # run false to stop input
    new_item = input(">> ")
    if new_item == 'DONE':
        print("Here's your list:")
        for item in shopping_list:
            print(item)
            run = False  # run false to stop input
    else:
        shopping_list.append(new_item)
        print("{} was Added! List has {} items".format(new_item, len(shopping_list)))




"""
*while* - A keyword that creates a loop that will continue until its condition is false. Using it like while True makes a loop that will run until it's explicitly stopped.
break - A keyword that stops a loop.
continue - A keyword that makes a loop skip to the next step.
list.append() - A method that adds an item to the end of a list.
for [...] in [...] - Two keywords that create a loop that moves over a collection until the end.
 split() - method on a string breaks the string up into a list. it breaks the string on spaces, tabs, or newlines.
"""
