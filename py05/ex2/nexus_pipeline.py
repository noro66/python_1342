from typing import Any, Protocol, List, Union
from abc import ABC, abstractmethod


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        ...


class InputStage:
    def process(self, data: Any) -> Any:
        try:
            if data:
                return data
            return {}
        except Exception as e:
            print("InputStage ERROR:", e)
            return data if data else {}


class TransformStage:
    def process(self, data: Any) -> Any:
        try:
            if isinstance(data, dict):
                data["processed"] = True
            if isinstance(data, str):
                data = f"Transformed: {data}"
            return data
        except Exception as e:
            print("TransformStage ERROR:", e)
            return data


class OutputStage:
    def process(self, data: Any) -> Any:
        try:
            return str(data)
        except Exception as e:
            print("OutputStage ERROR:", e)
            return ""


class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str) -> None:
        self.stages: List[ProcessingStage] = []
        self.pipeline_id = pipeline_id

    def add_stage(self, stage: ProcessingStage) -> None:
        if hasattr(stage, 'process') and callable(getattr(stage, 'process')):
            self.stages.append(stage)

    def _execute_pipeline_stages(self, data: Any) -> Any:
        try:
            result = data
            for stage in self.stages:
                result = stage.process(result)
            return result
        except Exception as e:
            print("Process ERROR: ", e)
            return data

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        ...


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        try:
            result = self._execute_pipeline_stages(data)
            return f"JSON Output: {result}"
        except Exception:
            return "JSON Output: Error processing data"


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        try:
            result = self._execute_pipeline_stages(data)
            return f"CSV Output: {result}"
        except Exception:
            return "CSV Output: Error processing data"


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        try:
            result = self._execute_pipeline_stages(data)
            return f"Stream Output: {result}"
        except Exception:
            return "Stream Output: Error processing data"


class NexusManager:
    def __init__(self) -> None:
        self.pipelines: List[ProcessingPipeline] = []

    def add_pipeline(
        self, pipeline: ProcessingPipeline
    ) -> None:
        if not pipeline or not isinstance(pipeline, ProcessingPipeline):
            return
        self.pipelines.append(pipeline)

    def process(
        self, pipeline: ProcessingPipeline, data: Any
    ) -> Union[str, Any]:
        try:
            return pipeline.process(data)
        except Exception as e:
            print("ERROR: ", e)
            return ""

    def chain_process(
        self, data: Any
    ) -> str:
        if not self.pipelines:
            return data
        res = data
        try:
            for pip in self.pipelines:
                res = self.process(pip, res)
            return res
        except Exception as e:
            print("ERROR:", e)
            return ""


class FailingStage:
    def process(self, data: Any) -> Any:
        raise ValueError("Invalid data format")


def stage_adder(adapter: ProcessingPipeline):
    stages = (InputStage(), TransformStage(), OutputStage())
    for stage in stages:
        adapter.add_stage(stage)


if __name__ == "__main__":
    try:
        print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")
        print("Initializing Nexus Manager...")
        print("Pipeline capacity: 1000 streams/second\n")
        print("Creating Data Processing Pipeline...")

        nexus_manager = NexusManager()
        json_adapter, csv_adapter, stream_adapter = \
            (JSONAdapter("ada_01"),
             CSVAdapter("ada_02"),
             StreamAdapter("ada_03")
             )
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
        print(f"Input: {json_data}")
        print("Transform: Enriched with metadata and validation")
        json_result = nexus_manager.process(json_adapter, json_data)
        print(json_result)
        print()

        print("Processing CSV data through same pipeline...")
        print(f"Input: {csv_data}")
        print("Transform: Enriched with metadata and validation")
        csv_result = nexus_manager.process(csv_adapter, csv_data)
        print(csv_result)
        print()

        print("Processing Stream data through same pipeline...")
        print(f"Input: {stream_data}")
        print("Transform: Enriched with metadata and validation")
        stream_result = nexus_manager.process(stream_adapter, stream_data)
        print(stream_result)
        print()

        # Chaining demo
        print("=== Pipeline Chaining Demo ===")
        print("Pipeline A -> Pipeline B -> Pipeline C")
        print("Data flow: Raw -> Processed -> Analyzed -> Stored")

        chain_result = nexus_manager.chain_process(
            "Raw data"
        )
        print(f"Chain result: {chain_result}")
        print("\n=== Error Recovery Test ===")
        print("Simulating pipeline failure...")

        bad_pipeline = JSONAdapter("bad_01")
        bad_pipeline.add_stage(InputStage())
        bad_pipeline.add_stage(FailingStage())

        result = nexus_manager.process(bad_pipeline, {"test": "data"})

        print(
            "\nAll streams processed successfully. Nexus throughput optimal."
            )
    except Exception as e:
        print("ERROR:", e)
