name = ""

max_tickets = 150

amount = int(input("How many tickets would you like to purchase?"))
count = amount

while amount > 0:
    print("You have {} seats left.".format(count))

    name = input("Name: ")
    count -= 1
    print()

    if count == 0:
        print("You have brought {} tickets. There are still {} tickets still available.".format(amount, max_tickets - amount))
        break

