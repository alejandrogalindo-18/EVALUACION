import csv
import os

def evaluar_respuestas(clave, respuestas_estudiante):
    """
    Compara las respuestas de un estudiante con la clave.
    Devuelve el número de aciertos.
    """
    aciertos = 0
    for pregunta, respuesta_correcta in clave.items():
        if pregunta in respuestas_estudiante and respuestas_estudiante[pregunta].upper() == respuesta_correcta.upper():
            aciertos += 1
    return aciertos

def generar_resultados_csv(clave, respuestas):
    """
    Genera el archivo src/data/resultados.csv con los resultados finales.
    Calcula aciertos y porcentaje para cada estudiante.
    """
    resultados = {}
    ruta_salida = "src/data/resultados.csv"
    os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)

    with open(ruta_salida, mode="w", newline="", encoding="utf-8") as archivo:
        campos = ["Nombre", "Aciertos", "Porcentaje"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()

        total_preguntas = len(clave)

        for nombre, resp in respuestas.items():
            aciertos = evaluar_respuestas(clave, resp)
            porcentaje = round((aciertos / total_preguntas) * 100, 2)
            resultados[nombre] = {"Aciertos": aciertos, "Porcentaje": porcentaje}
            escritor.writerow({
                "Nombre": nombre,
                "Aciertos": aciertos,
                "Porcentaje": porcentaje
            })

    print(f"\n📊 Archivo generado: {ruta_salida}")
    return resultados
