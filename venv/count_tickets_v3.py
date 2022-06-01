name_list= []
max_tickets = 150

amount = int(input("How many tickets would you like to purchase?"))
count = amount

while amount > 0:
    print("You have {} seats left.".format(count))

    name = input("Name: ")
    name_list.append(name)
    count -= 1
    print()

    if count == 0:
        print("You have brought {} tickets. There are still {} tickets available.".format(amount, max_tickets - amount))
        print("These are the names you used:")
        print(name_list)
        remove_or_add = input("Would you like to add or remove any names? 'R' means remove, 'A' means add.".lower())
        if remove_or_add == "a":
            add_name = input("Enter a name:")
            name_list.append(add_name)
            print(name_list)
            amount += 1
            print("You have brought {} tickets.".format(amount))
        elif remove_or_add == "r":
            remove_name = input("Enter a name to remove: ".lower())
            name_list.remove(remove_name)
            print(name_list)
            amount -= 1
            print("You have brought {} tickets.".format(amount))

        break


