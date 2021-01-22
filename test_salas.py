import pandas as pd
from utilities_darwined import report_duplicated, test_de_llaves, apply_row, to_report

########################   
### Check Properties ###
########################

def propiedad_capacidad_nonegativo(row):
    if row["CAPACIDAD"] < 0:
        Tupla = ("salas", str(row["ClaveReporte"]), "CAPACIDAD", "error", "Valor no permitido", "Valores permitidos números mayores que 0")
        return Tupla
    else:
        return None


def propiedad_capacidad_noncero(row):
    if row["CAPACIDAD"] == 0:
        Tupla = ("salas", str(row["ClaveReporte"]), "CAPACIDAD", "aviso", "Esta sala tiene una capacidad de 0 personas", "https://github.com/SirWerto/prueba_test_darwined/blob/master/docs/cerocapacidad.md")
        return Tupla
    else:
        return None

def propiedad_sobrecarga_nonegativo(row):
    if row["SOBRECARGA"] < 0:
        Tupla = ("salas", str(row["ClaveReporte"]), "SOBRECARGA", "error", "Valor no permitido", "Valores permitidos números mayores que 0")
        return Tupla
    else:
        return None

def propiedad_ficticio_numerospermitidos(row):
    if row["SOBRECARGA"] not in [0,1]:
        Tupla = ("salas", str(row["ClaveReporte"]), "FICTICIO", "error", "Valor no permitido", "Valores permitidos [0, 1]")
        return Tupla
    else:
        return None

def propiedad_ficticio_true(row):
    if row["SOBRECARGA"] == 1:
        Tupla = ("salas", str(row["ClaveReporte"]), "FICTICIO", "info", "Este edificio es ficticio", "")
        return Tupla
    else:
        return None






############################    
### Private Functions ###
############################

def crear_clave(x):
    Clave = str(x["SEDE"]) + str(x["EDIFICIO"])+ str(x["CODIGO"])
    return Clave

############################    
### Catalogue Validation ###
############################


def validacion_salas(Cat, path="Reporte/", to_csv=False):

    Salas = Cat["salas"]
    Sedes = Cat["sedes"]
    Edificios = Cat["edificios"]
    TSalas = Cat["tsalas"]

    if Salas is None:
        return []


    Salas["ClaveReporte"] = Salas.apply(crear_clave, axis=1)

    report = []
    TuplaDup = ("edificios", "Código", "error", "La clave está siendo usada en varias filas", "")
    report += report_duplicated(Salas, TuplaDup)



    report += apply_row(Salas, propiedad_capacidad_nonegativo, ["CAPACIDAD"])
    report += apply_row(Salas, propiedad_capacidad_noncero, ["CAPACIDAD"])
    report += apply_row(Salas, propiedad_sobrecarga_nonegativo, ["SOBRECARGA"])
    report += apply_row(Salas, propiedad_ficticio_numerospermitidos, ["FICTICIO"])
    report += apply_row(Salas, propiedad_ficticio_true, ["FICTICIO"])

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

    if isinstance(TSalas, pd.DataFrame):
        ClavesTSalas = TSalas["CODIGO"].values.tolist()
        keycolumns.append("TIPO")
        keylist.append(ClavesTSalas)

    report += test_de_llaves(Salas, "salas", keycolumns, keylist)

    

    #SAVE AND REPORT
    to_report(report, Salas, "Salas", path, to_csv)
    return report


    
