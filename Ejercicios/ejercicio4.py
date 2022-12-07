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





# Para la resolución de este problema, usaré el Factory Method.

# class Ordenador_base():

# 	""" Esta es la base del ordenador, compuesta por la unidad central, un dispositivo de entreda y otro de salida. """

# 	def __init__(self, unidad_central, dispositivo_entrada, dispositivo_salida):
#         self.unidad_central=unidad_central
#         self.dispositivo_entrada=dispositivo_entrada
#         self.dispositivo_salida=dispositivo_salida


# 	# def localize(self, msg):

# 	# 	"""change the message using translations"""
# 	# 	return self.translations.get(msg, msg)

# class dispositivo_entrada():
# 	"""Definimos los periféricos de etrada: Teclado, Ratón y Tableta gráfica"""

# 	def __init__(self, nombre_fabricante, modelo, precio_venta):
# 		self.nombre_fabricante=nombre_fabricante
#         self.modelo=modelo
#         self.precio_venta=precio_venta

#     def necesario_conocer_de(self, tipo_de_conector, puerto_valido):
#         pass

# 	# def localize(self, msg):

# 	# 	"""change the message using translations"""
# 	# 	return self.translations.get(msg, msg)

# class dispositivo_salida():
# 	"""Definimos los periféricos de salida, Pantallas e impresora (de inyeccion o laser)"""

#     def necesario_conocer_ds(self, puerto_valido, tipo_cartucho, pag_impresas_cambio_toner):
#         pass

# 	# def localize(self, msg):
# 	# 	return msg

# def Factory(language ="English"):

# 	"""Factory Method"""
# 	localizers = {
# 		"Ordenador Base": Ordenador_base,
# 		"Dispositivos de entrada": dispositivo_entrada(),
# 		"Dispositivos de salida": dispositivo_salida(),
# 	}

# 	return localizers[language]()


# class mi_lista():
#     def __init__(self, precio_total_lista, lista_dispositivos):
#         self.precio_total_lista = precio_total_lista
#         self.lista_dispositivos = lista_dispositivos

#     def poner_lista(self, dispositivo):
#         #aqui sumar al precio de la lista, el precio del periférico que vamos a poner al ordenador
#         self.precio_total_lista #=+ dispositivo_salida().concretar_disporiivo().precio

#     def quitar_lista(self, dispositivo):
#         # primero hay que ver que el dispositivo que vamos a quitar, lo teniamos y que no es un elemento base pq no se puede quitar
#         if dispositivo is in self.lista_dispositivos:
#             self.lista_dispositivos.remove(self.lista_dispositivos)
#         elif:
#             print('No tenías este dispositivo añadido a lka lista')
#         if dispositivo== unidad_central:
#             print('Imposible quitar este dispositivo puesto que conforma la unidad básica del ordenador')

#         #tambien hay que comprobar que  minimo se queda con un dispositivo de entrada y otro de salida
#         #aqui sumar al precio de la lista, el precio del periférico que vamos a poner al ordenador
#         self.precio_total_lista #=- dispositivo_salida().concretar_disporiivo().precio



# from abc import ABCMeta, abstractmethod

# #lo que haría: dos IBulder para componentes de entrada y salida

# class IBuilder_entrada(metaclass=ABCMeta):
#     "La interfaz del builder de los dispositivos de entrada"

#     #todos los dispotivos de entrada tienen que tener los siguientes atributos
#     def __init__(self, nombre_fabricante, modelo,precio_venta):
#         self.nombre_fabricante = nombre_fabricante
#         self.modelo=modelo
#         self.precio_venta = precio_venta


#     @staticmethod
#     @abstractmethod
#     def build_teclado(self, tipo_conector, puerto_valido):
#         "Build del dispositivo de entrada teclado"
#         self.nombre_fabricante ='Prueba 1 Teclado'
#         self.modelo='Logitec'
#         self.precio_venta =18
#         tipo_conector='C'
#         puerto_valido=3



