import pandas as pd
from utilities_darwined import report_duplicated, to_report


############################    
### Catalogue Validation ###
############################


def validacion_sedes(Cat, path="Reporte/", to_csv=False):

    Sedes = Cat["sedes"]

    if Sedes is None:
        return []


    Sedes["ClaveReporte"] = Sedes["CODIGO"]

    report = []
    TuplaDup = ("sedes", "Código", "error", "La clave está siendo usada en varias filas", "")
    report += report_duplicated(Sedes, TuplaDup)


    to_report(report, Sedes, "sedes", path, to_csv)
    return report
    
