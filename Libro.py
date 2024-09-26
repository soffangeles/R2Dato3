import re

def validar_cadena(cadena):
    patron = r'^[a-zA-Z\s]+$'
    if re.match(patron, cadena):
        return True
    else:
        return False

class Libro:
    def __init__(self, *params):
        if len(params) == 0:
            # Constructor por omisión
            self.__titulo = "El Retrato de Dorian Gray"
            self.__autor = "Oscar Wilde"
            self.__genero = "Ficción gótica"
            self.__ISBN = 978-6070749087
            self.__publicacion = 1890
            self.__editorial = "Debolsillo"
            self.__edicion = 1
            self.__pags = 288

        elif len(params) == 8:
            # Constructor por parámetros
            self.__titulo = params[0]
            self.__autor = params[1]
            self.__genero = params[2]
            self.__ISBN = params[3] if (len(params[3]) == 13 and params[3].replace("-", "").isnumeric() and
                                        (params[3][:3]=="978" or params[3][:3]=="979")) else None
            self.__publicacion = params[4]
            self.__editorial = params[5]
            self.__edicion = int(params[6]) if int(params[6]) >= 1 else 1
            self.__pags = params[7] if params[7] > 10 else 10

    #Métodos GET

    @property
    def titulo(self):
        """
        Método GET del parametro título
        :return: el título del libro
        """
        return self.__titulo

    @property
    def autor(self):
        """
        Método GET del parametro autor
        :return: el autor del libro
        """
        return self.__autor

    @property
    def genero(self):
        """
        Método GET del parametro genero
        :return: el género del libro
        """
        return self.__genero

    @property
    def ISBN(self):
        """
        Método GET del parametro ISBN
        :return: El ISBN del libro
        """
        return self.__ISBN

    @property
    def publicacion(self):
        """
        Método GET del parametro publicación
        :return: El año de publicación del libro
        """
        return self.__publicacion

    @property
    def editorial(self):
        """
        Método GET del parametro editorial
        :return: La editorial del libro
        """
        return self.__editorial

    @property
    def edicion(self):
        """
        Método GET del parametro edición
        :return: El número de edición del libro
        """
        return self.__edicion

    @property
    def pags(self):
        """
        Método GET del parametro pags
        :return: El número de páginas del libro
        """
        return self.__pags

    # Métodos SET

    @titulo.setter
    def titulo(self, titulo):
        """
        Método setter del parámetro título
        :param titulo: el título a poner del libro
        :return:
        """
        self.__titulo = titulo

    @autor.setter
    def autor(self, autor):
        """
        Método setter del parámetro autor
        :param autor: El autor del libro
        """
        self.__autor = autor

    @genero.setter
    def genero(self, genero):
        """
        Método setter del parámetro género
        :param genero: El género del libro
        """
        self.__genero = genero

    @ISBN.setter
    def ISBN(self, ISBN):
        """
        Método setter del parámetro ISBN
        :param ISBN: El ISBN del libro
        """
        self.__ISBN = ISBN

    @publicacion.setter
    def publicacion(self, publicacion):
        """
        Método setter del parámetro publicación
        :param publicacion: El año de publicación del libro
        """
        self.__publicacion = publicacion

    @editorial.setter
    def editorial(self, editorial):
        """
        Método setter del parámetro editorial
        :param editorial: La editorial del libro
        """
        self.__editorial = editorial

    @edicion.setter
    def edicion(self, edicion):
        """
        Método setter del parámetro edición
        :param edicion: El número de edición del libro
        """
        self.__edicion = edicion

    @pags.setter
    def pags(self, pags):
        """
        Método setter del parámetro pags
        :param pags: El número de páginas del libro
        """
        self.__pags = pags

    # Métodos calculadores

    def __str__(self) -> str:
        """
        Método string de la clase que permite dar una representación en cadena de un objeto
        :return: Una representación en cadena de un libro
        """
        return ("Título: {} | Autor: {} | Género: {} | ISBN: {} Año de publicación: {} |"
                "Editorial: {} | Número de edición: {} | Número de páginas: {}").format(self.__titulo,
                                                   self.__autor,
                                                   self.__genero,
                                                   self.__ISBN,
                                                   self.__publicacion,
                                                   self.__editorial,
                                                   self.__edicion,
                                                   self.__pags)

    def __iter__(self):
        """
        Método iter de la clase que permite obtener una representación iterable de un objeto
        :return: Una representación iterable de un libro
        """
        return iter([self.__titulo, self.__autor, self.__genero, self.__ISBN, self.__publicacion, self.__editorial,
                     self.__edicion, self.__pags])

    def __llave(self):
        """
        Método que permite dar una clave para referenciar a los objetos
        :return: La clave del objeto
        """
        return (self.__titulo, self.__autor, self.__genero, self.__ISBN, self.__publicacion, self.__editorial,
                self.__edicion, self.__pags)

    def __hash__(self):
        """
        Método que permite hashear a los objetos
        :return: Una representación hasheable de los objetos
        """
        return hash(self.__llave())

    def __eq__(self, otro):
        """
        Método mágico de comparación entre dos objetos de la clase
        :param otro: El otro objeto a comparar
        :return: True si los objetos son iguales, False en otro caso
        """
        if isinstance(otro, Libro):
            return self.__llave() == otro.__llave()

    def __gt__(self, otro):
        """
        Método mágico que permite decir la comparación entre dos objetos
        :param otro: El otro objeto a comparar
        :return: True si nuestro objeto es mayor al otro, False en otro caso
        """
        if isinstance(otro, Libro):
            return self.__titulo > otro.__titulo

    def __compare_strings(self, str2: str) -> int:
        """
        Método que permite comparar 2 cadenas
        :param str2: La otra cadena a comparar
        :return: -1 si la primer cadena es menor, 1 si la segunda fue menor, 0 en otro caso
        """
        if str(self) < str2:
            return -1
        elif str(self) > str2:
            return 1
        else:
            return 0
