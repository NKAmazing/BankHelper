from abc import ABC, abstractmethod

class Service(ABC):
    '''
    Abstract class that defines the methods that must implement the classes that inherit from it
    param:
        - ABC: Abstract class from which it inherits.
    '''
    @abstractmethod  
    def add(self, model):
        '''
        Método abstracto para agregar un modelo
        param:
            - model: Model to add
        '''
        pass

    @abstractmethod    
    def get_all(self):
        '''
        Abstract method to get all models
        '''
        pass

    @abstractmethod
    def get_by_id(self, id):
        '''
        Abstract method to get a model by its id
        '''
        pass