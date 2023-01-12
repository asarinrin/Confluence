from dicontainer import DependencyInjectionContainer
from usecase import UseCase

def main():

    dicontainer = DependencyInjectionContainer()
    usecase = dicontainer.resolve(UseCase)
    usecase.action()



if __name__ == "__main__":
    main()