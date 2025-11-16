"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214
    """
    ruta = r"C:\Users\ASUS\OneDrive\Documents\GitHub\David_Descriptiva\LAB-01-programacion-basica-en-python-DavidMontoya06\files\input\data.csv"
    suma = 0
    with open(ruta, "r", encoding="utf-8") as f:
        for linea in f:
            columnas = linea.strip().split()  # Divide por espacios/tabulaciones
            print(f"DEBUG: {columnas}")  # Ver qué hay en cada línea
            valor = columnas[1]  # Segunda columna (índice 1)
            suma += float(valor)

    return suma

if __name__ == "__main__":
    resultado = pregunta_01()
    print(f"La suma de la segunda columna es: {resultado}")