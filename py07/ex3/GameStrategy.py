from abc import ABC, abstractmethod
from typing import Dict, Any, List


class GameStrategy(ABC):
    def execute_turn(
         self, hand: List[Any], battlefield: List[Any]
         ) -> Dict[str, Any]:
        pass
    execute_turn = abstractmethod(execute_turn)

    def get_strategy_name(self) -> str:
        pass
    get_strategy_name = abstractmethod(get_strategy_name)

    def prioritize_targets(self, available_targets: List[str]) -> List[str]:
        pass
    prioritize_targets = abstractmethod(prioritize_targets)