#     @staticmethod
#     @abstractmethod
#     def build_raton(self, tipo_conector, puerto_valido):
#         "Build del ratón"
#         self.nombre_fabricante ='Prueba 1 Ratón'
#         self.modelo='Asus'
#         self.precio_venta =20
#         tipo_conector='A'
#         puerto_valido=2

#     @staticmethod
#     @abstractmethod
#     def build_tabletaGrafica(self, tipo_conector, puerto_valido):
#         "Build de la tableta gráfica"
#         self.nombre_fabricante ='Prueba 1 TabletaGráfica'
#         self.modelo='Dell'
#         self.precio_venta =450
#         tipo_conector='B'
#         puerto_valido=1


#     @staticmethod
#     @abstractmethod
#     def build_pantallaTactil(self, tipo_conector, puerto_valido):
#         "Build de la tableta gráfica"
#         self.nombre_fabricante ='Prueba 1 pantalla táctil'
#         self.modelo='Samsung'
#         self.precio_venta =470
#         tipo_conector='G'
#         puerto_valido=6

#     @staticmethod
#     @abstractmethod
#     def get_result():
#         "Return the final product"



# class IBuilder_salida(metaclass=ABCMeta):

#     @staticmethod
#     @abstractmethod
#     def build_pantallas(puerto_valido):
#         puerto_valido=6

#     tipo=[]
#     tipo_recambio=[]
#     @staticmethod
#     @abstractmethod
#     def build_impresoras(puerto_valido,tipo, tipo_recambio, pags):
#         puerto_valido=7
#         tipo=['Inyección', 'Láser']
#         tipo_recambio=['Cartucho', 'Tóner']
#         pags=1490

#     @staticmethod
#     @abstractmethod
#     def build_pantallaTactil(nombre_fabricante, modelo, precio_venta, tipo_conector, puerto_valido):
#         "Build de la tableta gráfica"
#         nombre_fabricante ='Prueba 1 pantalla táctil'
#         modelo='Samsung'
#         precio_venta =470
#         tipo_conector='G'
#         puerto_valido=6



# class Builder(IBuilder_entrada, IBuilder_salida):
#     "The Concrete Builder."

#     def __init__(self):
#         self.product = Product()

#     def build_teclado(self):
#         self.product.parts.append('Teclado')
#         return self

#     def build_raton(self):
#         self.product.parts.append('Ratón')
#         return self

#     def build_tabletaGrafica(self):
#         self.product.parts.append('Tableta Gráfica')
#         return self


#     def build_pantallaTactil(self):
#         self.product.parts.append('Pantalla Táctil')
#         return self

#     def build_pantallas(self):
#         self.product.parts.append('Pantalla')
#         return self

#     def build_Impresora(self):
#         self.product.parts.append('Impresora')
#         return self

#     def get_result(self):
#         return self.product

# class Product():
#     "The Product"

#     def __init__(self):
#         self.parts = []

# class Director:
#     "The Director, building a complex representation."

#     @staticmethod
#     def construct():
#         "Constructs and returns the final product"
#         print(Builder().build_teclado())
#         print(Builder().get_result)
#         # return Builder()\
#         #     .build_teclado()\
#         #     .build_raton()\
#         #     #.build_impresoras(1, 'inyeccion', 'cartucho')\
#         #     .get_result()

# # The Client
# PRODUCT = Director.construct()
# print(PRODUCT.parts)


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
        self._product.add("unidad_central")

    def produce_teclado(self) -> None:
        self._product.add("teclado")

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
        self.builder.produce_teclado()
        self.builder.produce_pantalla()

    def build_full_featured_product(self) -> None:
        self.builder.produce_unidad_central()
        self.builder.produce_teclado()
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
    builder.produce_teclado()
    builder.produce_raton()
    builder.produce_impresora()
    builder.product.list_parts()



#lista de patrones de diseño que veo útiles para el ejercicio:
#    -BUILDER
#    -FACTORY
