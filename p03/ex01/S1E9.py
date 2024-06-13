from abc import ABC, abstractmethod


class Character(ABC):
    """
    Abstract class representing a character.

    Attributes:
        `first_name` (str): The first name of the character.

        `is_alive` (bool): The alive status of the character.
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Initialize a character with a first name and alive status.

        `first_name` The first name of the character.

        `is_alive` The alive status of the character, defaults to True.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """
        Mark the character as dead.

        This method should be implemented by subclasses to change the
        character's status to `dead`. The implementation should update
        the `is_alive` attribute to `False`.
        """
        pass


class Stark(Character):
    """
    Class representing a Stark character, inherits from Character.

    Attributes:
        `first_name` (str): The first name of the Stark character.

        `is_alive` (bool): The alive status of the Stark character.
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Initialize a Stark character with a first name and alive status.

        `first_name` The first name of the Stark character.

        `is_alive` The alive status of the Stark character,
        defaults to True.
        """
        super().__init__(first_name, is_alive)

    def die(self):
        """
        Mark the Stark character as dead by setting `is_alive` to `False`.
        """
        self.is_alive = False
