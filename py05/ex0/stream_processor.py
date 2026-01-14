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
        length, total, average = 0, 0, 0
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


class TextProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return ""
        is_space, w_count, char_count = True, 0, 0
        for c in data:
            if c == " ":
                is_space = True
            if c != " " and is_space:
                w_count += 1
                is_space = False
            char_count += 1
        return f"text: {char_count} characters, {w_count} words"

    def validate(self, data: Any) -> bool:
        try:
            count = 0
            for c in data:
                _ = c + ""
                count += 1
            return count > 0
        except Exception:
            return False


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            return ""
        if data[:6] == "ERROR:":
            message = data[7:]
            return f"ERROR level detected: {message}"
        elif data[:5] == "INFO:":
            message = data[6:]
            return f"INFO level detected: {message}"
        return ""

    def validate(self, data: Any) -> bool:
        try:
            if not (data[0:6] == "ERROR:" or data[0:5] == "INFO:"):
                return False
            count = 0
            for c in data:
                _ = c + ""
                count += 1
            return count > 0
        except Exception:
            return False

    def format_output(self, result: str) -> str:
        if result[0:5] == "ERROR":
            return f"[ALERT] {result}"
        return f"[INFO] {result}"


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    print()
    # Demo NumericProcessor
    print("Initializing Numeric Processor...")
    numeric = NumericProcessor()
    data1 = [1, 2, 3, 4, 5]
    print(f"Processing data: {data1}")
    if numeric.validate(data1):
        print("Validation: Numeric data verified")
    result = numeric.process(data1)
    print(numeric.format_output(result))
    print()

    # Demo TextProcessor
    print("Initializing Text Processor...")
    text = TextProcessor()
    data2 = "Hello Nexus World"
    print(f"Processing data: \"{data2}\"")
    if text.validate(data2):
        print("Validation: Text data verified")
    result = text.process(data2)
    print(text.format_output(result))
    print()

    # Demo LogProcessor
    print("Initializing Log Processor...")
    log = LogProcessor()
    data3 = "ERROR: Connection timeout"
    print(f"Processing data: \"{data3}\"")
    if log.validate(data3):
        print("Validation: Log entry verified")
    result = log.process(data3)
    print(log.format_output(result))
    print()

    # Polymorphic Demo
    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    test_cases = [
        (NumericProcessor(), [1, 2, 3]),
        (TextProcessor(), "Hello World"),
        (LogProcessor(), "INFO: System ready")
    ]

    result_num = 1
    for processor, data in test_cases:
        if processor.validate(data):
            result = processor.process(data)
            formatted = processor.format_output(result)
            print(f"Result {result_num}: {formatted}")
        result_num += 1

    print()
    print("Foundation systems online. Nexus ready for advanced streams.")
