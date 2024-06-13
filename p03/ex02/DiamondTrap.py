from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    Class representing King, inheriting
    from both Baratheon and Lannister families.

    Attributes:
        `first_name` (str): The first name of the King.
        `is_alive` (bool): The alive status of the King.
        `family_name` (str): The family name of the King,
        defaults to 'Baratheon'.
        `eyes` (str): The eye color of the King, defaults to 'brown'.
        `hairs` (str): The hair color of the King, defaults to 'dark'.
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Initialize King with a first name and alive status.

        `first_name` The first name of King.
        `is_alive` The alive status of King, defaults to True.
        """
        super().__init__(first_name, is_alive)
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def set_eyes(self, eyes_color: str):
        """
        Set the eye color of King.

        `eyes_color` The new eye color for King.
        """
        self.eyes = eyes_color

    def set_hairs(self, hair_color: str):
        """
        Set the hair color of King.

        `hair_color` The new hair color for King.
        """
        self.hairs = hair_color

    def get_eyes(self) -> str:
        """
        Get the current eye color of King.

        `return` The current eye color.
        """
        return self.eyes

    def get_hairs(self) -> str:
        """
        Get the current hair color of King.

        `return` The current hair color.
        """
        return self.hairs
