def leer_clave(path):
    clave = {}
    with open(path, 'r') as f:
        for linea in f:
            num, resp = linea.strip().split(',')
            clave[num] = resp
    return clave

def leer_respuestas(path):
    estudiantes = []
    with open(path, 'r') as f:
        encabezado = f.readline().strip().split(',')[1:]
        for linea in f:
            partes = linea.strip().split(',')
            nombre = partes[0]
            respuestas = partes[1:]
            estudiantes.append((nombre, respuestas))
    return estudiantes, encabezado

def evaluar_respuestas(clave_path, respuestas_path, salida_path):
    clave = leer_clave(clave_path)
    estudiantes, preguntas = leer_respuestas(respuestas_path)

    with open(salida_path, 'w') as f:
        f.write("nombre,aciertos\n")
        for nombre, respuestas in estudiantes:
            aciertos = sum(1 for i, r in enumerate(respuestas) if r == clave.get(str(i+1)))
            f.write(f"{nombre},{aciertos}\n")
    print(f"✅ Archivo generado: {salida_path}")
