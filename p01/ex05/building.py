import sys


def count_characters(text):
    """
    Count the number of upper-case, lower-case, punctuation, digits,
    and spaces in the given text.

    Args:
    text (str): The input text to analyze.

    Returns:
    dict: A dictionary containing counts for upper-case, lower-case,
    punctuation, digits, and spaces.
    """
    if text is None:
        print("What is the text to count?")
        text = sys.stdin.readline()

    upper_count = sum(1 for char in text if char.isupper())
    lower_count = sum(1 for char in text if char.islower())
    punctuation_count = sum(1 for char in text if char in
                            "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
    digit_count = sum(1 for char in text if char.isdigit())
    space_count = sum(1 for char in text if char.isspace())

    return {
        "upper letters": upper_count,
        "lower letters": lower_count,
        "punctuation marks": punctuation_count,
        "digits": digit_count,
        "spaces": space_count
    }


def main():
    """
    Main function to handle command-line arguments
    and print the character counts.
    """
    try:
        if len(sys.argv) == 1:
            text = None
        elif len(sys.argv) == 2:
            text = sys.argv[1]
        else:
            raise AssertionError("Exactly one argument is required.")
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return

    counts = count_characters(text)

    total_chars = sum(counts.values())
    print(f"The text contains {total_chars} characters:")
    for category, count in counts.items():
        print(f"{count} {category}")


if __name__ == "__main__":
    main()
