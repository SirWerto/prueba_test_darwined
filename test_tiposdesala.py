import pandas as pd
from utilities_darwined import report_duplicated, to_report


############################    
### Catalogue Validation ###
############################


def validacion_tiposdesala(Cat, path="Reporte/", to_csv=False):

    TiposDeSala = Cat["tsalas"]

    if TiposDeSala is None:
        return []


    TiposDeSala["ClaveReporte"] = TiposDeSala["CODIGO"]

    report = []
    TuplaDup = ("tiposdesalas", "Código", "error", "La clave está siendo usada en varias filas", "")
    report += report_duplicated(TiposDeSala, TuplaDup)

    keycolumns = []
    keylist = []

    
    #SAVE AND REPORT
    to_report(report, TiposDeSala, "tipos de sala", path, to_csv)
    return report
    
