from abc import ABC, abstractmethod
from django.db import models

# Abstract class that defines the methods that must implement the classes that inherit from it

class Create(ABC):
    '''
    Abstract class with the abstract methods to create a model
    param:
        - ABC: Abstract class from which it inherits.
    '''
    @abstractmethod  
    def create(self, model: models.Model):
        '''
        Method to create a model
        
        param:
            - model: Model to create
        '''
        pass

class Read(ABC):
    '''
    Abstract class with the abstract methods to read a model
    param:
        - ABC: Abstract class from which it inherits.
    '''
    @abstractmethod
    def find_all(self):
        '''
        Method to find all models
        '''
        pass

    @abstractmethod
    def find_by_id(self, id: int) -> models.Model:
        '''
        Method to find a model by its id
        '''
        pass

class Update(ABC):
    '''
    Abstract class with the abstract methods to update a model
    param:
        - ABC: Abstract class from which it inherits.
    '''
    @abstractmethod
    def update(self, model: models.Model) -> models.Model:
        '''
        Method to update a model
        '''
        pass

class Delete(ABC):
    '''
    Abstract class with the abstract methods to delete a model
    param:
        - ABC: Abstract class from which it inherits.
    '''
    @abstractmethod
    def delete(self, model: models.Model):
        '''
        Method to delete a model
        '''
        pass 

    @abstractmethod
    def delete_by_id(self, id: int):
        '''
        Method to delete a model by its id
        '''
        pass