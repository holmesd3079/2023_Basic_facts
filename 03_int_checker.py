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


questions = int_check("How many questions do you want to play with?"
                      " <Enter> for infinite", 0, high_num=None, exit_code="")
infinite_mode = False
questions_answered = 0
if questions == "":
    print("you chose infinite mode")
    questions = 5
    infinite_mode = True
else:
    print(f"you chose regular mode with {questions} questions")

questions_left = questions
while questions_left >= 1:
    questions_answered += 1
    do_something = input("Enter in anything")
    if do_something == "xxx":
        break

    if infinite_mode:
        print(f"you chose infinite mode\nquestion: {questions_answered}")
    else:
        print(f"you chose regular mode with {questions_left} questions")
        questions_left -= 1
