shopping_list = []


def show_help():
    print("What do you want from the store?")
    print("Enter 'DONE' to stop. Enter 'HELP' for help. Enter 'SHOW' to see your current list'")


def show_list():
    print("Here's your list")
    for item in shopping_list:
        print(item)


def add_to_list(item):
    shopping_list.append(item)
    print("{} was added! List has {} item(s)".format(new_item, len(shopping_list)))

show_help()
run = True

while run:  # run True to start input
    new_item = input(">> ")
    if new_item == "DONE":
        show_list()
        run = False  # run false to stop input
    elif new_item == "HELP":
        show_help()
    elif new_item == "SHOW":
        show_list()
    else:
        add_to_list(new_item)
