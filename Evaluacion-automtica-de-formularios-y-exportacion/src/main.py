import os
import sys

# Asegurar que el directorio raíz del proyecto esté en sys.path para poder
# importar el paquete `modules` desde este script cuando se ejecute como
# "python src/main.py".
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from loader import cargar_csv_como_diccionario, cargar_respuestas_csv
from modules.evaluador import generar_resultados_csv

def mostrar_encabezado():
    print("==============================================")
    print("    SISTEMA DE EVALUACIÓN AUTOMÁTICA ")
    print("==============================================\n")

def verificar_archivos():
    """Verifica que existan los archivos clave y respuestas antes de continuar."""
    data_dir = os.path.join(os.path.dirname(__file__), "data")
    clave_path = os.path.join(data_dir, "clave.csv")
    respuestas_path = os.path.join(data_dir, "respuestas.csv")

    if not os.path.exists(clave_path):
        print(f" No se encontró el archivo: {clave_path}")
        exit(1)
    if not os.path.exists(respuestas_path):
        print(f" No se encontró el archivo: {respuestas_path}")
        exit(1)
    print("✅ Archivos verificados correctamente.\n")

def ejecutar_proceso():
    """Ejecuta el proceso completo de evaluación."""
    # 1️Verificar archivos de entrada
    verificar_archivos()

    #  Cargar la clave de respuestas
    data_dir = os.path.join(os.path.dirname(__file__), "data")
    clave_path = os.path.join(data_dir, "clave.csv")
    respuestas_path = os.path.join(data_dir, "respuestas.csv")

    clave = cargar_csv_como_diccionario(clave_path)
    print(" Clave de respuestas cargada:")
    for k, v in clave.items():
        print(f"  Pregunta {k}: {v}")
    print()

    # Cargar respuestas de los estudiantes
    respuestas = cargar_respuestas_csv(respuestas_path)
    print(" Respuestas cargadas:")
    for nombre, resp in respuestas.items():
        print(f"  {nombre}: {resp}")
    print()

    # 4️ Evaluar y generar resultados
    resultados = generar_resultados_csv(clave, respuestas)
    print(" Resultados generados correctamente:\n")

    total_preguntas = len(clave)
    # `generar_resultados_csv` devuelve un dict con la siguiente forma:
    # { nombre: {"Aciertos": int, "Porcentaje": float }, ... }
    for nombre, datos in resultados.items():
        if isinstance(datos, dict):
            aciertos = datos.get("Aciertos", 0)
            porcentaje = datos.get("Porcentaje", round((aciertos / total_preguntas) * 100, 2) if total_preguntas else 0)
        else:
            # Compatibilidad por si la función devolviera solo el número de aciertos
            aciertos = datos
            porcentaje = round((aciertos / total_preguntas) * 100, 2) if total_preguntas else 0

        print(f"  {nombre}: {aciertos} aciertos ({porcentaje}%)")

    print("\n Archivo de resultados guardado en: src/data/resultados.csv\n")

def main():
    """Función principal que ejecuta el sistema completo."""
    mostrar_encabezado()
    ejecutar_proceso()

if __name__ == "__main__":
    main()
