from abc import ABC, abstractmethod
from typing import List, Any, Optional, Dict, Union


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.stats = {}

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        ...

    @abstractmethod
    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        pass

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        ...
