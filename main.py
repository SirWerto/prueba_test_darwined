import sys
import pandas as pd
import time
from test_asignatura import validacion_asignatura
from test_escuelas import validacion_escuelas
from test_sedes import validacion_sedes
from test_edificios import validacion_edificios
from test_tiposdesala import validacion_tiposdesala
from test_salas import validacion_salas


def try_to_read(key, Path):
    try:
        if key == "franjas":
            File = pd.read_excel(Path, sheet_name=None)
        else:
            File = pd.read_excel(Path, engine="openpyxl")
    except:
        print("No se ha podido cargar el fichero " + str(Path))
        return None
    else:
        print(str(Path) + " fichero cargado correctamente")
        return File


def main(catalogos, path="Reporte/", to_csv=False):

    start = time.time()
    reportlist = []

    print("================ CARGA =====================")
    Cat = {key:try_to_read(key, value) for key, value in catalogos.items()}

    print("================ EVALUACIÓN ================")
    reportlist += validacion_escuelas(Cat, path=path, to_csv=to_csv)
    reportlist += validacion_sedes(Cat, path=path, to_csv=to_csv)
    reportlist += validacion_edificios(Cat, path=path, to_csv=to_csv)
    reportlist += validacion_tiposdesala(Cat, path=path, to_csv=to_csv)
    reportlist += validacion_salas(Cat, path=path, to_csv=to_csv)
    reportlist += validacion_asignatura(Cat, path=path, to_csv=to_csv)

    
    end = time.time()
    print("================ RESUMEN ===================")
    print("La evaluación ha durado " + str(round(end-start, 2)) + " segundos")
    if len(reportlist) == 0:
        print("TODOS LOS CATÁLOGOS PASADOS SON CORRECTOS")
    else:
        print("SE HAN ENCONTRADO UN TOTAL DE " + str(len(reportlist)) + " ALERTAS")
        if to_csv:
            pd.DataFrame(reportlist, columns=["Catalogo", "Clave", "Columnas afectadas", "Tipo de alerta", "Msg1", "Msg2"]).to_csv(path+"Reporte.csv")
        else:
            pd.DataFrame(reportlist, columns=["Catalogo", "Clave", "Columnas afectadas", "Tipo de alerta", "Msg1", "Msg2"]).to_excel(path+"Reporte.xlsx")

    #Try to load all files


    
