import pandas as pd



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


