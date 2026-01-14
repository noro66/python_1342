from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: Processed {result}"


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            return ""
        length = 0
        total = 0
        average = 0
        for n in data:
            total += n
            length += 1
        if length == 0:
            return "0 numeric values, sum=0, avg=0"
        average = total / length
        return (
            f"{length} numeric values, " +
            f"sum={total}, avg={average:.1f}"
            )

    def validate(self, data: Any) -> bool:
        try:
            count = 0
            for n in data:
                _ = n + 0
                count += 1
            return count > 0
        except (TypeError, ValueError):
            return False


class TextProcessor(NumericProcessor):
    pass


class LogProcessor(NumericProcessor):
    pass
