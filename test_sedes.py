import pandas as pd

def report_duplicated(Sedes):
    ListOfDuplicated = Sedes.loc[Sedes["ClaveReporte"].duplicated(), "ClaveReporte"].values.tolist()
    Reporte = [("sedes", Clave, "Código", "error", "La clave está siendo usada en varias filas", "") for Clave in ListOfDuplicated]
    return Reporte

############################    
### Catalogue Validation ###
############################


def validacion_sedes(Cat, path="Reporte/", to_csv=False):

    Sedes = Cat["sedes"]

    if Sedes is None:
        return []


    Sedes["ClaveReporte"] = Sedes["CODIGO"]

    report = []

    report += report_duplicated(Sedes)


    if len(report) != 0:
        print("Se han encontrado " + str(len(report)) + " alertas en el catalogo de sedes")
        clavesconerror = [(clave, tipo) for fichero, clave, column, tipo, msg1, msg2 in report]
        ce = pd.DataFrame(clavesconerror, columns=["ClaveReporte", "Error"])
        Sedes = Sedes.merge(ce, how="left", on="ClaveReporte")
        
        cols = Sedes.columns.values.tolist()
        NewCols = ["ClaveReporte", "Error"] + cols[:-2]

        if to_csv:
            Sedes[NewCols].to_csv(path+"RSedes.csv", index=False)
            return report
        else:
            Sedes[NewCols].to_excel(path+"RSedes.xlsx", index=False)
            return report
    else:
        return []
    
