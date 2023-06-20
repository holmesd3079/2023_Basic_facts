# ALL FUNCTIONS GO HERE
# V3 - divide now only generates integer answerable questions
import random


def statement_generator(statement, decoration):
    middle = f'{decoration.upper() * 3} | {statement}! | {decoration.upper() * 3}'
    top_bottom = decoration.upper() * len(middle)

    print(top_bottom)
    print(middle)
    print(top_bottom)


# int checker also includes minimum and maximum and exit code can be used for infinite mode
def int_check(question, low_num=None, high_num=None, exit_code=None):
    situation = ""

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
                    print(f"Please enter a number that is more than (or equal to) {low_num}")
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
          '\n Custom modes (Range (If you put 10 the range will be -10 to 10 with negative Questions))'
          '\n- '
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
def fix_number(number, abs_on):
    if abs_on:
        number = abs(number)

    return number


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

advanced_options = choice_checker("Would you like to go to "
                                  "advanced settings (No for default) ")
# more flexable options
if advanced_options == "yes":
    want_divide = choice_checker("Do you want divide in your questions? ")
    negative_allowed = choice_checker("do you allow negative answers? ")
    want_minus = choice_checker("Do you want minus in your questions? ")
    want_times = choice_checker("Do you want times in your questions? ")

    # Checks if they want to keep certain operations
    if want_minus == "no":
        list.remove(operations, "-")
    if want_times == "no":
        list.remove(operations, "x")
    if want_divide == "no":
        list.remove(operations, "÷")

    if negative_allowed == "yes":
        only_positive = False
    else:
        only_positive = True

    pick_mode = int_check("Pick your custom selection of numbers ", low_num=1)
    mode_min_range = fix_number(-pick_mode, only_positive)
    mode_max_range = pick_mode

else:
    # asks the mode so it sets the number range
    pick_mode = choice_checker("Choose easy / medium / hard (xxx to quit): ",
                               valid_list, "Please enter easy / medium / hard or 'xxx' to quit ")
    if pick_mode == "hard":
        mode_min_range = -30
    elif pick_mode == "medium":
        mode_min_range = -20
    else:
        mode_min_range = -10

    mode_max_range = abs(mode_min_range)
# if asking how many questions is entered empty then infinite mode is turned on
questions = int_check("How many questions do you want?"
                      " <Enter> for infinite ", 0, high_num=None, exit_code="")
if questions == "":
    infinite_mode = True
    questions = 10

if pick_mode == "xxx":  # exit code on pick mode
    exit("Pick mode exit code")

questions_left = questions
print("\n\n\n")
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
        #  divide
        answer = 1.5
        while answer != round(answer, 0):  # Keep regenerating until the answer is an integer
            chosen_number1 = generate_question_int(mode_min_range, mode_max_range)
            chosen_number2 = generate_question_int(mode_min_range, mode_max_range)
            if chosen_number1 < chosen_number2:
                hold_number = chosen_number1
                chosen_number1 = chosen_number2
                chosen_number2 = hold_number
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
        print("Correct!")
        reply = "Correct"
    elif ask_problem == "xxx":
        break
    else:
        print("The answer given was wrong, the answer was:", answer)
        reply = "Wrong"
    has_played = True
    list.append(round_stats, f"\nQ{questions_answered}: {generate} = {answer}"
                             f" \nYour answer: {ask_problem} \t\t\t({reply})")

if has_played:
    want_stats = choice_checker("Do you want your statistics for this round? ")
    if want_stats == "yes":
        statement_generator("QUIZ HISTORY", ":")
        for history in round_stats:
            print(history)
