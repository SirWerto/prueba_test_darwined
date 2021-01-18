import pandas as pd

def report_duplicated(Escuelas):
    ListOfDuplicated = Escuelas.loc[Escuelas["ClaveReporte"].duplicated(), "ClaveReporte"].values.tolist()
    Reporte = [("escuelas", Clave, "Código", "error", "La clave está siendo usada en varias filas", "") for Clave in ListOfDuplicated]
    return Reporte

############################    
### Catalogue Validation ###
############################


def validacion_escuelas(Cat, path="Reporte/", to_csv=False):

    Escuelas = Cat["escuelas"]

    if Escuelas is None:
        return []


    Escuelas["ClaveReporte"] = Escuelas["CODIGO"]

    report = []

    report += report_duplicated(Escuelas)


    if len(report) != 0:
        print("Se han encontrado " + str(len(report)) + " alertas en el catalogo de escuelas")
        clavesconerror = [(clave, tipo) for fichero, clave, column, tipo, msg1, msg2 in report]
        ce = pd.DataFrame(clavesconerror, columns=["ClaveReporte", "Error"])
        Escuelas = Escuelas.merge(ce, how="left", on="ClaveReporte")
        
        cols = Escuelas.columns.values.tolist()
        NewCols = ["ClaveReporte", "Error"] + cols[:-2]

        if to_csv:
            Escuelas[NewCols].to_csv(path+"REscuelas.csv", index=False)
            return report
        else:
            Escuelas[NewCols].to_excel(path+"REscuelas.xlsx", index=False)
            return report
    else:
        return []
    
