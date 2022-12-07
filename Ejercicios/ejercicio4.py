# Ejercicio 4 (4 Puntos)
# En una aplicación de venta y configuración de ordenadores personales se considera un ordenador como la suma de varios componentes
# (una unidad central y varios elementos periféricos).
# El mínimo imprescindible para que se considere un ordenador es la unidad central, un dispositivo de entrada y otro de salida,
# pero pueden añadirse todos los que deseemos ofertar o que nos pidan los clientes.

# Para crearlo habrá que dar esos componentes mínimos y se puede modificar la configuración en cualquier momento añadiendo, quitando o cambiando
# exclusivamente periféricos. Por último, el precio de venta del ordenador es la suma de sus componentes.

# Todos componentes tienen información sobre el nombre del fabricante, el modelo y el precio de venta, que cambia con frecuencia.
# Los dispositivos de entrada que manejamos actualmente son el teclado, el ratón y la tableta gráfica.
# En todos los casos necesitamos saber el tipo de conector que utiliza (será un STRING) y los puertos válidos(varios valores de tipo entero).

# Los dispositivos de salida de que disponemos son las pantallas y las impresoras (de inyección y láser).
# También tenemos que saber los puertos válidos. Además para las impresoras necesitamos saber el tipo de cartucho o "tóner" utilizado
# y el número de páginas impresas desde el último cambio de "tóner"(sólo para impresoras láser).

# Por último tenemos un dispositivo especial, la pantalla táctil que sirve de dispositivo de entrada y de salida simultáneamente.
# Diseñe las clases y relaciones que representen una solución adecuada para este problema.
# Como consejo realiza un diagrama de clases de al menos las clases que representen el ordenador,
# los dos primeros niveles de la jerarquía de componentes y las impresoras láser.



#Nota: Se dispone de una clase mi_lista con las siguientes características: contador,precio_total_lista, poner(argumento) y quitar(argumento).







from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Builder(ABC):

    @property
    def product(self) -> None:
        pass

    def unidad_central(self) -> None:
        pass


    def teclado(self, nombre_fabricante, modelo, precio) -> None:
        pass

    def raton(self, nombre_fabricante, modelo, precio) -> None:
        pass


    def tabletaGrafica(self, nombre_fabricante, modelo, precio) -> None:
        pass

    def pantalla(self) -> None:
        pass

    def impresora(self) -> None:
        pass
    def pantallaTactil(self) -> None:
        pass


class ConcreteBuilder1(Builder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    @property
    def product(self) -> Product1:

        product = self._product
        self.reset()
        return product

    def produce_unidad_central(self) -> None:
        self._product.add("unidad_central")

    def produce_teclado(self,  nombre_fabricante, modelo, precio, tipo_conector, puerto_valido) -> None:
        self._product.add("teclado")
        print('(Teclado) Nombre del fabricante:'+ nombre_fabricante)
        print('(Teclado) modelo: '+ modelo)
        print('(Teclado) precio: '+ str(precio))
        print('(Teclado) tipo_conector: '+ tipo_conector)
        print('(Teclado) puerto_valido: '+ str(puerto_valido))

    def produce_raton(self) -> None:
        self._product.add("raton")

    def produce_tabletaGrafica(self) -> None:
        self._product.add("Tableta Grafica")

    def produce_pantalla(self) -> None:
        self._product.add("Pantalla")

    def produce_impresora(self) -> None:
        self._product.add("impresora")

    def produce_pantalla_tactil(self) -> None:
        self._product.add("pantalla tactil")


class Product1():

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}", end="")


class Director:

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_minimal_viable_product(self) -> None:
        self.builder.produce_unidad_central()
        self.builder.produce_teclado('Pablo', 'ASUS', 12, 'T', 2)
        self.builder.produce_pantalla()

    def build_full_featured_product(self) -> None:
        self.builder.produce_unidad_central()
        self.builder.produce_teclado('Pablo', 'ASUS', 12, 'T', 2)
        self.builder.produce_raton()
        self.builder.produce_tabletaGrafica()
        self.builder.produce_pantalla()
        self.builder.produce_impresora()

if __name__ == "__main__":

    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder

    print("Standard basic product: ")
    director.build_minimal_viable_product()
    builder.product.list_parts()

    print("\n")

    print("Standard full featured product: ")
    director.build_full_featured_product()
    builder.product.list_parts()

    print("\n")

    print("Custom product: ")
    builder.produce_unidad_central()
    builder.produce_teclado('Pablo', 'ASUS', 12, 'T', 2)
    builder.produce_raton()
    builder.produce_impresora()
    builder.product.list_parts()



#lista de patrones de diseño que veo útiles para el ejercicio:
#    -BUILDER
#    -FACTORY
