from abc import ABC, abstractmethod

class AbstractAnalysis(ABC):
    @abstractmethod
    def run_analysis(self, level: str):
        pass