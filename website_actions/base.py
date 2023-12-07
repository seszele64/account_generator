from abc import ABC, abstractmethod

class BaseService(ABC):

    @abstractmethod
    def create_account(self, **kwargs):
        pass

    @abstractmethod
    def register(self, **kwargs):
        pass