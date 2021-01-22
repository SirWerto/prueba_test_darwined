import pandas as pd
from utilities_darwined import report_duplicated, to_report


############################    
### Catalogue Validation ###
############################


def validacion_jornadas(Cat, path="Reporte/", to_csv=False):

    Jornadas = Cat["jornadas"]

    if Jornadas is None:
        return []


    Jornadas["ClaveReporte"] = Jornadas["CODIGO"]

    report = []
    TuplaDup = ("jornadas", "Código", "error", "La clave está siendo usada en varias filas", "")
    report += report_duplicated(Jornadas, TuplaDup)

    #SAVE AND REPORT
    to_report(report, Jornadas, "jornadas", path, to_csv)
    return report

    
