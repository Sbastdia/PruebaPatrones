from __future__ import annotations
from abc import ABC, abstractmethod

#Patrón Bridge


class Abstraction:
    """
    The Abstraction defines the interface for the "control" part of the two
    class hierarchies. It maintains a reference to an object of the
    Implementation hierarchy and delegates all of the real work to this object.
    """

    def __init__(self, nombre, numero, tiempo, implementation: Implementation):
        self.implementation = implementation
        self.nombre = nombre
        self.numero = numero
        self.tiempo = tiempo

    def operation(self) -> str:
        return (f"Abstraction: Operación base con:\n"
                f"{self.implementation.operation_implementation1()}")


class ExtendedAbstraction(Abstraction):
    """
    You can extend the Abstraction without changing the Implementation classes.
    """

    def operation(self) -> str:
        return (f"ExtendedAbstraction: Operación extendida con:\n"
                f"{self.implementation.operation_implementation2()}")

    def operation2(self) -> str:
        return (f"ExtendedAbstraction: Operación extendida con:\n"
                f"{self.implementation.operation_implementation3()}")


class Implementation(ABC):
    """
    The Implementation defines the interface for all implementation classes. It
    doesn't have to match the Abstraction's interface. In fact, the two
    interfaces can be entirely different. Typically the Implementation interface
    provides only primitive operations, while the Abstraction defines higher-
    level operations based on those primitives.
    """

    @abstractmethod
    def operation_implementation1(self) -> str:
        self.nombre = input("Introduce el nombre de la base (simple o compuesta): ")
        return self.nombre

    @abstractmethod
    def operation_implementation2(self) -> str:

        self.numero = input("Introduce el número de ambulancias: ")
        if(self.numero.isdigit()):
            self.numero = int(self.numero)

        if(self.nombre == "simple"):
            if(self.numero > 3):
                self.numero = 3

        elif(self.nombre == "compuesta"):
            if(self.numero > 5):
                self.numero = 5

        return self.numero


    @abstractmethod
    def operation_implementation3(self) -> str:
        self.tiempo = input("Introduce el tiempo medio de asistencia: ")

        return self.tiempo

"""
Each Concrete Implementation corresponds to a specific platform and implements
the Implementation interface using that platform's API.
"""


class ConcreteImplementationA(Implementation):
    def operation_implementation1(self) -> str:
        return "ConcreteImplementationA: Aquí aparece el nombre de la base"


class ConcreteImplementationB(Implementation):
    def operation_implementation2(self) -> str:
        return "ConcreteImplementationB: Aquí aparece el número de ambulancias"

class ConcreteImplementationC(Implementation):
    def operation_implementation3(self) -> str:
        return "ConcreteImplementationB: Aquí aparece el tiempo medio de asistencia"



def client_code(abstraction: Abstraction) -> None:
    """
    Except for the initialization phase, where an Abstraction object gets linked
    with a specific Implementation object, the client code should only depend on
    the Abstraction class. This way the client code can support any abstraction-
    implementation combination.
    """

    # ...

    print(abstraction.operation(), end="")

    # ...


if __name__ == "__main__":
    """
    The client code should be able to work with any pre-configured abstraction-
    implementation combination.
    """

    implementation = ConcreteImplementationA()
    abstraction = Abstraction(implementation)
    client_code(abstraction)

    print("\n")

    implementation = ConcreteImplementationB()
    abstraction = ExtendedAbstraction(implementation)
    client_code(abstraction)



    implementation = ConcreteImplementationC()
    abstraction = ExtendedAbstraction(implementation)
    client_code(abstraction)