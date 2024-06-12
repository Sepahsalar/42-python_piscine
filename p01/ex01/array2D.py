import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Truncate a 2D array and return the truncated version
    based on the provided start and end arguments.

    Parameters:
        family (list): A 2D list representing the array.
        start (int): The starting index for truncation.
        end (int): The ending index for truncation.

    Returns:
        list: The truncated 2D array.

    Raises:
        ValueError: If the input is not a 2D list
        with consistent row lengths.
    """
    try:
        if not isinstance(family, list) or not all(isinstance(row, list)
                                                   and len(row)
                                                   == len(family[0])
                                                   for row in family):
            raise ValueError("Input must be a 2D list with tthe same length")
    except ValueError as v:
        print(v)
        return None
    family_array = np.array(family)
    print("My shape is:", family_array.shape)
    sliced_array = family_array[start:end]
    print("My new shape is:", sliced_array.shape)
    return sliced_array.tolist()
