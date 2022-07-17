from abc import ABC, abstractmethod


class Actor(ABC):
    @abstractmethod
    def act(self, driver):
        pass
