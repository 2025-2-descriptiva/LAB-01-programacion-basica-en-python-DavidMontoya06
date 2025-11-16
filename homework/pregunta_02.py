"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        data = {}
        for line in file:
            parts = line.strip().split("\t")
            key = parts[0]
            if key not in data:
                data[key] = 1  # Initialize count
            else:
                data[key] += 1  # Increment count

        result = sorted(data.items())
    return result