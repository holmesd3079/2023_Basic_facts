# ALL FUNCTIONS GO HERE

import random


# Decorates texts with the given Character(s) with a top bottom and a few sides
# !!!!!!!!!!!!!!!!!
# !!! | Test! | !!!
# !!!!!!!!!!!!!!!!!
def statement_generator(statement, decoration):
    middle = f'{decoration.upper() * 3} | {statement}! | {decoration.upper() * 3}'
    top_bottom = decoration.upper() * len(middle)

    print(top_bottom)
    print(middle)
    print(top_bottom)


statement_generator("Test", "!")


# int checker also includes minimum and maximum and exit code can be used for infinite mode
def int_check(question, low_num=None, high_num=None, exit_code=None):
    situation = ""
# Checks the higher and lower and if it exists or not, it sets the situation
    if low_num is not None and high_num is not None:
        situation = "both"
    elif low_num is not None and high_num is None:
        situation = "low only"

    while True:

        response = input(question + " ")
        # Returns if exit code is the exit code given
        if response == exit_code:
            return response

        # entire loop to check the int, if it errors it will loop again instead of crashing the entire program
        try:
            # Turns the response to int
            response = int(response)
            # Checks if the boundaries exist
            if situation == "both":
                # If it's past the boundaries given
                if response < low_num or response > high_num:
                    print(f"Please enter a number between {low_num} and {high_num}")
                    continue
            # if it only has a minimum then check if the response is lower than the minimum
            elif situation == "low only":
                if response <= low_num:
                    print(f"Please enter a number that is more than {low_num}")
                    continue

            return response

        except ValueError:
            print("Please enter an integer")


# Shows the instructions when this function is triggered
def instructions():
    print("****How to play****\n")
    print('GUIDE'
          '\n- Pick how many questions you want for a round\n'
          '\n- Advanced options allow'
          '\n Operations: Minus, Times and Divide:'
          '\n Negative questions'
          '\n Custom modes (Range (If you put 10 the range will be -10 to 10 with negative Questions)) minimum is 5'
          '\n- Advanced options off (modes will be 0 to (mode range) ig negatives are not allowed)'
          '\n Easy: Plus and minus with a range of -10 to 10 ()'
          '\n Medium: Plus,minus and times with a range of -20 to 20'
          '\n Hard: Plus, minus, Times & divide with a range of -30 to 30'
          '\n\n')
    return ""


# returns the choice list if they chose the first letter from the list or the whole word however if the list is not
# filled in then it will become a yes no checker to shorten code
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


# Sets the number according to the set settings (if abs_on is true, abs makes negative a positive and positive to...
# ... a positive and returns the number)


def generate_question_int(minimum, maximum):
    number = 0
    while number == 0:  # If any of them generate 0 then regenerate
        number = random.randint(minimum, maximum)
    return number


# Values
valid_list = ["easy", "medium", "hard", "xxx"]
operations = ["+", "-", "x", "÷"]
yes_no = ["yes", "no"]
entire_quiz_stats = []
round_stats = []
picked_operation = None
infinite_mode = False
play_again = True
has_played = False
mode_min_range = 0
mode_max_range = 0

# MAIN LOOP

# Asks if they need instructions
statement_generator("Welcome to the basic facts Quiz!", "*")
want_instructions = choice_checker("would you like to see the instructions? ")
# If yes then run the Instruction function
if want_instructions == "yes":
    instructions()
# The entire Game (Set round settings or quit) stops the Game if play_again is false
questions_answered = 0
# Questions will not be -4 - 5 = -7 if this is set yes it will be 4 - 5 = -1
negative_allowed = choice_checker("do you allow negative Questions? (Answers can be negatives if the question is a "
                                  "minus)")
# Go deeper in settings (with advanced options)
advanced_options = choice_checker("Would you like to go to "
                                  "advanced settings (No for default) ")
# more flexable options
if negative_allowed == "yes":
    only_positive = False
else:
    only_positive = True
# if the part where it asks if you want advanced settings is yes it will go into advanced settings part
if advanced_options == "yes":
    want_divide = choice_checker("Do you want divide in your questions? ")
    want_minus = choice_checker("Do you want minus in your questions? ")
    want_times = choice_checker("Do you want times in your questions? ")

    # Checks if they want to keep certain operations if no then it removes it form the list
    if want_minus == "no":
        list.remove(operations, "-")
    if want_times == "no":
        list.remove(operations, "x")
    if want_divide == "no":
        list.remove(operations, "÷")

    pick_mode = int_check("Pick your custom selection of numbers ", low_num=5)
    mode_min_range = -pick_mode
    mode_max_range = pick_mode
