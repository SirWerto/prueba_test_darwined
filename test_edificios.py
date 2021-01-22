import pandas as pd
from utilities_darwined import report_duplicated, test_de_llaves, to_report


def crear_clave(x):
    Clave = str(x["SEDE"]) + str(x["CODIGO"])
    return Clave

############################    
### Catalogue Validation ###
############################


def validacion_edificios(Cat, path="Reporte/", to_csv=False):

    Edificios = Cat["edificios"]
    Sedes = Cat["sedes"]

    if Edificios is None:
        return []


    Edificios["ClaveReporte"] = Edificios.apply(crear_clave, axis=1)

    report = []
    TuplaDup = ("edificios", "Código", "error", "La clave está siendo usada en varias filas", "")
    report += report_duplicated(Edificios, TuplaDup)

    keycolumns = []
    keylist = []
    if isinstance(Sedes, pd.DataFrame):
        ClavesSede = Sedes["CODIGO"].values.tolist()
        keycolumns.append("SEDE")
        keylist.append(ClavesSede)

    report += test_de_llaves(Edificios, "edificios", keycolumns, keylist)

    



    #SAVE AND REPORT
    to_report(report, Edificios, "edificios", path, to_csv)
    return report
    
