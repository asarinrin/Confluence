from abc import ABC, ABCMeta, abstractmethod

# 抽象クラス
class Animal(ABC):
    
    @abstractmethod
    def cry(self) -> None:
        raise NotImplementedError

# 抽象クラスを実装した具象クラス
class Cat(Animal):
    def __init__(self): 
        pass
    
    def cry(self) -> str:
        return 'cry meow meow.'