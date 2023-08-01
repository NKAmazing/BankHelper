from abc import ABC, abstractmethod

class Command(ABC):
    '''
    Abstract class to define the structure of the commands
    '''
    @abstractmethod
    def execute(self):
        pass