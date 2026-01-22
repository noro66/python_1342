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
    nexus_manager = NexusManager()
    json_adapter, csv_adapter, stream_adapter = \
        (JSONAdapter("ada_01"), CSVAdapter("ada_02"), StreamAdapter("ada_03"))
    for adapter in (json_adapter, csv_adapter, stream_adapter):
        stage_adder(adapter)
