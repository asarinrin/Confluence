from injector import Injector, Binder
from animal import Animal, Cat
from vehicle import Vehicle, Car

class DependencyInjectionContainer():

    def __init__(self) -> None:
        self.injector = Injector(self.__class__.config)

    @classmethod
    def config(cls, binder: Binder):
        binder.bind(Animal, Cat)
        binder.bind(Vehicle, Car)
        # binder.multibind(dict[Animal, Vehicle], to={Cat, Car})

    def resolve(self, cls):
        return self.injector.get(cls)