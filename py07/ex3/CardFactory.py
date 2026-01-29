from abc import ABC, abstractmethod
from typing import Dict, Union  # Optional


class CardFactory(ABC):
    """
    Abstract Factory for creating card families.

    Each concrete factory (Fantasy, Sci-Fi, etc.) creates cards
    that belong together thematically, ensuring consistency.

    This is the ABSTRACT FACTORY PATTERN!
    """

    @abstractmethod
    def create_creature(self, name_or_power: Union[str, int, None] = None):
        """
        Create a creature card.

        Args:
            name_or_power: Optional name (str) or power level (int)

        Returns:
            A creature Card instance
        """
        pass

    @abstractmethod
    def create_spell(self, name_or_power: Union[str, int, None] = None):
        """
        Create a spell card.

        Args:
            name_or_power: Optional name (str) or power level (int)

        Returns:
            A spell Card instance
        """
        pass

    @abstractmethod
    def create_artifact(self, name_or_power: Union[str, int, None] = None):
        """
        Create an artifact card.

        Args:
            name_or_power: Optional name (str) or power level (int)

        Returns:
            An artifact Card instance
        """
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> Dict:
        """
        Create a complete themed deck.

        Args:
            size: Number of cards in the deck

        Returns:
            Dictionary with deck information and card list
        """
        pass

    @abstractmethod
    def get_supported_types(self) -> Dict:
        """
        Return the types of cards this factory can create.

        Returns:
            Dictionary mapping categories to available types
        """
        pass
