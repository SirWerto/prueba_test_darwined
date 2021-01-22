import pandas as pd


def to_report(report, df, nombrecat, path, to_csv=False):
    if len(report) == 0:
        return None
    else:
        print("Se han encontrado " + str(len(report)) + " alertas en el catalogo de " + nombrecat)
        clavesconerror = [(clave, tipo) for fichero, clave, column, tipo, msg1, msg2 in report]
        ce = pd.DataFrame(clavesconerror, columns=["ClaveReporte", "Error"])
        ce.loc[:,"Error"] = pd.Categorical(ce["Error"], ["error", "aviso", "recomendacion", "info"])
        cleance = ce.sort_values("Error").drop_duplicates(subset="ClaveReporte", ignore_index=True).copy()
        df = df.merge(cleance, how="left", on="ClaveReporte")
        
        cols = df.columns.values.tolist()
        NewCols = ["ClaveReporte", "Error"] + cols[:-2]
        
        if to_csv:
            df[NewCols].to_csv(path+"R" + nombrecat + ".csv", index=False)
            return None
        else:
            df[NewCols].to_excel(path+"R" + nombrecat + ".xlsx", index=False)
            return None

def apply_row(df, func, columns, **kargs):
    owncolumns = columns.copy()
    owncolumns.append("ClaveReporte")
    try:
        tofix = df[owncolumns].apply(func, axis=1, **kargs).dropna().values.tolist()
        return tofix
    except:
        return []


def report_duplicated(df, Tupla):
    ListOfDuplicated = df.loc[df["ClaveReporte"].duplicated(), "ClaveReporte"].values.tolist()
    Reporte = [(Tupla[0], Clave, Tupla[1], Tupla[2], Tupla[3], Tupla[4]) for Clave in ListOfDuplicated]
    return Reporte

def test_de_llaves(df, nombrecat, columns=[], listoflistofkeys=[]):
    listofreport = [test_de_llave(df.copy(), column, listofkeys, nombrecat) for column, listofkeys in zip(columns, listoflistofkeys)]
    report = [alerta for reporte in listofreport for alerta in reporte]
    return report



def test_de_llave(df, column, listofkeys, nombrecat):
    try:
        ListNotIn = df.loc[~df[column].isin(listofkeys), "ClaveReporte"].values.tolist()
    except Error:
        print(Error)
        return []
    else:
        Reporte = [(nombrecat, Clave, column, "error", "Clave no encontrada", "Añada la clave o elimine esta fila") for Clave in ListNotIn]
        return Reporte


def report_null(df, mustcolumns, nombrecat):
    listofreoport = [report_null_c(df, column, nombrecat) for column in mustcolumns]
    report = [alerta for reporte in listofreport for alerta in reporte]
    return report

def report_null_c(df, column, nombrecat):
    try:
        ListNull = df.loc[df[column].isna(), "ClaveReporte"].values.tolist()
    except Error:
        print(Error)
        return []
    else:
        Reporte = [(nombrecat, Clave, column, "error", "Campo vacio", "Rellene el campo o elimine la fila") for Clave in ListNotIn]
        return Reporte


