from S1E9 import Character


class Baratheon(Character):
    """
    Representing the Baratheon family.

    Attributes:
        `first_name` (str): The first name of the Baratheon character.
        `is_alive` (bool): The alive status of the Baratheon character.
        `family_name` (str): The family name, default is "Baratheon".
        `eyes` (str): Eye color, default is "brown".
        `hairs` (str): Hair color, default is "dark".
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Initialize a Baratheon character with a first name and alive status.

        `first_name` The first name of the Baratheon character.

        `is_alive` The alive status of the Baratheon character,
        defaults to True.
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """
        Return a string representation of the Baratheon character.

        `return` A string describing the character's family,
        eye color, and hair color.
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """
        Return a string representation of the Baratheon character
        for debugging.

        `return` A string describing the character's family,
        eye color, and hair color.
        """
        return self.__str__()

    def die(self):
        """
        Mark the character as dead by setting `is_alive` to `False`.
        """
        self.is_alive = False


class Lannister(Character):
    """
    Representing the Lannister family.

    Attributes:
        `first_name` (str): The first name of the Lannister character.
        `is_alive` (bool): The alive status of the Lannister character.
        `family_name` (str): The family name, default is "Lannister".
        `eyes` (str): Eye color, default is "blue".
        `hairs` (str): Hair color, default is "light".
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Initialize a Lannister character with a first name and alive status.

        `first_name` The first name of the Lannister character.

        `is_alive` The alive status of the Lannister character,
        defaults to True.
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """
        Return a string representation of the Lannister character.

        `return` A string describing the character's family,
        eye color, and hair color.
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """
        Return a string representation of the Lannister character
        for debugging.

        `return` A string describing the character's family,
        eye color, and hair color.
        """
        return self.__str__()

    def die(self):
        """
        Mark the character as dead by setting `is_alive` to `False`.
        """
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool = True):
        """
        Class method to create a Lannister character.

        `first_name` The first name of the Lannister character.

        `is_alive` The alive status of the Lannister character,
        defaults to True.

        `return` An instance of Lannister.
        """
        return cls(first_name, is_alive)
