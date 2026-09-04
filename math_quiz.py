import random
import time
from inputimeout import inputimeout, TimeoutOccurred


OPERATORS = ["+", "-", "*"] # I am keeping this final boss for now: "/"
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expration = str(left) + " " + operator + " " + str(right)
    answer = eval(expration) # very important it generates answers
    return expration, answer


def main():
    wrong = 0
    correct = 0

    input("Press Enter to start the game!")
    print("-----------------------------------")

    # timer starts
    start_time = time.time()

    for i in range(TOTAL_PROBLEMS):
        expr, answer = generate_problem()
        while True:
            try:
                guess = inputimeout(prompt = "Problem #" + str(i + 1) + ": " + expr + " = ", timeout = 10)
            except TimeoutOccurred:
                print("You took more then 5 second to answer. Better Luck next time")
                quit()


            if guess == str(answer):
                correct += 1
                break
            print("Wrong! Try again.")

        


    #timer ends
    end_time = time.time()

    total_time = end_time - start_time

    print("-----------------------------------")
    print("Nice Work! You finished in", round(total_time, 2), "seconds!")


if __name__ == "__main__":
    main()


# README.md
# =========
#
# # Timed Math Quiz
#
# A command-line math quiz that gives you ten randomly generated addition,
# subtraction, or multiplication problems. Each problem has a ten-second
# time limit.
#
# ## Requirements
#
# - Python 3
# - `inputimeout`
#
# Install the dependency with:
#
# ```bash
# pip install inputimeout
# ```
#
# ## Running the Quiz
#
# Run the script from a terminal:
#
# ```bash
# python math_quiz.py
# ```
#
# Press Enter to begin. Answer each problem by typing the result and pressing
# Enter. The quiz displays your completion time when all problems are finished.
#
# ## Configuration
#
# Update these constants in `math_quiz.py` to customize the quiz:
#
# - `MIN_OPERAND`: smallest generated operand
# - `MAX_OPERAND`: largest generated operand
# - `TOTAL_PROBLEMS`: number of problems
# - `OPERATORS`: supported arithmetic operators
#
# ## Notes
#
# - Each answer must be entered as an integer string, such as `42`.
# - Incorrect answers can be retried.
# - The quiz ends when a problem times out.
