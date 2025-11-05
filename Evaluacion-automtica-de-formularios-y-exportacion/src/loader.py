import csv
import os

def cargar_csv_como_diccionario(path):
    """
    Lee un archivo CSV y lo convierte en un diccionario,
    usando la primera columna como clave.
    Maneja errores en caso de archivos faltantes o datos corruptos.
    """
    data = {}

    try:
        if not os.path.exists(path):
            print(f" Error: El archivo no existe -> {path}")
            return {}

        with open(path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for fila in reader:
                if len(fila) >= 2:
                    data[fila[0]] = fila[1]

        return data

    except Exception as e:
        print(f"⚠️ Error inesperado al leer {path}: {e}")
        return {}


def cargar_respuestas_csv(path):
    """
    Lee las respuestas de los estudiantes desde un CSV y las almacena
    en un diccionario con la estructura:
    { 'Nombre' : { '1': 'A', '2': 'C', ... } }
    """
    respuestas = {}

    try:
        if not os.path.exists(path):
            print(f" Error: El archivo no existe -> {path}")
            return {}

        with open(path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            encabezado = next(reader)[1:]  # Ignorar la columna del nombre

            for fila in reader:
                nombre = fila[0]
                respuestas[nombre] = {str(i+1): fila[i+1] for i in range(len(fila)-1)}

        return respuestas

    except Exception as e:
        print(f"Error al leer respuestas desde {path}: {e}")
        return {}
