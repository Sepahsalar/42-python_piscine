class calculator:
    """
    A class to perform vector operations.

    Methods:
        `dotproduct` Calculates dot product of two vectors.

        `add_vec` Adds two vectors element-wise.

        `sous_vec` Subtracts second vector from the first element-wise.
    """
    @classmethod
    def dotproduct(cls, V1, V2):
        """
        Calculate the dot product of two vectors.

        `V1` First vector as a list of floats.

        `V2` Second vector as a list of floats.
        """
        result = sum(x * y for x, y in zip(V1, V2))
        print(f"Dot product is: {result}")

    @classmethod
    def add_vec(cls, V1, V2):
        """
        Add two vectors element-wise.

        `V1` First vector as a list of floats.

        `V2` Second vector as a list of floats.
        """
        result = [float(x + y) for x, y in zip(V1, V2)]
        print(f"Add Vector is : {result}")

    @classmethod
    def sous_vec(cls, V1, V2):
        """
        Subtract second vector from the first element-wise.

        `V1` First vector as a list of floats.
        `V2` Second vector as a list of floats.
        """
        result = [float(x - y) for x, y in zip(V1, V2)]
        print(f"Sous Vector is: {result}")
