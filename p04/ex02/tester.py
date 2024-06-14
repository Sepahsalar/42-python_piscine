from callLimit import callLimit


@callLimit(3)
def f():
    """
    A sample function to demonstrate call limiting.
    """
    print("f()")


@callLimit(1)
def g():
    """
    A sample function to demonstrate call limiting.
    """
    print("g()")


if __name__ == "__main__":
    for i in range(3):
        f()
        g()
