from typing import Any, Protocol, List, Dict, Union, Optional
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

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        ...
