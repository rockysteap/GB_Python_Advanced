import timeit

# Python Timeit() Syntax:
# Syntax: timeit.timeit(stmt, setup, timer, number)

# Parameter:
# stmt which is the statement you want to measure; it defaults to ‘pass’.
# setup which is the code that you run before running the stmt; it defaults to ‘pass’.

# We generally use this to import the required modules for our code.

# timer which is a timeit.Timer object;
#   it usually has a sensible default value so you don’t have to worry about it.
#   the number which is the number of executions you’d like to run the stmt.
# Returns the number of seconds it took to execute the code.

"""
Ex.1
# testing timeit()
import timeit

# code snippet to be executed only once
mysetup = "5+5"

print(timeit.timeit(mysetup))  # 0.0094435999635607
"""

"""
Ex.2
import timeit
import random


def fun():
    return random.randint(100, 800)


start = timeit.default_timer()
print("The start time is :", start)
fun()
print("The difference of time is :", timeit.default_timer() - start)

# The start time is : 786108.0703139
# The difference of time is : 3.029999788850546e-05
"""


