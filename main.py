import sys
import pandas as pd
from test_asignatura import validacion_asignatura


def try_to_read(Path):
    try:
        File = pd.read_excel(Path, engine="openpyxl")
    except:
        print("No se ha podido cargar el fichero " + str(Path))
        return None
    else:
        print(str(Path) + " fichero cargado correctamente")
        return File


def main(catalogos, booltest=None):

    reportlist = []

    Cat = {key:try_to_read(value) for key, value in catalogos.items()}
    reportlist += validacion_asignatura(Cat["asignatura"], Cat["tsalas"], Cat["franjas"])
    pd.DataFrame(reportlist, columns=["Catálogo", "Clave", "Columnas afectadas", "Tipo de alerta", "Msg1", "Msg2"]).sort_values(by=["Catálogo", "Clave"], axis=1).to_excel("Reporte/Reporte.xlsx")

    #Try to load all files


    
