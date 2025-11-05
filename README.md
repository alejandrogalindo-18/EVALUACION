#  Evaluación Automática de Formularios y Exportación de Resultados

## Descripción General

Este proyecto permite **evaluar automáticamente formularios de respuestas** (por ejemplo, exámenes o cuestionarios) a partir de un archivo CSV con la **clave de respuestas correctas** y otro con las **respuestas de los estudiantes**.  
El sistema compara ambas fuentes de datos y genera un nuevo archivo `resultados.csv` con el puntaje obtenido por cada estudiante.

---

##  Requisitos del Proyecto

Antes de ejecutar el programa, asegúrate de tener instalado lo siguiente:

###  Requisitos de software
- **Python 3.10** o superior  
- **Git Bash** (si usas Windows)  
- Editor de texto recomendado: **Visual Studio Code**

###  Librerías necesarias
Las librerías que utiliza el proyecto son estándar de Python, por lo que no es necesario instalar dependencias adicionales.  
Sin embargo, asegúrate de tener un entorno limpio ejecutando:

```bash
python --version
```
```
Para ejecutar el codigo python "c:\Users\...\...\GitHub\EVALUACION\Evaluacion-automtica-de-formularios-y-exportacion\src\main.py"
python "c:\Users\ander\Documents\GitHub\EVALUACION\Evaluacion-automtica-de-formularios-y-exportacion\src\main.py"

```
---
### Estructura de carpetas 
---
```

│
├── src/
│   ├── main.py
│   │   # Archivo principal del proyecto.
│   │   # Se encarga de coordinar la carga de datos, la evaluación
│   │   # y la exportación de los resultados.
│   │
│   ├── modules/
│   │   ├── loader.py
│   │   │   # Contiene funciones para leer archivos CSV.
│   │   │   # Funciones principales:
│   │   │   # - cargar_csv_como_diccionario()
│   │   │   # - cargar_respuestas_csv()
│   │   │
│   │   ├── exporter.py
│   │   │   # Contiene la lógica para comparar las respuestas de los estudiantes
│   │   │   # con la clave correcta y generar el archivo 'resultados.csv'.
│   │   │
│   │   └── __init__.py
│   │       # Archivo vacío que marca esta carpeta como un paquete Python.
│   │
│   └── data/
│       ├── clave.csv
│       │   # Archivo con las respuestas correctas del examen.
│       │   # Ejemplo:
│       │   # 1,A
│       │   # 2,C
│       │
│       ├── respuestas.csv
│       │   # Archivo con las respuestas de los estudiantes.
│       │   # Ejemplo:
│       │   # nombre,1,2,3,4
│       │   # Laura,A,C,B,D
│       │   # Pedro,B,A,D,C
│       │
│       └── resultados.csv
│           # Archivo generado automáticamente con los resultados finales.
│
├── README.md
│   # Documentación del proyecto (este archivo).
│
└── .gitignore
    # Opcional: lista de archivos o carpetas a excluir del repositorio.
```
