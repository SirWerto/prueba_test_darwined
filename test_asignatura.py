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

def propiedad_usable_numerospermitidos(row):
    if row["USABLE"] not in [0,1]:
        Tupla = ("asignaturas", str(row["ClaveReporte"]), "USABLE", "error", "Valor no permitido", "Valores permitidos [0, 1]")
        return Tupla
    else:
        return None

def propiedad_usable_info_cero(row):
    if row["USABLE"] == 0:
        Tupla = ("asignaturas", str(row["ClaveReporte"]), "USABLE", "info", "Esta asignatura esta deshabilitada", "")
        return Tupla
    else:
        return None

def propiedad_num_bloques_cero_bloques(row):
    if row["NUM BLOQUES"] == 0:
        Tupla = ("asignaturas", str(row["ClaveReporte"]), "NUM BLOQUES", "aviso", "Se imparten 0 bloques de la asignatura", "https://github.com/SirWerto/prueba_test_darwined/blob/master/docs/cerosesiones.md")
        return Tupla
    else:
        return None

def propiedad_num_sesiones_cero_sesiones(row):
    if row["NUM SESIONES"] == 0:
        Tupla = ("asignaturas", str(row["ClaveReporte"]), "NUM SESIONES", "aviso", "Se imparten 0 sesiones de la asignatura", "https://github.com/SirWerto/prueba_test_darwined/blob/master/docs/cerosesiones.md")
        return Tupla
    else:
        return None

def propiedad_req_horario_numerospermitidos(row):
    if row["REQ HORARIO"] not in [0,1]:
        Tupla = ("asignaturas", str(row["ClaveReporte"]), "REQ HORARIO", "error", "Valor no permitido", "Valores permitidos [0, 1]")
        return Tupla
    else:
        return None

def propiedad_req_horario_false(row):
    if row["REQ HORARIO"] == 0:
        Tupla = ("asignaturas", str(row["ClaveReporte"]), "REQ HORARIO", "info", "Esta asignatura no requiere horario", "")
        return Tupla
    else:
        return None

def propiedad_req_sala_numerospermitidos(row):
    if row["REQ SALA"] not in [0,1]:
        Tupla = ("asignaturas", str(row["ClaveReporte"]), "REQ SALA", "error", "Valor no permitido", "Valores permitidos [0, 1]")
        return Tupla
    else:
        return None

def propiedad_req_sala_false(row):
    if row["REQ SALA"] == 0:
        Tupla = ("asignaturas", str(row["ClaveReporte"]), "REQ SALA", "info", "Esta asignatura no requiere sala", "")
        return Tupla
    else:
        return None

def propiedad_req_docente_numerospermitidos(row):
    if row["REQ DOCENTE"] not in [0,1]:
        Tupla = ("asignaturas", str(row["ClaveReporte"]), "REQ DOCENTE", "error", "Valor no permitido", "Valores permitidos [0, 1]")
        return Tupla
    else:
        return None

def propiedad_req_docente_false(row):
    if row["REQ DOCENTE"] == 0:
        Tupla = ("asignaturas", str(row["ClaveReporte"]), "REQ DOCENTE", "info", "Esta asignatura no requiere docente", "")
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


def validacion_asignatura(Asignaturas, TSalas, Franjas, path="Reporte/", to_csv=False):

    Asignaturas["ClaveReporte"] = Asignaturas.apply(crear_clave, axis=1)

    report = []


    #Obligatorias
    report += apply_row(Asignaturas, propiedad_req_horario_numerospermitidos, ["REQ HORARIO"])
    report += apply_row(Asignaturas, propiedad_req_horario_false, ["REQ HORARIO"])
    report += apply_row(Asignaturas, propiedad_req_sala_numerospermitidos, ["REQ SALA"])
    report += apply_row(Asignaturas, propiedad_req_sala_false, ["REQ SALA"])
    report += apply_row(Asignaturas, propiedad_req_docente_numerospermitidos, ["REQ DOCENTE"])
    report += apply_row(Asignaturas, propiedad_req_docente_false, ["REQ DOCENTE"])
    #Opcionales
    #Dependientes

    report += apply_row(Asignaturas, propiedad_online_numerospermitidos, ["ONLINE"])
    report += apply_row(Asignaturas, propiedad_usable_numerospermitidos, ["USABLE"])
    report += apply_row(Asignaturas, propiedad_usable_info_cero, ["USABLE"])
    report += apply_row(Asignaturas, propiedad_num_bloques_cero_bloques, ["NUM BLOQUES"])
    report += apply_row(Asignaturas, propiedad_num_sesiones_cero_sesiones, ["NUM SESIONES"])


    if len(report) != 0:
        print("Se han encontrado " + str(len(report)) + " alertas en el catalogo de asignaturas")
        clavesconerror = [(clave, tipo) for fichero, clave, column, tipo, msg1, msg2 in report]
        ce = pd.DataFrame(clavesconerror, columns=["ClaveReporte", "Error"])
        Asignaturas = Asignaturas.merge(ce, how="left", on="ClaveReporte")
        
        cols = Asignaturas.columns.values.tolist()
        NewCols = ["ClaveReporte", "Error"] + cols[:-2]
        
        if to_csv:
            Asignaturas[NewCols].to_csv(path+"RAsignaturas.csv", index=False)
            return report
        else:
            Asignaturas[NewCols].to_excel(path+"RAsignaturas.xlsx", index=False)
            return report
    else:
        return []

    
