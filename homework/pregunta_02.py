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
    ruta = r"C:\Users\ASUS\OneDrive\Documents\GitHub\David_Descriptiva\LAB-01-programacion-basica-en-python-DavidMontoya06\files\input\data.csv"
    conteo = {}
    
    with open(ruta, "r", encoding="utf-8") as f:
        for linea in f:
            columnas = linea.strip().split()  # Dividir por espacios
            letra = columnas[0]  # Primera columna
            conteo[letra] = conteo.get(letra, 0) + 1
    
    # Ordenar alfabéticamente y convertir a lista de tuplas
    resultado = sorted(conteo.items())
    return resultado


if __name__ == "__main__":
    resultado = pregunta_02()
    print(resultado)
