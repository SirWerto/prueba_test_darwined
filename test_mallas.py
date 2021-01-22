import pandas as pd
from utilities_darwined import report_duplicated, test_de_llaves, apply_row, to_report


########################   
### Check Properties ###
########################




def propiedad_Not_NaN(row):
    if row.notna().all() != True:
        Tupla = ("mallas", str(row["ClaveReporte"]), "TODAS", "error", "Hay celdas vacias", "")
        return Tupla
    else:
        return None

############################    
### Private Functions ###
############################

def crear_clave(x):
    Clave = str(x["SEDE"]) + str(x["ESCUELA"])+ str(x["MODALIDAD"])+ str(x["JORNADA"])+ str(x["CARRERA"])+ str(x["CURRICULO"])+ str(x["CODIGO"])
    return Clave

############################    
### Catalogue Validation ###
############################


def validacion_mallas(Cat, path="Reporte/", to_csv=False):

    Mallas = Cat["mallas"]
    Sedes = Cat["sedes"]
    Edificios = Cat["edificios"]

    if Mallas is None:
        return []


    Mallas["ClaveReporte"] = Mallas.apply(crear_clave, axis=1)
    allcolumns = Asignaturas.columns.tolist()[:-1].copy()
    columnsmust = ['SEDE', 'ESCUELA', 'MODALIDAD', 'JORNADA', 'CARRERA', 'CURRICULO', 'CODIGO', 'NIVEL']

    report = []
    TuplaDup = ("mallas", "Código", "error", "La clave está siendo usada en varias filas", "")
    report += report_duplicated(Mallas, TuplaDup)


    report += apply_row(Mallas, propiedad_Not_NaN, columnsmust)

    report += apply_row(Mallas, propiedad_ficticio_true, ["FICTICIO"])

    keycolumns = []
    keylist = []
    if isinstance(Sedes, pd.DataFrame):
        ClavesSede = Sedes["CODIGO"].values.tolist()
        keycolumns.append("SEDE")
        keylist.append(ClavesSede)

    if isinstance(Edificios, pd.DataFrame):
        ClavesEdificios = Edificios["CODIGO"].values.tolist()
        keycolumns.append("EDIFICIO")
        keylist.append(ClavesEdificios)


    report += test_de_llaves(Mallas, "mallas", keycolumns, keylist)

    

    #SAVE AND REPORT
    to_report(report, Mallas, "Mallas", path, to_csv)
    return report