else:
    # asks the mode so it sets the number range
    pick_mode = choice_checker("Choose easy / medium / hard (xxx to quit): ",
                               valid_list, "Please enter easy / medium / hard or 'xxx' to quit ")
    if pick_mode == "hard":
        mode_min_range = -30
    elif pick_mode == "medium":
        mode_min_range = -20
        list.remove(operations, "÷")
    else:
        mode_min_range = -10
        list.remove(operations, "÷")
        list.remove(operations, "x")
    mode_max_range = abs(mode_min_range)
# negative questions no longer will be asked
if negative_allowed == "no":
    mode_min_range = 0

# if asking how many questions is entered empty then infinite mode is turned on
questions = int_check("How many questions do you want?"
                      " <Enter> for infinite ", 0, high_num=None, exit_code="")
# Infinite mode (xxx to quit game)
if questions == "":
    infinite_mode = True
    questions = 10

if pick_mode == "xxx":  # exit code on pick mode if you want to exit out
    exit("Pick mode exit code")

questions_left = questions
print("\n")
statement_generator("QUIZ START", "=")
while questions_left >= 1:  # main game loop
    questions_answered += 1
    print()
    if infinite_mode:  # if its infinite mode it does not take away questions left else 1 goes
        print(f"infinite mode; question: {questions_answered}")
    else:
        print(f"{questions_left} questions left")
        questions_left -= 1

    # generates from the fixed mode numbers
    chosen_number1 = 0
    chosen_number2 = 0
    # Question cant be 0 + 0 or for example 5 + 0 it cant have a 0
    while chosen_number1 == 0 or chosen_number2 == 0:  # If any of them generate 0 then regenerate
        chosen_number1 = generate_question_int(mode_min_range, mode_max_range)
        chosen_number2 = generate_question_int(mode_min_range, mode_max_range)
        picked_operation = random.choice(operations)

    # pre-calculates answer
    if picked_operation == "+":
        answer = chosen_number1 + chosen_number2
    elif picked_operation == "x":
        answer = chosen_number1 * chosen_number2
    elif picked_operation == "-":
        answer = chosen_number1 - chosen_number2
    else:
        # Goes through a loop to make sure that you can answer an integer until it finds one (This is for divide)
        answer = 1.5
        while answer != round(answer, 0):  # Keep regenerating until the answer is an integer
            chosen_number1 = generate_question_int(mode_min_range, mode_max_range)
            chosen_number2 = generate_question_int(mode_min_range, mode_max_range)
            if chosen_number1 < chosen_number2:
                # Re-arranges the numbers, so it the question is with the big number at the front
                # (Example 3 ÷ 5 would be 5 ÷ 3)
                hold_number = chosen_number1
                chosen_number1 = chosen_number2
                chosen_number2 = hold_number
                # answer pre-calculate
                answer = chosen_number1 / chosen_number2

    if picked_operation == "÷":
        generate = f"{chosen_number1} {picked_operation} {chosen_number2}"
        # Show the Question
    else:
        generate = f"{chosen_number1} {picked_operation} {chosen_number2}"  # Show the Question

    # asks what the answer is
    ask_problem = int_check(f"{generate} = ", low_num=None, high_num=None, exit_code="xxx")
    reply = ""
    if ask_problem == answer:  # checks the question and the answer
        # Numbers and the weird text is for colors for example this "Correct!" is Green
        print(f"\033[92mCorrect!\033[00m")
        reply = "Correct"
    elif ask_problem == "xxx":
        break
    else:
        print(f"\033[91mIncorrect\033[00m, the answer was:", answer)
        reply = "Wrong"
    has_played = True
    if reply == "Wrong":
        # Adds this to the list for round history at the end of the game (If wrong)
        list.append(round_stats, f"\033[91m\nQ{questions_answered}: {generate} = {answer}"
                                 f" \nYour answer: {ask_problem} \t\t({reply})\033[00m")
    else:
        # Adds this to the list for round history at the end of the game (If Correct)
        list.append(round_stats, f"\033[92m\nQ{questions_answered}: {generate} = {answer}"
                                 f" \nYour answer: {ask_problem} \t\t({reply})\033[00m")
# If the user exited at the start or on the first question the round history question will not ask the user
if has_played:
    want_stats = choice_checker("Would you like your round history? ")
    if want_stats == "yes":
        statement_generator("QUIZ HISTORY", ":")
        # Prints loop history
        for history in round_stats:
            print(history)
