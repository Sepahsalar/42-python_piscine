import sys


def check_odd_even(num):
    if num % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


try:
    if len(sys.argv) == 2:
        num = int(sys.argv[1])
        check_odd_even(num)
    elif len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
except ValueError:
    print("AssertionError: argument is not an integer")
