class calculator:
    """
    A class to perform arithmetic operations on vectors with scalars.

    Attributes:
        `vector` (list): The vector to perform operations on.
    """

    def __init__(self, vector: list):
        """
        Initialize the calculator with a vector.

        `vector` The list representing the vector.
        """
        self.vector = vector

    def __str__(self):
        """
        Returns a string representation of the vector.
        """
        return str(self.vector)

    def __repr__(self):
        """
        Returns a string representation of the vector for debugging.
        """
        return f"calculator({self.vector})"

    def __add__(self, scalar):
        """
        Perform addition of scalar to each element of the vector
        and print the result.

        `scalar` The scalar value to add.
        """
        result = [element + scalar for element in self.vector]
        print(result)
        self.vector = result

    def __mul__(self, scalar):
        """
        Perform multiplication of each element of the vector by scalar
        and print the result.

        `scalar` The scalar value to multiply.
        """
        result = [element * scalar for element in self.vector]
        print(result)
        self.vector = result

    def __sub__(self, scalar):
        """
        Perform subtraction of scalar from each element of the vector
        and print the result.

        `scalar` The scalar value to subtract.
        """
        result = [element - scalar for element in self.vector]
        print(result)
        self.vector = result

    def __truediv__(self, scalar):
        """
        Perform division of each element of the vector by scalar
        and print the result.

        `scalar` The non-zero scalar value to divide by.

        Raises `ZeroDivisionError` If scalar is 0.
        """
        try:
            if scalar == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            result = [element / scalar for element in self.vector]
            print(result)
            self.vector = result
        except ZeroDivisionError as e:
            print(f"Error: {e}")
            return None
