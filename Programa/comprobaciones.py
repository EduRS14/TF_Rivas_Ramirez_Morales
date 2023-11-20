import os

# Nombre del archivo que deseamos comprobar
def comprobacion():
    nombre_archivo = "grafo.png"
    condicion = 0
    # Obtenemos la ruta del directorio actual
    directorio_actual = os.getcwd()

    # Comprobamos si el archivo existe en el directorio actual
    ruta_completa = os.path.join(directorio_actual, nombre_archivo)

    if os.path.isfile(ruta_completa):
        condicion = 1
    else:
        condicion = 0
    
    return condicion