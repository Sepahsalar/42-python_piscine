import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[float]:
    """
    Calculate BMI values from height and weight lists.

    Parameters:
    height (list[int | float]): A list of heights in meters.
    weight (list[int | float]): A list of weights in kilograms.

    Returns:
    list[float]: A list of calculated BMI values.

    Raises:
    TypeError: If height or weight is not a list,
    or elements are not int or float.
    ValueError: If height and weight lists are not the same length.
    """
    try:
        if not isinstance(height, list) or not isinstance(weight, list):
            raise TypeError("Height and weight must be lists.")
        if len(height) != len(weight):
            raise ValueError("The lists must have the same length.")
        if not all(isinstance(h, (int, float)) for h in height):
            raise TypeError("Height elements must be int or float.")
        if not all(isinstance(w, (int, float)) for w in weight):
            raise TypeError("Weight elementsmust be int or float.")
    except TypeError as t:
        print(t)
        return None
    except ValueError as v:
        print(v)
        return None
    height_arr = np.array(height)
    weight_arr = np.array(weight)
    bmi_arr = weight_arr / (height_arr ** 2)
    return bmi_arr.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Apply a limit to BMI values to determine if they are above the limit.

    Parameters:
    bmi (list[int | float]): A list of BMI values.
    limit (int): The limit to compare each BMI value against.

    Returns:
    list[bool]: A list of booleans indicating
    if each BMI value is above the limit.

    Raises:
    TypeError: If bmi is not a list, or elements are not int or float,
    or limit is not an integer.
    """
    try:
        if bmi is None:
            return None
        if not isinstance(bmi, list):
            raise TypeError("BMI must be a list.")
        if not all(isinstance(b, (int, float)) for b in bmi):
            raise TypeError("Elements in the BMI list must be int or float.")
        if not isinstance(limit, int):
            raise TypeError("Limit must be an integer.")
    except TypeError as t:
        print(t)
        return None
    return [b > limit for b in bmi]
