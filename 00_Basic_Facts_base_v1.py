# ALL FUNCTIONS GO HERE
import math
import random


# Checks if the question is yes or no then returns the valid answer
# int checker also includes minimum and maximum and exit code can be used for infinite mode
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


# Checks if the given Question is y/n Yes/No and returns yes or no
def yes_no(question):
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes or no")


# Shows the instructions when this function is triggered
def instructions():
    print("****How to play****\n")
    print('Rules go here\n')
    return ""


# returns the choice list if they chose the first letter from the list or the whole word
def choice_checker(question, chosen_valids, error):
    valid = False
    while not valid:
        response = input(question).lower()

        for item in chosen_valids:
            if response == item[0] or response == item:
                return item

        print(error)


# Sets the number according to the set settings (if abs_on is true, abs makes negative a positive and positive to...
# ... a positive and returns the number)
def fix_number(number, abs_on):
    if abs_on:
        number = abs(number)

    return number


# Values
valid_list = ["easy", "medium", "hard", "xxx"]
infinite_mode = False
mode_min_range = 0
mode_max_range = 0
play_again = True

# MAIN LOOP

# Asks if they need instructions
want_instructions = yes_no("Hello welcome to the Basic facts quiz would you like to see the instructions")
# If yes then run the Instruction function
if want_instructions == "yes":
    instructions()
# The entire Game (Set round settings or quit) stops the Game if play_again is false
while play_again:
    only_positive = False
    # how many questions do they want
    questions = int_check("How many questions do you want?"
                          " <Enter> for infinite", 0, high_num=None, exit_code="")
    # asks for advanced options
    advanced_options = yes_no("Would you like to go to advanced settings (No for default)")
    # more flexable options
    if advanced_options == "yes":
        negative_allowed = yes_no("do you allow negative answers?")
        if negative_allowed == "yes":
            only_positive = False
        else:
            only_positive = True
        pick_mode = int_check("Pick your custom selection of numbers", low_num=0)
        mode_min_range = fix_number(-mode_min_range, only_positive)
        mode_max_range = pick_mode

    else:
        # asks the mode so it sets the number range
        pick_mode = choice_checker("Choose easy / medium / hard (xxx to quit): ",
                                   valid_list, "Please enter easy / medium / hard or 'xxx' to quit")
        if pick_mode == "hard":
            mode_min_range = -30
        elif pick_mode == "medium":
            mode_min_range = -20
        else:
            mode_min_range = -10
        mode_max_range = abs(mode_min_range)
# if asking how many questions is entered empty then infinite mode is turned on
    if questions == "":
        questions = 10
        infinite_mode = True
    questions_left = questions

    if pick_mode == "xxx":  # exit code on pick mode
        break
    questions_answered = 0

    print("\n\n\n")
    while questions_left >= 1:  # main game loop
        questions_answered += 1

        if infinite_mode:  # if its infinite mode it does not take away questions left else 1 goes
            print(f"infinite mode; question: {questions_answered}")
        else:
            print(f"you chose regular mode with {questions_left} questions")
            questions_left -= 1

        # generates from the fixed mode numbers
        chosen_number1 = random.randint(mode_min_range, mode_max_range)
        chosen_number2 = random.randint(mode_min_range, mode_max_range)
        generate = f"{chosen_number1} + {chosen_number2}"  # Show the Question
        # pre-calculates answer
        answer = chosen_number1 + chosen_number2
        # asks what the answer is
        ask_problem = int_check(f"{generate} = ", low_num=None, high_num=None, exit_code="xxx")
        if ask_problem == answer:  # checks the question and the answer
            print("Correct")
        elif ask_problem == "xxx":
            break
        else:
            print("Wrong")

    play_again = yes_no("Would you like to play again?")  # asks if they want to play again
    if play_again == "yes":
        play_again = True
    else:
        play_again = False
