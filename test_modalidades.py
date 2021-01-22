import pandas as pd
from utilities_darwined import report_duplicated, to_report


############################    
### Catalogue Validation ###
############################


def validacion_modalidades(Cat, path="Reporte/", to_csv=False):

    Modalidades = Cat["modalidades"]

    if Modalidades is None:
        return []


    Modalidades["ClaveReporte"] = Modalidades["CODIGO"]

    report = []
    TuplaDup = ("modalidades", "Código", "error", "La clave está siendo usada en varias filas", "")
    report += report_duplicated(Modalidades, TuplaDup)


    #SAVE AND REPORT
    to_report(report, Escuelas, "escuelas", path, to_csv)
    return report
    
