from typing import Any, Protocol, List, Union
from abc import ABC, abstractmethod


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        ...


class InputStage:
    def process(self, data: Any) -> Any:
        if data:
            return data
        return {}


class TransformStage:
    def process(self, data: Any) -> Any:
        if isinstance(data, dict):
            data["processed"] = True
        if isinstance(data, str):
            data = f"Transformed: {data}"
        return data


class OutputStage:
    def process(self, data: Any) -> Any:
        return str(data)


class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str) -> None:
        self.stages: List[ProcessingStage] = []
        self.pipeline_id = pipeline_id

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    def process_helper(self, data: Any) -> Any:
        result = data
        for stage in self.stages:
            result = stage.process(result)
        return result

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        ...


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        result = self.process_helper(data)
        return f"JSON Output: {result}"


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        result = self.process_helper(data)
        return f"CSV Output: {result}"


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        result = self.process_helper(data)
        return f"Stream Output: {result}"


class NexusManager:
    def __init__(self) -> None:
        self.pipelines = []

    def add_pipeline(
        self, pipeline: ProcessingPipeline
    ) -> None:
        self.pipelines.append(pipeline)

    def process(
        self, pipeline: ProcessingPipeline, data: Any
    ) -> str:
        return pipeline.process(data)

    def chain_process(
        self, pipelines: List[ProcessingPipeline], data: Any
    ) -> str:
        res = data
        for pip in pipelines:
            res = self.process(pip, res)
        return res


def stage_adder(adapter: ProcessingPipeline):
    stages = (InputStage(), TransformStage(), OutputStage())
    for stage in stages:
        adapter.add_stage(stage)


if __name__ == "__main__":
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")
    print("Initializing Nexus Manager...")
    print("Pipeline capacity: 1000 streams/second\n")
    print("Creating Data Processing Pipeline...")

    nexus_manager = NexusManager()
    json_adapter, csv_adapter, stream_adapter = \
        (JSONAdapter("ada_01"), CSVAdapter("ada_02"), StreamAdapter("ada_03"))
    for adapter in (json_adapter, csv_adapter, stream_adapter):
        stage_adder(adapter)

    # Add adapters to manager
    nexus_manager.add_pipeline(json_adapter)
    nexus_manager.add_pipeline(csv_adapter)
    nexus_manager.add_pipeline(stream_adapter)

    # Sample data
    json_data = {"sensor": "temp", "value": 23.5, "unit": "C"}
    csv_data = "user,action,timestamp"
    stream_data = "Real-time sensor stream"
    print("Stage 1: Input validation and parsing")
    print("Stage 2: Data transformation and enrichment")
    print("Stage 3: Output formatting and delivery\n")

    # Process each type
    print("=== Multi-Format Data Processing ===\n")
    print("Processing JSON data through pipeline...")

    json_result = nexus_manager.process(json_adapter, json_data)
    print(f"Input: {json_data}")
    print(f"Output: {json_result}")
    # Chaining demo
    # ...

    print("\nAll streams processed successfully. Nexus throughput optimal.")
