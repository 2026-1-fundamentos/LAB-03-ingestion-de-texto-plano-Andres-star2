"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd
def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    with open("files/input/clusters_report.txt", encoding="utf-8") as file:
        datos = []
        for _ in range(4):
            next(file)

        cluster = ""
        cantidad = ""
        procentaje = " "
        palabras = ""

        for linea in file:
            if linea.strip() == "":
                continue
            
            primera = linea.strip().split()[0]

            if primera.isdigit():
                if cluster !="":
                    palabras = " ".join(palabras.split()).rstrip(".")
                    datos.append([int(cluster),int(cantidad),porcentaje,palabras])

                partes = linea.split()

                cluster = partes[0]
                cantidad = partes[1]
                porcentaje = float(partes[2].replace(",","."))
                palabras = " ".join(partes[4:])

            else:
                palabras += " "+" ".join(linea.split()).rstrip(".")
        datos.append([int(cluster),int(cantidad),porcentaje,palabras])   

        df = pd.DataFrame(datos,columns=["cluster","cantidad_de_palabras_clave","porcentaje_de_palabras_clave","principales_palabras_clave",])    

    return df
print(pregunta_01())



