shopping_list = []


def remove_item(idx):
    index = idx - 1
    item = shopping_list.pop(index)
    print("remove {}".format(item))


def show_help():
    print("\nSeparate each item with a coma.")
    print("Type 'DONE' to quit, 'SHOW' to see the current list, REMOVE to delete an item and 'HELP' to get this message.")


def show_list():
    count = 1
    for new_item in shopping_list:
        print("{}:{}".format(count, new_item))
        count += 1

print("Give me a list of things you want to shop for.")
show_help()

run = True
while run:
    new_item = input("> ")
    if new_item == "DONE":
        print("Here's you're list:")
        run = False
        for new_item in shopping_list:
            print(new_item)
    elif new_item == "SHOW":
        show_list()
    elif new_item == "HELP":
        show_help()
    elif new_item == "REMOVE":
        show_list()
        idx = input("Which item do you want to remove? Which number? ")
        remove_item(int(idx))
    else:
        temporary_list = new_item.split()  # split each item into a list
        index = input("Add this is at a certain spot? Press enter for the end of the list, or give me a number. Currently {} items in the list".format(len(shopping_list)))
        if index:
            spot = (int(index) - 1)  # because of a 0 index List
            for item in temporary_list:  # loops thru each item and inserts into the shopping list
                print('inserting new item:', item)
                shopping_list.insert(spot, item)  # strip any white space from item
                spot += 1
        else:
            for item in temporary_list:  # loops thru each item and inserts into the shopping list
                print('appending new item:', item)
                shopping_list.append(item)
