from abc import ABC, ABCMeta, abstractmethod

# 抽象クラス
class Vehicle(ABC):

    @property
    @abstractmethod
    def speed(self):
        pass
    
    @property
    @abstractmethod
    def direction(self):
        pass

    @speed.setter
    @abstractmethod
    def speed(self):
        pass
    
    @direction.setter
    @abstractmethod
    def direction(self):
        pass
    
    @abstractmethod
    def accelerate(self) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def deccelerate(self) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def turn_right(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def turn_left(self) -> None:
        raise NotImplementedError

# 抽象クラスを実装した具象クラス
class Car(Vehicle):
    def __init__(self): 
        self.__speed = 0
        self.__direction = 0
    
    @property
    def speed(self):
        return self.__speed
    
    @property
    def direction(self):
        return self.__direction

    @speed.setter
    def speed(self, value):
        self.__speed = value
    
    @direction.setter
    def direction(self, value):
        self.__direction = value

    def accelerate(self) -> None:
        self.speed += 1
    
    def deccelerate(self) -> None:
        self.speed -= 1

    def turn_right(self) -> None:
        self.direction += 1
        self.direction %= 4
    
    def turn_left(self) -> None:
        self.direction += 3
        self.direction %= 4
