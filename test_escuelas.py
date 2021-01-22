import pandas as pd
from utilities_darwined import report_duplicated, to_report


############################    
### Catalogue Validation ###
############################


def validacion_escuelas(Cat, path="Reporte/", to_csv=False):

    Escuelas = Cat["escuelas"]

    if Escuelas is None:
        return []


    Escuelas["ClaveReporte"] = Escuelas["CODIGO"]

    report = []

    TuplaDup = ("escuelas", "Código", "error", "La clave está siendo usada en varias filas", "")
    report += report_duplicated(Escuelas, TuplaDup)


    #SAVE AND REPORT
    to_report(report, Escuelas, "escuelas", path, to_csv)
    return report
    
