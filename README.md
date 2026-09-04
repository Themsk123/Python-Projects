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
