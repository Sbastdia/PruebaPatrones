from abc import ABC, abstractmethod

#Patrón Bridge

class Base(ABC):

    @abstractmethod
    def numeroAmbulancias(self) -> str:
        pass

    def tiempoEstimado(self) -> str:
        pass
class BaseCompuesta(Base):

    def __init__(self, nombre, bases: list[Base]):
        self.nombre = nombre
        self.base=bases

    def numeroAmbulancias(self):
        numero=0
        for base in self.base:
            numero+=base.numeroAmbulancias()
        return numero

    def tiempoEstimado(self):
        tiempo=0
        for base in self.base:
            tiempo+=base.tiempoEstimado()
        return tiempo/len(self.base)


class BaseSimple(Base):

    def __init__(self, nombre, numero, tiempo):
        self.nombre = nombre
        self.numero = numero
        self.tiempo = tiempo

    def numeroAmbulancias(self):
        return self.numero

    def tiempoEstimado(self):
        return self.tiempo

class Implementation(ABC):

    @abstractmethod
    def operation_implementation1(self) -> str:
        self.nombre = input("Introduce el nombre de la base (simple o compuesta): ")
        return self.nombre



class ConcreteImplementationA(BaseSimple):
    def operation_implementation1(self) -> str:
        return "ConcreteImplementationA: Aquí aparece el caso de una base simple"


class ConcreteImplementationB(BaseCompuesta):
    def operation_implementation2(self) -> str:
        return "ConcreteImplementationB: Aquí aparece el caso de una base compuesta"


def ejecutar():

    print("Ejemplo de la implementación de un patrón Bridge")
    print("")

    print("Introduce el nombre de la base (simple o compuesta): ")
    nombre = input()
    print("Introduce el número de ambulancias: ")
    numero = int(input())
    print("Introduce el tiempo estimado: ")
    tiempo = int(input())

    if nombre == "simple":
        base = ConcreteImplementationA(nombre, numero, tiempo)
        print(base.operation_implementation1())
    elif nombre == "compuesta":
        base = ConcreteImplementationB(nombre, numero, tiempo)
        print(base.operation_implementation2())
    else:
        print("No se ha introducido una base válida")

    print("")

    print("¿Quieres introducir otra base? (s/n)")
    respuesta = input()
    if respuesta == "s":
        ejecutar()
    else:
        print("Hasta pronto")

if __name__ == "__main__":

    ejecutar()