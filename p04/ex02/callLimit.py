def callLimit(limit):
    """
    A decorator factory that returns a decorator to limit
    the number of times a function can be called.

    Args:
    - `limit` (int): The maximum number of times
    the decorated function can be called.

    Returns:
    - A `decorator` that limits the function calls.
    """
    def callLimiter(function):
        """
        A decorator that wraps a function to limit
        its number of calls.

        Args:
        - `function`: The function to be limited.

        Returns:
        - The `wrapped` function with a call `limit`.
        """
        count = 0

        def limit_function(*args, **kwds):
            """
            The wrapper function that enforces the call limit.

            Args:
            - `*args`: Positional arguments for the wrapped function.
            - `**kwds`: Keyword arguments for the wrapped function.
            """
            nonlocal count
            if count < limit:
                count += 1
                function(*args, **kwds)
            else:
                print(f"Error: {function} call too many times")
        return limit_function
    return callLimiter
