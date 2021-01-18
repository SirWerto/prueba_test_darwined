import pandas as pd
from utilities_darwined import report_duplicated


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

    



    if len(report) != 0:
        print("Se han encontrado " + str(len(report)) + " alertas en el catalogo de tipos de sala")
        clavesconerror = [(clave, tipo) for fichero, clave, column, tipo, msg1, msg2 in report]
        ce = pd.DataFrame(clavesconerror, columns=["ClaveReporte", "Error"])
        TiposDeSala = TiposDeSala.merge(ce, how="left", on="ClaveReporte")
        
        cols = TiposDeSala.columns.values.tolist()
        NewCols = ["ClaveReporte", "Error"] + cols[:-2]

        if to_csv:
            TiposDeSala[NewCols].to_csv(path+"RTiposDeSala.csv", index=False)
            return report
        else:
            TiposDeSala[NewCols].to_excel(path+"RTiposDeSala.xlsx", index=False)
            return report
    else:
        return []
    
