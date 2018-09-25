#list(s)
items = []
grocery_list = []
store_lists = []
#Classes
class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

class Store:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.items = []

    def __repr__(self):
        return ("\n**{0}**\n{1}\n{2}".format(self.title, self.description, self.items))


while True:

    print("** WELCOME TO SHOOPING LIST **")
    choice = input("What would you like to do? \n'1'-add list\n'2'-view\n'3'-quit: ").lower()

    if choice =='3':
        break

    if choice == '1':
        store_input = input("Which store is this list for?: ")
        description_input = input("Enter the address of the store: ")

        store1 = Store(store_input, description_input)

        store_lists.append(store1)

        while True:
            choice = input("Add an item (y/n): ").lower()
            if choice == 'n':
                break
            if choice == 'y':
                item_input = input("Add an item: ")

            grocery_item1 = Item(item_input)

            store1.items.append(grocery_item1)
    if choice == '2':
        print(store_lists)
        # print(store1.title)
        # print(store1.description)
        # print(store1.items)
