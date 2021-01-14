import pandas as pd



##################
### Generators ###
##################

def gen_val_prio(LenSalas):
    yield 0
    Counter = 0
    i = 1
    while i < LenSalas+1:
        Counter += i
        i += 1
        yield Counter

########################   
### Check Properties ###
########################

def propiedad_online_numerospermitidos(row):
    if row["ONLINE"] not in [0,1]:
        Tupla = ("asignaturas", str(row["ClaveReporte"]), "ONLINE", "error", "Valor no permitido", "Valores permitidos [0, 1]")
        return Tupla
    else:
        return None


######################
### Test Functions ###
######################


############################    
### Private Functions ###
############################

def crear_clave(x):
    Clave = str(x["SEDE"])+str(x["ESCUELA"])+str(x["MODALIDAD"])+str(x["JORNADA"])+str(x["CARRERA"])+str(x["CURRICULO"])+str(x["ASIGNATURA"])+str(x["COMPONENTE"])
    return Clave

def apply_row(df, func, columns, **kargs):
    columns.append("ClaveReporte")
    tofix = df[columns].apply(func, axis=1, **kargs).dropna().values.tolist()
    return tofix

############################    
### Catalogue Validation ###
############################


def validacion_asignatura(Asignaturas, TSalas, Franjas):

    Asignaturas["ClaveReporte"] = Asignaturas.apply(crear_clave, axis=1)

    report = []

    report += apply_row(Asignaturas, propiedad_online_numerospermitidos, ["ONLINE"])

    if TSalas != None:
        print("hola")
    if Franjas != None:
        print("hola")

    clavesconerror = [clave for fichero, clave, column, tipo, msg1, msg2 in report]
    Asignaturas.loc[:, "Error"] = 0
    Asignaturas.loc[Asignaturas["ClaveReporte"].isin(clavesconerror), "Error"] = 1

    cols = Asignaturas.columns.values.tolist()
    NewCols = ["ClaveReporte", "Error"] + cols[:-2]

    Asignaturas[NewCols].to_excel("RAsignaturas.xlsx", index=False)

    return report

    
