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


    def teclado(self) -> None:
        pass

    def raton(self) -> None:
        pass

    def tabletaGrafica(self) -> None:
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
        self._product.add("Unidad central")

    def produce_teclado(self) -> None:
        self._product.add("Teclado")


    def get_teclado(self,  nombre_fabricante, modelo, precio, tipo_conector, puerto_valido) -> None:
        self._product.add("Teclado")
        print('(Teclado) Nombre del fabricante:'+ nombre_fabricante)
        print('(Teclado) modelo: '+ modelo)
        print('(Teclado) precio: '+ str(precio))
        print('(Teclado) tipo_conector: '+ tipo_conector)
        print('(Teclado) puerto_valido: '+ str(puerto_valido))
        self._product.sumar_precio(int(precio))

    def produce_raton(self) -> None:
        self._product.add("Ratón")


    def get_raton(self, nombre_fabricante, modelo, precio, tipo_conector, puerto_valido) -> None:
        self._product.add("Raton")
        print('(Ratón) Nombre del fabricante:'+ nombre_fabricante)
        print('(Ratón) modelo: '+ modelo)
        print('(Ratón) precio: '+ str(precio))
        print('(Ratón) tipo_conector: '+ tipo_conector)
        print('(Ratón) puerto_valido: '+ str(puerto_valido))
        self._product.sumar_precio(int(precio))

    def produce_tabletaGrafica(self) -> None:
        self._product.add("Tableta Gráfica")

    def get_tabletaGrafica(self, nombre_fabricante, modelo, precio, tipo_conector, puerto_valido) -> None:
        self._product.add("Tableta Grafica")
        print('(Tableta Gráfica) Nombre del fabricante:'+ nombre_fabricante)
        print('(Tableta Gráfic) modelo: '+ modelo)
        print('(Tableta Gráfic) precio: '+ str(precio))
        print('(Tableta Gráfic) tipo_conector: '+ tipo_conector)
        print('(Tableta Gráfic) puerto_valido: '+ str(puerto_valido))
        self._product.sumar_precio(int(precio))


    def produce_pantalla(self) -> None:
        self._product.add("Pantalla")

    def get_pantalla(self, nombre_fabricante, modelo, precio, puerto_valido) -> None:
        self._product.add("Pantalla")
        self._product.sumar_precio(precio)
        print('(Pantalla) Nombre del fabricante:'+ nombre_fabricante)
        print('(Pantalla) modelo: '+ modelo)
        print('(Pantalla) precio: '+ str(precio))
        print('(Pantalla) puerto_valido: '+ str(puerto_valido))
        self._product.sumar_precio(int(precio))

    def produce_impresora(self) -> None:
        self._product.add("Impresora")

    def get_impresora(self, nombre_fabricante, modelo, precio,puerto_valido, tipo_impresora, tipo_recambio, pags):
        self._product.add("impresora")
        print('(impresora) Nombre del fabricante:'+ nombre_fabricante)
        print('(impresora) modelo: '+ modelo)
        print('(impresora) precio: '+ str(precio))
        print('(impresora) puerto_valido: '+ str(puerto_valido))
        print('(Impresora) Tipo de impresora: '+ tipo_impresora)
        print('(Impresora) Tipo de recambio: '+ tipo_recambio)
        print('(Impresora) Páginas impresas desde el último cambio: '+ str(pags))
        self._product.sumar_precio(int(precio))


    def produce_pantalla_tactil(self) -> None:
        self._product.add("Pantalla Táctil")

    def get_pantalla_tactil(self, nombre_fabricante, modelo, precio, tipo_conector, puerto_valido) -> None:
        self._product.add("pantalla tactil")
        print('(Pantalla Táctil) Nombre del fabricante:'+ nombre_fabricante)
        print('(Pantalla Táctil) modelo: '+ modelo)
        print('(Pantalla Táctil) precio: '+ str(precio))
        print('(Pantalla Táctil) tipo_conector: '+ tipo_conector)
        print('(Pantalla Táctil) puerto_valido: '+ str(puerto_valido))
        self._product.sumar_precio(int(precio))



class Product1():

    def __init__(self) -> None:
        self.parts = []
        self.precios=[]

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def sumar_precio(self, precio: Any) -> None:
        self.precios.append(int(precio))


    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}", end="")
        print('\n')

    def total_prize(self) -> None:
        print(f"Precio total: {sum(self.precios)}", end="")


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
        self.builder.produce_teclado()
        self.builder.produce_pantalla()

    def build_full_featured_product(self) -> None:
        self.builder.produce_unidad_central()
        self.builder.produce_teclado()
        self.builder.produce_raton()
        self.builder.produce_tabletaGrafica()
        self.builder.produce_pantalla()
        self.builder.produce_impresora()
        self.builder.produce_pantalla_tactil()

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

    print("Custom1 product: ")
    builder.produce_unidad_central()
    builder.get_teclado('Pablo', 'ASUS', 12, 'T', 2)
    builder.get_raton('María', 'DELL', 34, 'A', 1)
    builder.get_impresora('Alex','Apple', 130, 5, 'Inyección', 'Cartucho', 0)
    builder.product.list_parts()
    builder.product.total_prize()


    print("\n")

    print("Custom2 product: ")
    builder.produce_unidad_central()
    builder.get_tabletaGrafica('Steve', 'Apple', 400, 'C', 3)
    builder.get_teclado('Bill', 'Microsoft', 230, 'B', 1)
    builder.get_pantalla_tactil('Rubén', 'HP', 69, 'R', 9)
    builder.product.list_parts()
    builder.product.total_prize()



    #quedaría: crear una condición que evalue que los elementos mínimos están en la lista para poder crear un ordenador
    #hacer que funcione lo del precio