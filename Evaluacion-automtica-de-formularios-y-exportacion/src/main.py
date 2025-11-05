from modules.loader import cargar_csv_como_diccionario, cargar_respuestas_csv
from modules.exporter import generar_resultados_csv
import os

def mostrar_encabezado():
    print("==============================================")
    print("     🧩 SISTEMA DE EVALUACIÓN AUTOMÁTICA 🧠")
    print("==============================================\n")

def verificar_archivos():
    """Verifica que existan los archivos clave y respuestas antes de continuar."""
    if not os.path.exists("src/data/clave.csv"):
        print("❌ No se encontró el archivo: src/data/clave.csv")
        exit()
    if not os.path.exists("src/data/respuestas.csv"):
        print("❌ No se encontró el archivo: src/data/respuestas.csv")
        exit()
    print("✅ Archivos verificados correctamente.\n")

def ejecutar_proceso():
    """Ejecuta el proceso completo de evaluación."""
    # 1️⃣ Verificar archivos de entrada
    verificar_archivos()

    # 2️⃣ Cargar la clave de respuestas
    clave = cargar_csv_como_diccionario("src/data/clave.csv")
    print("📘 Clave de respuestas cargada:")
    for k, v in clave.items():
        print(f"  Pregunta {k}: {v}")
    print()

    # 3️⃣ Cargar respuestas de los estudiantes
    respuestas = cargar_respuestas_csv("src/data/respuestas.csv")
    print("📗 Respuestas cargadas:")
    for nombre, resp in respuestas.items():
        print(f"  {nombre}: {resp}")
    print()

    # 4️⃣ Evaluar y generar resultados
    resultados = generar_resultados_csv(clave, respuestas)
    print("✅ Resultados generados correctamente:\n")

    for nombre, puntaje in resultados.items():
        total_preguntas = len(clave)
        porcentaje = round((puntaje / total_preguntas) * 100, 2)
        print(f"  {nombre}: {puntaje} aciertos ({porcentaje}%)")

    print("\n📂 Archivo de resultados guardado en: src/data/resultados.csv\n")

def main():
    """Función principal que ejecuta el sistema completo."""
    mostrar_encabezado()
    ejecutar_proceso()

if __name__ == "__main__":
    main()
