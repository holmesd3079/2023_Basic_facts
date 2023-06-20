yes_no = ["yes", "no"]
valid_list = ["easy", "medium", "hard", "xxx"]


def choice_checker(question, chosen_valids=None, error=None):
    valid = False
    if chosen_valids is None:
        chosen_valids = yes_no
        error = "Pick yes or no"

    while not valid:
        response = input(question).lower()

        for item in chosen_valids:
            if response == item[0] or response == item:
                return item

        print(error)


while True:
    # ask user for a choice and check is its valid
    user_choice = choice_checker("Choose easy / medium / hard: ",
                                 valid_list, "Please enter easy / medium / hard or 'xxx' to quit")
    print("You chose", user_choice)

    if user_choice == "xxx":
        break
print("we are done")

want_stats = choice_checker("Would you like to see the stats?")
if want_stats == "yes":
    print("Stats go here")
else:
    print("you chose no")
