import sys
from abc import ABC, abstractmethod
from typing import List, Any, Optional, Dict, Union


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.stats = {}

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        ...

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return self.stats

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        return data_batch


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.avg_temp = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        total_temp = temp_val_count = r_process = 0
        result = "Processing sensor batch: ["

        for dictionary in data_batch:
            r_process += 1
            (key, value), = dictionary.items()
            result += f"{key}:{value},"
            if key == "temp":
                total_temp += value
                temp_val_count += 1

        result = result.rstrip(",")
        result += "]"

        try:
            self.avg_temp = total_temp / temp_val_count
        except ZeroDivisionError as e:
            print("ERROR: ", e, file=sys.stderr)
            return ""

        self.stats["reading_process"] = r_process
        self.stats["average_temp"] = self.avg_temp

        return result

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria:
            return [
                    dictionary
                    for dictionary in data_batch
                    if criteria in dictionary
                    ]
        return data_batch


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stats["buy"] = 0
        self.stats["sell"] = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            t_ops = net_flow = 0
            for dictionary in data_batch:
                t_ops += 1
                type_value = dictionary.get("type", "")
                amount_value = dictionary.get("amount", 0)
                if type_value == "buy":
                    net_flow += amount_value
                    self.stats["buy"] += amount_value
                elif type_value == "sell":
                    net_flow -= amount_value
                    self.stats["sell"] += amount_value
            return (
                f"Transaction analysis: {t_ops}, net flow: {net_flow} units"
                )
        except Exception as e:
            print("ERROR: ", e, file=sys.stderr)
            return ""

    def filter_data(self, data_batch: List[Any], criteria: str
                    | None = None) -> List[Any]:
        if criteria:
            return [dictionary
                    for dictionary in data_batch
                    if dictionary.get("type", "") == criteria
                    ]
        return data_batch
