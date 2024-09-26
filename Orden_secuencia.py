def __particion(arreglo, inicio, fin) -> int:
    """
    Esta función organiza los elementos del arreglo de manera que todos los elementos
    menores o iguales al pivote estén a la izquierda y todos los elementos mayores estén
    a la derecha. El pivote se coloca en su posición correcta.
    :param arreglo: int[] Arreglo de enteros
    :param inicio: La posición inicial
    :param fin: La posición final
    :return: La posición correcta del pivote
    :rtype: int
    """
    pivote = arreglo[inicio]
    left = inicio + 1
    right = fin
    while True:
        while left <= right and arreglo[left] <= pivote:
            left += 1
        while arreglo[right] >= pivote and right >= left:
            right -= 1
        if right < left:
            break
        else:  # Intercambiamos los datos que no cumplieron las condiciones
            arreglo[left], arreglo[right] = arreglo[right], arreglo[left]
    # Movemos el pivote a la posición correcta
    arreglo[inicio], arreglo[right] = arreglo[right], arreglo[inicio]
    return right  # Devolvemos la posición correcta del pivote


def quick_sort(arreglo, inicio, fin):
    """
    Esta función aplica recursivamente el algoritmo Quick Sort a los subarreglos definidos por el pivote.
    :param arreglo: int[] Arreglo de enteros
    :param inicio: La posición inicial
    :param fin: La posición final
    :return: int[] Arreglo de enteros ordenado
    :rtype: int[]
    """
    if inicio < fin:
        posicion_part = __particion(arreglo, inicio, fin)
        quick_sort(arreglo, inicio, posicion_part - 1)
        quick_sort(arreglo, posicion_part + 1, fin)
    return arreglo


def __particion1(arreglo, inicio, fin, comparador) -> int:
    """
    Segundo método que permite hacer una partición de un arreglo con comparador
    :param arreglo: El arreglo a particionar
    :param inicio: El inicio del arreglo
    :param fin: El final del arreglo
    :param comparador: El comparador con el que se hará la partición del arreglo
    :return: la posición correcta del pivote
    """
    pivote = arreglo[inicio]
    left = inicio + 1
    right = fin
    while True:
        while left <= right and comparador(arreglo[left], pivote) <= 0:
            left += 1
        while comparador(arreglo[right], pivote) > 0 and right >= left:
            right -= 1
        if right < left:
            break
        else:  # Intercambiamos los datos que no cumplieron las condiciones
            arreglo[left], arreglo[right] = arreglo[right], arreglo[left]
            # Movemos el pivote a la posición correcta
    arreglo[inicio], arreglo[right] = arreglo[right], arreglo[inicio]
    return right  # Devolvemos la posición correcta del pivote


def quick_sort1(arreglo, inicio, fin, comparador):
    """
    Método quick sort de la correspondiente partición 1
    :param arreglo: El arreglo sobre el cual se efectuara el método quick sort
    :param inicio: El inicio del arreglo
    :param fin: El final del arreglo
    :param comparador: El comparador en el que se basará el ordenamiento
    :return: EL arreglo ordenado
    """
    if inicio < fin:
        posicion_part = __particion1(arreglo, inicio, fin, comparador)

        quick_sort1(arreglo, inicio, posicion_part - 1, comparador)
        quick_sort1(arreglo, posicion_part + 1, fin, comparador)
        return arreglo
