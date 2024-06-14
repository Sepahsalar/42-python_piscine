def square(x):
    """
    Returns the `square` of the given number `x`.

    Parameters:
    `x` (`int` or `float`): The number to be squared.

    Returns:
    `int` or `float`: The square of `x`.
    """
    return x * x


def pow(x):
    """
    Returns the `exponentiation` of the given number `x `by itself.

    Parameters:
    `x` (`int` or `float`): The number to be exponentiated by itself.

    Returns:
    `int` or `float`: The result of `x` raised to the power of `x`.
    """
    return x ** x


def outer(x, function):
    """
    Returns an object that, when called,
    returns the result of applying the given `function` to `x`.
    Each call returns the result of applying the `function`
    to the result of the previous call.

    Parameters:
    `x` (`int` or `float`): The initial number.
    `function`: The `function` to be applied to `x`.

    Returns:
    `object`: An object that when called returns the result of the `function`.
    """
    count = 0

    def inner():
        """
        Applies the given `function` to the initial number `x` or
        the result of the previous call.

        Returns:
        `float`: The result of the function application.
        """
        nonlocal count
        result = x
        for _ in range(count + 1):
            result = function(result)
        count += 1
        return result
    return inner
