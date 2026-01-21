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
        if not data_batch or not isinstance(data_batch, list):
            return ""

        total_temp = temp_val_count = r_process = 0
        result = "Processing sensor batch: ["

        for dictionary in data_batch:
            if not isinstance(dictionary, dict):
                continue
            r_process += 1
            for key, value in dictionary.items():
                if key == "temp" and not isinstance(value, (int, float)):
                    continue
                result += f"{key}:{value}, "
                if key == "temp":
                    total_temp += value
                    temp_val_count += 1

        result = result.rstrip(" ,")
        result += "]"
        try:
            self.avg_temp = total_temp / temp_val_count
        except ZeroDivisionError as e:
            print("ERROR: ", e, file=sys.stderr)
            self.stats = {}
            return ""

        self.stats["ops"] = r_process
        self.stats["average_temp"] = self.avg_temp

        return result

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        if not data_batch or not isinstance(data_batch, list):
            return []

        if not criteria:
            return data_batch

        return [
                dictionary
                for dictionary in data_batch
                if criteria in dictionary
                and ((criteria == "temp" and dictionary["temp"] > 19)
                     or (criteria == "humidity"
                     and dictionary["humidity"] > 59)
                     )
                    ]


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stats["ops"] = 0
        self.stats["net_flow"] = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        if not data_batch or not isinstance(data_batch, list):
            return ""
        try:
            t_ops = net_flow = 0
            result = "Processing transaction batch: ["

            for dictionary in data_batch:
                if not isinstance(dictionary, dict):
                    continue
                t_ops += 1
                type_value = dictionary.get("type", "")
                amount_value = dictionary.get("amount", 0)
                if not isinstance(type_value, str) \
                        or not isinstance(amount_value, (int, float)):
                    continue

                if type_value == "buy":
                    result += f"{type_value}:{amount_value}, "
                    net_flow += amount_value

                elif type_value == "sell":
                    result += f"{type_value}:{amount_value}, "
                    net_flow -= amount_value

            result = result.rstrip(", ")
            result += "]"
            self.stats["ops"] = t_ops
            self.stats["net_flow"] = net_flow
            return result
        except Exception as e:
            print("ERROR: ", e, file=sys.stderr)
            return ""

    def filter_data(self, data_batch: List[Any], criteria: str
                    | None = None) -> List[Any]:
        if criteria:
            return [dictionary
                    for dictionary in data_batch
                    if (dictionary.get("type", "") == criteria
                        and dictionary.get("amount", 0) > 125)
                    ]
        return data_batch


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stats["ops"] = 0
        self.stats["error_count"] = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            t_event = t_errors = 0
            result = "Processing event batch ["
            not_first = True
            for event in data_batch:
                t_event += 1

                if not not_first:
                    result += " "
                not_first = False

                result += f"{event},"

                if event == "error":
                    self.stats["error_count"] += 1
                    t_errors += 1

            result = result.rstrip(",")
            result += "]"
            self.stats["ops"] = t_event
            self.stats["error_count"] = t_errors
            return result
        except Exception as e:
            print("ERROR: ", e, file=sys.stderr)
            return ""

    def filter_data(self, data_batch: List[Any],
                    criteria: str | None = None) -> List[Any]:
        if criteria:
            return [event
                    for event in data_batch
                    if event == criteria
                    ]
        return data_batch


class StreamProcessor:

    def process_stream(self, stream: DataStream, data: List[Any]) -> str:
        return stream.process_batch(data)

    def filter_stream(self, stream: DataStream,
                      data: List[Any], criteria: str) -> List[Any]:
        return stream.filter_data(data, criteria)

    def get_stream_stats(self, stream: DataStream) -> Dict:
        return stream.get_stats()


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")
    print("Initializing Sensor Stream...")
    stream_processor = StreamProcessor()
    stream_id = "SENSOR_001"
    sensor_data = [{"temp": 22.5}, {"humidity": 65}, {"temp": 23.0}]
    sensor_stream = SensorStream(stream_id)
    process = stream_processor.process_stream(sensor_stream, sensor_data)
    print(f"Stream ID: {stream_id}, Type: Environmental Data")
    print(process)
    sensor_stats = stream_processor.get_stream_stats(sensor_stream)
    print(
        f"Sensor analysis: {sensor_stats['ops']}",
        f"readings processed, avg temp: {sensor_stats['average_temp']:.1f}°C"
        )
    print()

    print("Initializing Transaction Stream...")
    stream_processor = StreamProcessor()
    stream_id = "TRANS_001"
    transaction_data = [{"type": "buy", "amount": 100},
                        {"type": "buy", "amount": 10},
                        {"type": "sell", "amount": 100},
                        {"type": "buy", "amount": 10},
                        {"type": "sell", "amount": 100},
                        {"type": "buy", "amount": 10},]
    transaction_stream = TransactionStream(stream_id)
    process = stream_processor.process_stream(transaction_stream,
                                              transaction_data)
    print(f"Stream ID: {stream_id}, Type:  Financial Data")
    print(process)
    transaction_stats = stream_processor.get_stream_stats(transaction_stream)
    print(
        f"Transaction analysis: {transaction_stats['ops']} operations,",
        f"net flow: {transaction_stats['net_flow']} units"
        )
    print()

    print("Initializing Event Stream...")
    stream_processor = StreamProcessor()
    stream_id = "EVENT_001"
    event_data = ["login", "error", "logout"]
    event_stream = EventStream(stream_id)
    process = stream_processor.process_stream(event_stream, event_data)
    print(f"Stream ID: {stream_id}, Type: System Events")
    print(process)
    event_stats = stream_processor.get_stream_stats(event_stream)
    print(
        f"Event analysis: {event_stats['ops']} events,",
        f"{event_stats['error_count']} error detected"
        )
    print()
    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")
    test_cases = [
     ("Sensor data", SensorStream("SENSOR_002"),
      [{"temp": 25.0}, {"humidity": 70}, {"temp": 34.4}],
      "readings processed"
      ),
     ("Transaction data",
      TransactionStream("SENSOR_002"),
      [
        {"type": "buy", "amount": 200},
        {"type": "sell", "amount": 50},
        {"type": "buy", "amount": 103},
        {"type": "sell", "amount": 30}
        ], "operations processed"
      ),
     (
      "Event data", EventStream("EVENT_002"),
      ["login", "error", "logout"],
      "events processed"
      ),
    ]
    print()
    for stream_data in test_cases:
        res = stream_processor.process_stream(stream_data[1], stream_data[2])
        stats = stream_processor.get_stream_stats(stream_data[1])
        if res:
            print(
                f"- {stream_data[0]}: {stats.get('ops', 0)} {stream_data[-1]}"
                )
    print()
    print("Stream filtering active: High-priority data only")
    sensor_stream = SensorStream("ENSOR_00")
    trans_stream = TransactionStream("TRANS_00")
    filter_sens_res = sensor_stream.filter_data(test_cases[0][2], "temp")
    filter_trans_res = trans_stream.filter_data(test_cases[1][2], "buy")
    len_sensor = len(filter_sens_res)
    len_trans = len(filter_trans_res)
    print(f"Filtered results: {len_sensor}",
          f"critical sensor alerts, {len_trans} large transaction")
    print()
    print("All streams processed successfully. Nexus throughput optimal.")
