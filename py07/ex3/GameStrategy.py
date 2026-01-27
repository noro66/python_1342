from abc import ABC, abstractmethod
from typing import List, Dict


class GameStrategy(ABC):
    """
    Abstract base class defining a game strategy interface.

    A strategy encapsulates an algorithm for how to play a turn.
    Different strategies can be swapped without changing the game engine.

    This is the STRATEGY PATTERN in action!
    """

    @abstractmethod
    def execute_turn(self, hand: List, battlefield: List) -> Dict:
        """
        Execute a complete turn using this strategy.

        Args:
            hand: List of cards currently in hand
            battlefield: List of cards/entities on the battlefield

        Returns:
            Dictionary containing turn results
            (cards played, damage dealt, etc.)
        """
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        """Return the name of this strategy."""
        pass

    @abstractmethod
    def prioritize_targets(self, available_targets: List) -> List:
        """
        Order targets by priority according to this strategy.

        Args:
            available_targets: List of potential targets

        Returns:
            Sorted list with highest priority targets first
        """
        pass
