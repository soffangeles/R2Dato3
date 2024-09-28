#Importamos todas las interfaces y clases necesarias
from typing import TypeVar
import numpy as np
import Libro as L
from Orden_secuencia import quick_sort1
from Secuenciable import Secuenciable
import csv

T = TypeVar('T')

class Secuencia(Secuenciable):

    def __init__(self, *params):
        if len(params) == 0:  # Constructor por omisión
            self.__datos = np.empty(30, dtype=L.Libro)
            self.__nd = 0
            print("Se creo una secuencia para 20 elementos!\n")
        elif len(params) == 1:  # Constructor por parámetros
            try:
                self.__datos = np.empty(params[0], dtype=L.Libro)
                self.__nd = 0
                print(f"Se creo una secuencia para {params[0]} elementos!\n")
            except ValueError:
                print("El tamaño del arreglo debe ser positivo!\n")

    def __iter__(self):
        """
        Método iterable de la secuencia que permite conocer sus elementos uno por uno
        :return: Una representación iterable de la secuencia
        """
        self.pos = 0
        return self

    def __next__(self) -> L.Libro:
        """
        Método next de la representación iterable de la secuencia
        :return: El siguiente elemento de la iteración
        """
        if self.pos < self.nd:
            a = self.datos[self.pos]
            self.pos += 1
            return a
        else:
            raise StopIteration

    # Métodos GET

    @property
    def datos(self):
        """
        Método GET del parámetro "datos"
        :return:
        """
        return self.__datos

    @property
    def nd(self) -> int:
        """
        Método GET del parámetro "nd" (quien indica la posición del siguiente elemento a agregar)
        :return:
        """
        return self.__nd

    # Métodos calculadores

    def agregar1(self, elemento: T):
        """
        Método que agrega un elemento a la sucesión.
        Si el arreglo está lleno, crea uno nuevo con el doble de capacidad
        y copia los elementos del arreglo anterior al nuevo.
        :param elemento: El elemento a agregar.
        """

        if self.__nd == len(self.__datos):
            # Si el arreglo está lleno, crea uno nuevo con el doble de capacidad
            nuevo_tamano = len(self.__datos) * 2
            nuevo_datos = np.empty(nuevo_tamano, dtype=L.Libro)
            # Copia los elementos del arreglo anterior al nuevo.
            for i in range(self.__nd):
                nuevo_datos[i] = self.__datos[i]
            # Actualiza la referencia al nuevo arreglo.
            self.__datos = nuevo_datos

        # Agrega el elemento al arreglo
        self.__datos[self.__nd] = elemento
        self.__nd += 1

    def agregar2(self, elemento: T, nveces: int):
        """
        Segundo parémetro que agrega elementos a la sucesión, solo que
        ahora agrega varios elementos (iguales) a la vez
        :param elemento: El elemento a agregar
        :param nveces: Las veces que se va a agregar el elemento
        """

        if nveces <= 0:
            return

        if self.__nd + nveces > len(self.__datos):
            # Si no hay suficiente espacio, crea un nuevo arreglo
            nuevo_tamano = len(self.__datos) * 2
            while nuevo_tamano - self.__nd < nveces:
                nuevo_tamano *= 2
            nuevo_datos = np.empty(nuevo_tamano, dtype=L.Libro)
            # Copia los elementos del arreglo anterior al nuevo.
            for i in range(self.__nd):
                nuevo_datos[i] = self.__datos[i]
            # Actualiza la referencia al nuevo arreglo.
            self.__datos = nuevo_datos

        # Agrega los elementos al arreglo
        for _ in range(nveces):
            self.__datos[self.__nd] = elemento
            self.__nd += 1

    def contiene(self, valor: T) -> bool:
        """
        Método que nos dice si la secuencia contiene a un elemento o no
        :param valor: El elemento a buscar
        :return: True si está contenido, False en caso contrario
        """
        for elemento in self.__datos[:self.__nd]:
            if elemento == valor:
                return True
        return False

    def repeticiones(self, elemento: T) -> int:
        repeticiones = 0
        for libro in self.__datos[:self.__nd]:
            if libro.titulo == elemento.titulo and libro.autor == elemento.autor and libro.ISBN == elemento.ISBN:  # Compara atributos relevantes
                repeticiones += 1
        return repeticiones

    def __encuentra(self, valor: T) -> int:
        """
        Método que nos dice la posición que ocupa un elemento en particular dentro de la secuencia
        :param valor: El elemento a decir su posición
        :return: La posición en la que se encuentra, None si no se encuentra
        """
        # Verificar si la secuencia está ordenada (puedes agregar una bandera o método para esto)
        ordenada = False # Asumiendo que no está ordenada por defecto

        if ordenada:
            # Búsqueda binaria si la secuencia está ordenada
            inicio = 0
            fin = self.__nd - 1

            while inicio <= fin:
                medio = (inicio + fin) // 2

                if self.__datos[medio] == valor:
                    return medio  # Lo encontró
                elif self.__datos[medio] < valor:
                    inicio = medio + 1
                else:
                    fin = medio - 1
        else:
            # Búsqueda lineal si la secuencia no está ordenada
            for i in range(self.__nd):
                if self.__datos[i] == valor:
                    return i

        return None # No se encontró el elemento

    def eliminar1(self, elemento: T):
        """
        Método que permite eliminar de la secuencia todas las veces que aparezca un elemento.
        :param elemento: El elemento a eliminar
        """
        indices_a_eliminar = []  # Lista para almacenar los índices de los elementos a eliminar

        for i in range(self.__nd):
            # Compara atributos relevantes en lugar de objetos
            if self.__datos[i].titulo == elemento.titulo and self.__datos[i].autor == elemento.autor and self.__datos[
                i].ISBN == elemento.ISBN:
                indices_a_eliminar.append(i)  # Agregar el índice a la lista

        # Eliminar los elementos utilizando los índices en orden inverso
        for indice in reversed(indices_a_eliminar):
            self.__datos = np.delete(self.__datos, indice)  # Eliminar el elemento
            self.__nd -= 1  # Decrementar el número de elementos

        if not indices_a_eliminar:  # Si no se encontraron elementos para eliminar
            print("El elemento no se encuentra en la secuencia\n")

    def eliminar_libro(self, elemento: T):
        if self.contiene(elemento):
            pos = self.__encuentra(elemento)
            if pos is not None:
                # Desplazar los elementos a la izquierda para eliminar el elemento
                for i in range(pos, self.__nd - 1):
                    self.__datos[i] = self.__datos[i + 1]
                self.__nd -= 1
                self.__datos[self.__nd] = None  # Opcional: marcar la posición como vacía

    def eliminar2(self, elemento: T, nveces: int):
        if not self.contiene(elemento) or nveces <= 0:
            return

        eliminados = 0
        while eliminados < nveces and self.contiene(elemento):
            self.eliminar_libro(elemento)
            eliminados += 1

    def esta_vacia(self) -> bool:
        """
        Método que nos permite decir si nuestra secuencia está vacía
        :return: True si la secuencia es vacía, False en otro caso
        """
        if self.__nd == 0:
            return True

    def cardinalidad(self) -> int:
        """
        Método que nos dice el número total de elementos que hay en la sucesión
        :return: La cantidad total de elementos que tiene la sucesión
        """
        return self.__nd

    def vaciar(self):
        """
        Método que vuelve a la sucesión vacía
        """
        self.__nd = 0

    def secuencia_unico(self):
        """
        Método que devuelve una representación de la sucesión donde cada elemento está
        dentro de esta a lo mas una vez
        """
        it1=iter(self)
        try:
            while True:
                elem = next(it1)
                reps = self.repeticiones(elem)
                self.eliminar2(elem, reps-1)
        except StopIteration:
            pass

    def comparar_libros_titulo(libro1: L.Libro, libro2: L.Libro) -> int:
        """
        Función que compara dos libros por su título.

        :param libro1: El primer libro a comparar.
        :type libro1: L.Libro
        :param libro2: El segundo libro a comparar.
        :type libro2: L.Libro
        :return: Un entero que indica la relación entre los títulos de los libros.
                 -1 si el título de libro1 es menor que el de libro2.
                  0 si los títulos son iguales.
                  1 si el título de libro1 es mayor que el de libro2.
        :rtype: int
        """
        if libro1.titulo < libro2.titulo:
            return -1
        elif libro1.titulo > libro2.titulo:
            return 1
        else:
            return 0

    def comparar_libros_genero_titulo(libro1: L.Libro, libro2: L.Libro) -> int:
        """
        Función que compara dos libros por género y título.

        :param libro1: El primer libro a comparar.
        :type libro1: L.Libro
        :param libro2: El segundo libro a comparar.
        :type libro2: L.Libro
        :return: Un entero que indica la relación entre los géneros y títulos de los libros.
                 -1 si el género o título de libro1 es menor que el de libro2.
                  0 si los géneros y títulos son iguales.
                  1 si el género o título de libro1 es mayor que el de libro2.
        :rtype: int
        """
        if libro1.genero < libro2.genero:
            return -1
        elif libro1.genero > libro2.genero:
            return 1
        else:  # Si los géneros son iguales, comparar por título
            if libro1.titulo < libro2.titulo:
                return -1
            elif libro1.titulo > libro2.titulo:
                return 1
            else:
                return 0

    def ordenar(self):
        """
        Método que permite ordenar de manera ascendente los elementos de la
        sucesión
        :return: La sucesión ordenada de manera ascendente
        """
        arreglo = self.__datos.copy()
        if len(arreglo) > 1:
            orden = quick_sort1(arreglo.copy(), 0, self.__nd - 1,
                                Secuencia.comparar_libros_titulo)
            for libro in orden:
                if libro is not None:
                    print(libro)
            print()
        else:
            return arreglo

    def ordenar2(self, comparador):
        """
        Método que permite ordenar los elementos de la sucesión usando un comparador
        :param comparador: La manera de ordenar los elementos de la sucesión
        :return: La sucesión ordenada mediante el comparador
        """
        arreglo = self.__datos.copy()
        if len(arreglo) > 1:
            orden = quick_sort1(arreglo.copy(), 0, self.__nd - 1, comparador)
            for libro in orden:
                if libro is not None:
                    print(libro)
            print()
        else:
            return arreglo

    def guardar_en_csv(self, nombre_archivo: str):
        """
        Guarda los datos del inventario en un archivo CSV usando un iterador.

        :param nombre_archivo: El nombre del archivo CSV donde se guardarán los datos.
        """
        with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo_csv:
            escritor = csv.writer(archivo_csv)
            # Escribir la cabecera
            escritor.writerow(["titulo", "autor", "genero", "ISBN", "publicacion", "editorial", "edicion", "pags"])

            # Crear un iterador para la secuencia
            iterador_libros = iter(self)

            try:
                while True:
                    libro = next(iterador_libros)
                    escritor.writerow(list(libro))
            except StopIteration:
                pass
