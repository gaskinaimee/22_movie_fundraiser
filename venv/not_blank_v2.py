
def not_blank(question, error_message, enter_input):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print(error_message, enter_input)

name = not_blank("Name: ", "Sorry, this can't be blank,", "please enter your name.")


