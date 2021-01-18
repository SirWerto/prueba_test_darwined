import pandas as pd
from utilities_darwined import report_duplicated, test_de_llaves


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

    



    if len(report) != 0:
        print("Se han encontrado " + str(len(report)) + " alertas en el catalogo de edificios")
        clavesconerror = [(clave, tipo) for fichero, clave, column, tipo, msg1, msg2 in report]
        ce = pd.DataFrame(clavesconerror, columns=["ClaveReporte", "Error"])
        Edificios = Edificios.merge(ce, how="left", on="ClaveReporte")
        
        cols = Edificios.columns.values.tolist()
        NewCols = ["ClaveReporte", "Error"] + cols[:-2]

        if to_csv:
            Edificios[NewCols].to_csv(path+"REdificios.csv", index=False)
            return report
        else:
            Edificios[NewCols].to_excel(path+"REdificios.xlsx", index=False)
            return report
    else:
        return []
    
