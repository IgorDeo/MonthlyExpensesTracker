from abc import ABC, abstractmethod


class Iterator(ABC):
    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def __next__(self):
        pass
