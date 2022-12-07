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


class mi_lista():
    def __init__(self, precio_total_lista, lista_dispositivos):
        self.precio_total_lista = precio_total_lista
        self.lista_dispositivos = lista_dispositivos

    def poner_lista(self, dispositivo):
        #aqui sumar al precio de la lista, el precio del periférico que vamos a poner al ordenador
        self.precio_total_lista #=+ dispositivo_salida().concretar_disporiivo().precio

    def quitar_lista(self, dispositivo):
        # primero hay que ver que el dispositivo que vamos a quitar, lo teniamos y que no es un elemento base pq no se puede quitar
        if dispositivo is in self.lista_dispositivos:
            self.lista_dispositivos.remove(self.lista_dispositivos)
        elif:
            print('No tenías este dispositivo añadido a lka lista')
        if dispositivo== unidad_central:
            print('Imposible quitar este dispositivo puesto que conforma la unidad básica del ordenador')

        #tambien hay que comprobar que  minimo se queda con un dispositivo de entrada y otro de salida
        #aqui sumar al precio de la lista, el precio del periférico que vamos a poner al ordenador
        self.precio_total_lista #=- dispositivo_salida().concretar_disporiivo().precio



from abc import ABCMeta, abstractmethod

#lo que haría: dos IBulder para componentes de entrada y salida

class IBuilder_entrada(metaclass=ABCMeta):
    "La interfaz del builder de los dispositivos de entrada"

    #todos los dispotivos de entrada tienen que tener los siguientes atributos
    def __init__(self, nombre_fabricante, modelo,precio_venta):
        self.nombre_fabricante = nombre_fabricante
        self.modelo=modelo
        self.precio_venta = precio_venta


    @staticmethod
    @abstractmethod
    def build_teclado(self, tipo_conector, puerto_valido):
        "Build del dispositivo de entrada teclado"
        self.nombre_fabricante ='Prueba 1 Teclado'
        self.modelo='Logitec'
        self.precio_venta =18
        tipo_conector='C'
        puerto_valido=3



    @staticmethod
    @abstractmethod
    def build_raton(self, tipo_conector, puerto_valido):
        "Build del ratón"
        self.nombre_fabricante ='Prueba 1 Ratón'
        self.modelo='Asus'
        self.precio_venta =20
        tipo_conector='A'
        puerto_valido=2

    @staticmethod
    @abstractmethod
    def build_tabletaGrafica(self, tipo_conector, puerto_valido):
        "Build de la tableta gráfica"
        self.nombre_fabricante ='Prueba 1 TabletaGráfica'
        self.modelo='Dell'
        self.precio_venta =450
        tipo_conector='B'
        puerto_valido=1


    @staticmethod
    @abstractmethod
    def build_pantallaTactil(self, tipo_conector, puerto_valido):
        "Build de la tableta gráfica"
        self.nombre_fabricante ='Prueba 1 pantalla táctil'
        self.modelo='Samsung'
        self.precio_venta =470
        tipo_conector='G'
        puerto_valido=6

    @staticmethod
    @abstractmethod
    def get_result():
        "Return the final product"

class Builder(IBuilder):
    "The Concrete Builder."

    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.parts.append('a')
        return self

    def build_part_b(self):
        self.product.parts.append('b')
        return self

    def build_part_c(self):
        self.product.parts.append('c')
        return self

    def get_result(self):
        return self.product

class Product():
    "The Product"

    def __init__(self):
        self.parts = []

class Director:
    "The Director, building a complex representation."

    @staticmethod
    def construct():
        "Constructs and returns the final product"
        return Builder()\
            .build_part_a()\
            .build_part_b()\
            .build_part_c()\
            .get_result()

# The Client
PRODUCT = Director.construct()
print(PRODUCT.parts)


# if __name__ == "__main__":

# 	f = Factory("French")
# 	e = Factory("English")
# 	s = Factory("Spanish")

# 	message = ["car", "bike", "cycle"]

# 	for msg in message:
# 		print(f.localize(msg))
# 		print(e.localize(msg))
# 		print(s.localize(msg))




#lista de patrones de diseño que veo útiles para el ejercicio:
#    -BUILDER
#    -FACTORY
