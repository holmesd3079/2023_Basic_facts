# Functions go here
yes_no = ["yes", "no"]


# checks users enters either the first letter or
# the full word for a given list, returns full word

def choice_checker(question, chosen_valids, error):
    valid = False
    while not valid:
        response = input(question).lower()

        for item in chosen_valids:
            if response == item[0] or response == item:
                return item

        print(error)


# Main Routine starts here

valid_list = ["easy", "medium", "hard", "xxx"]

while True:
    # ask user for a choice and check is its valid
    user_choice = choice_checker("Choose easy / medium / hard: ",
                                 valid_list, "Please enter easy / medium / hard or 'xxx' to quit")
    print("You chose", user_choice)

    if user_choice == "xxx":
        break
print("we are done")
