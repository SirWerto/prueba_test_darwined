import pandas as pd
from utilities_darwined import report_duplicated, test_de_llaves, apply_row, to_report

########################   
### Check Properties ###
########################



############################    
### Private Functions ###
############################

def crear_clave(x):
    Clave = str(x["SEDE"]) + str(x["ESCUELA"])+ str(x["MODALIDAD"]) + str(x["JORNADA"]) + str(x["CODIGO"])
    return Clave

############################    
### Catalogue Validation ###
############################


def validacion_carreras(Cat, path="Reporte/", to_csv=False):

    Carreras = Cat["carreras"]
    Sedes = Cat["sedes"]
    Escuelas = Cat["escuelas"]
    Modalidades = Cat["modalidades"]
    Jornadas = Cat["jornadas"]
    Periodos = Cat["periodos"]

    if Carreras is None:
        return []


    Carreras["ClaveReporte"] = Carreras.apply(crear_clave, axis=1)

    report = []
    TuplaDup = ("carreras", "Código", "error", "La clave está siendo usada en varias filas", "")
    report += report_duplicated(Carreras, TuplaDup)

    keycolumns = []
    keylist = []
    if isinstance(Sedes, pd.DataFrame):
        ClavesSede = Sedes["CODIGO"].values.tolist()
        keycolumns.append("SEDE")
        keylist.append(ClavesSede)

    if isinstance(Escuelas, pd.DataFrame):
        ClavesEscuela = Escuelas["CODIGO"].values.tolist()
        keycolumns.append("ESCUELA")
        keylist.append(ClavesEscuela)

    if isinstance(Modalidades, pd.DataFrame):
        ClavesModalidad = Modalidades["CODIGO"].values.tolist()
        keycolumns.append("MODALIDAD")
        keylist.append(ClavesModalidad)

    if isinstance(Jornadas, pd.DataFrame):
        ClavesJornada = Jornadas["CODIGO"].values.tolist()
        keycolumns.append("JORNADA")
        keylist.append(ClavesJornada)

    if isinstance(Periodos, pd.DataFrame):
        ClavesPeriodo = Periodos["CODIGO"].values.tolist()
        keycolumns.append("PERIODO")
        keylist.append(ClavesPeriodo)

    report += test_de_llaves(Carreras, "carreras", keycolumns, keylist)

    

    #SAVE AND REPORT
    to_report(report, Carreras, "carreras", path, to_csv)
    return report


    
