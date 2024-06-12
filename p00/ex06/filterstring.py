import sys
from ft_filter import ft_filter


def filter_strings(S, N):
    """Filter words in a string S that have a length greater than N."""
    words = S.split()
    return list(ft_filter(lambda word: len(word) > N, words))


def main():
    """
    Main function to handle command-line arguments
    and filter words from a string.

    The function expects exactly two arguments:
    - A string (S) containing words separated by spaces.
    - An integer (N) representing the minimum word length to filter.

    The function will print a list of words from S that
    have a length greater than N.

    If the number of arguments is incorrect or
    if the types of arguments are invalid,
    it prints an AssertionError with an appropriate message.
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return

    try:
        S = str(sys.argv[1])
    except ValueError:
        print("AssertionError: the arguments are bad")
        return

    try:
        N = int(sys.argv[2])
    except ValueError:
        print("AssertionError: the arguments are bad")
        return

    result = filter_strings(S, N)
    print(result)


if __name__ == "__main__":
    main()
