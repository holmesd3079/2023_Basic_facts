import random


def int_check(question, low_num=None, high_num=None, exit_code=None):
    situation = ""

    if low_num is not None and high_num is not None:
        situation = "both"
    elif low_num is not None and high_num is None:
        situation = "low only"

    while True:

        response = input(question)
        if response == exit_code:
            return response

        try:
            response = int(response)

            if situation == "both":

                if response < low_num or response > high_num:
                    print(f"Please enter a number between {low_num} and {high_num}")

                    continue

            elif situation == "low only":
                if response <= low_num:
                    print(f"Please enter a number that is more than (or equal to) {low_num}")
                    continue

            return response

        except ValueError:

            print("Please enter an integer")


def yes_no(question):
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes or no")


# Sets the number according to the set settings
def fix_number(number, abs_on):
    if abs_on:
        number = abs(number)

    return number


mode_min_range = 0
mode_max_range = 0
infinite_mode = False
only_positive = False
questions = 5  # int_check("How many questions do you want to play with? "
#                          " <Enter> for infinite ", 0, high_num=None, exit_code="")
advanced_options = yes_no("Would you like to go to advanced settings (No for default) ")
if questions == "":
    infinite_mode = True
    questions = 5
if advanced_options == "yes":
    negative_allowed = yes_no("do you allow negative answers?")
    if negative_allowed == "yes":
        only_positive = False
    else:
        only_positive = True
    pick_mode = int_check("Pick your custom selection of numbers", low_num=0)
if only_positive:
    mode_min_range = 0
else:
    mode_min_range = fix_number(-15, only_positive)
mode_max_range = fix_number(15, only_positive)

questions_left = questions
questions_answered = 0
while questions_left >= 1:
    if infinite_mode:
        print(f"Infinite mode; Questions answered: {questions_answered}")
        questions_left += 1
    else:
        print(f"Questions left: {questions_left}")
    chosen_number1 = random.randint(mode_min_range, mode_max_range)
    chosen_number2 = random.randint(mode_min_range, mode_max_range)
    generate = f"{chosen_number1} + {chosen_number2}"
    answer = chosen_number1 + chosen_number2
    ask_problem = int_check(f"{generate} = ", low_num=None, high_num=None, exit_code="xxx")
    if ask_problem == answer:
        print("Correct")
    elif ask_problem == "xxx":
        exit()
    else:
        print("Answer given was wrong, correct answer was", answer)
    questions_left -= 1
    questions_answered += 1
