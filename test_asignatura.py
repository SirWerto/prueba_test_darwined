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

def propiedad_online_InfoUno(row):
    if row["ONLINE"] == 1:
        Tupla = ("asignaturas", str(row["ClaveReporte"]), "ONLINE", "info", "Esta asignatura se imparte online", "")
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

def propiedad_PrioridadDeAula_NumerosPermitidos(row, tiposdesalas, allow_list):
    if row[tiposdesalas].sum() not in allow_list:
        Tupla = ("asignaturas", str(row["ClaveReporte"]), "Prioridades de sala", "error", "Números no permitidos", "Tienen que ser números consecutivos [1,2,3...]")
        return Tupla
    else:
        return None

def propiedad_PrioridadDeAula_NumerosNoConsecutivos(row, tiposdesalas):   
    Setrow = set(row[tiposdesalas].values)
    LS = len(Setrow)
    Set = set(range(LS))
    if Setrow.difference(Set) != set():
        Tupla = ("asignaturas", str(row["ClaveReporte"]), "Prioridades de sala", "error", "Prioridades no consecutivas", "Tienen que ser números consecutivos [1,2,3...]")
        return Tupla
    else:
        return None

def propiedad_PrioridadDeAula_CeroPrioridades(row, tiposdesalas):
    if row[tiposdesalas].sum() == 0:
        Tupla = ("asignaturas", str(row["ClaveReporte"]), "Prioridades de sala", "aviso", "No se ha definido ninguna prioridad", "https://github.com/SirWerto/prueba_test_darwined/blob/master/docs/ceroprioridades.md")
        return Tupla
    else:
        return None

def propiedad_Franjas_NumerosPermitidos(row, franjas):
    Setrow = set(row[franjas].values)
    if Setrow.difference(set([0,1])) != set():
        Tupla = ("asignaturas", str(row["ClaveReporte"]), "Franjas", "error", "Números no permitidos", "Valores permitidos [0, 1]")
        return Tupla
    else:
        return None

def propiedad_Franjas_CeroFranjas(row, franjas):
    if row[franjas].sum() == 0:
        Tupla = ("asignaturas", str(row["ClaveReporte"]), "Franjas", "aviso", "No se ha definido ninguna franja", "https://github.com/SirWerto/prueba_test_darwined/blob/master/docs/cerofranjas.md")
        return Tupla
    else:
        return None

def propiedad_SesionesAlineadas_NumerosPermitidos(row):
    if row["SESIONES ALINEADAS"] not in [0,1]:
        Tupla = ("asignaturas", str(row["ClaveReporte"]), "SESIONES ALINEADAS", "error", "Números no permitidos", "Valores permitidos [0, 1]")
        return Tupla
    else:
        return None

def propiedad_SesionesAlineadas_InfoUno(row):
    if row["SESIONES ALINEADAS"] == 1:
        Tupla = ("asignaturas", str(row["ClaveReporte"]), "SESIONES ALINEADAS", "info", "Esta asignatura se imparte alineada", "")
        return Tupla
    else:
        return None

def propiedad_Not_NaN(row):
    if row.notna().all() != True:
        Tupla = ("asignaturas", str(row["ClaveReporte"]), "TODAS", "error", "Hay celdas vacias", "")
        return Tupla
    else:
        return None

def propiedad_VacantesMax_NumerosPermitidos(row):
    if not isinstance(row['VAC MAX'], (int, float)) or row['VAC MAX'] < 0:
        Tupla = ("asignaturas", str(row["ClaveReporte"]), "VAC MAX", "error", "Números no permitidos", "Los valores permitidos son enteros mayores que 0")
        return Tupla
    else:
        return None

def propiedad_VacantesMax_MaxCero(row):
    if row['VAC MAX'] == 0:
        Tupla = ("asignaturas", str(row["ClaveReporte"]), "VAC MAX", "aviso", "No hay vacantes para esta asignatura", "https://github.com/SirWerto/prueba_test_darwined/blob/master/docs/cerovac.md")
        return Tupla
    else:
        return None

def propiedad_VacantesMin_NumerosPermitidos(row):
    if not isinstance(row['VAC MIN'], (int, float)) or row['VAC MIN'] < 0:
        Tupla = ("asignaturas", str(row["ClaveReporte"]), "VAC MIN", "error", "Números no permitidos", "Los valores permitidos son enteros mayores que 0")
        return Tupla
    else:
        return None

def propiedad_VacantesOpt_NumerosPermitidos(row):
    if not isinstance(row['VAC OPT'], (int, float)) or row['VAC OPT'] < 0:
        Tupla = ("asignaturas", str(row["ClaveReporte"]), "VAC OPT", "error", "Números no permitidos", "Los valores permitidos son enteros mayores que 0")
        return Tupla
    else:
        return None

def propiedad_VacantesOpt_MaxCero(row):
    if row['VAC OPT'] == 0:
        Tupla = ("asignaturas", str(row["ClaveReporte"]), "VAC OPT", "aviso", "Las vacantes óptimas para esta asignatura son de 0", "https://github.com/SirWerto/prueba_test_darwined/blob/master/docs/cerovac.md")
        return Tupla
    else:
        return None

def propiedad_Vacantes_MaxOpt(row):
    if row['VAC OPT'] > row['VAC MAX']:
        Tupla = ("asignaturas", str(row["ClaveReporte"]), "VAC OPT and MAX", "error", "Las vacantes óptimas son mayores que las máximas", "opt < max")
        return Tupla
    else:
        return None

def propiedad_Vacantes_MaxMin(row):
    if row['VAC MIN'] > row['VAC MAX']:
        Tupla = ("asignaturas", str(row["ClaveReporte"]), "VAC MIN and MAX", "error", "Las vacantes mínimas son mayores que las máximas", "min < max")
        return Tupla
    else:
        return None

def propiedad_Vacantes_OptMin(row):
    if row['VAC MIN'] > row['VAC OPT']:
        Tupla = ("asignaturas", str(row["ClaveReporte"]), "VAC MIN and OPT", "error", "Las vacantes mínimas son mayores que las óptimas", "min < opt")
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
    owncolumns = columns.copy()
    owncolumns.append("ClaveReporte")
    try:
        tofix = df[owncolumns].apply(func, axis=1, **kargs).dropna().values.tolist()
        return tofix
    except:
        return []

############################    
### Catalogue Validation ###
############################


def validacion_asignatura(Asignaturas, TSalas, Franjas, path="Reporte/", to_csv=False):

    Asignaturas["ClaveReporte"] = Asignaturas.apply(crear_clave, axis=1, result_type='reduce')
    allcolumns = Asignaturas.columns.tolist()[:-1].copy()

    columnsmust = ['SEDE', 'ESCUELA', 'MODALIDAD', 'JORNADA', 'CARRERA', 'CURRICULO', 'ASIGNATURA', 'NOMBRE', 'COMPONENTE' \
                   , 'TIPO', 'NUM BLOQUES', 'NUM SESIONES', 'VAC MAX', 'REQ HORARIO', 'REQ SALA', 'REQ DOCENTE', 'ONLINE' \
                   , 'SESIONES ALINEADAS', 'USABLE']
    report = []


    #Obligatorias
    report += apply_row(Asignaturas, propiedad_Not_NaN, columnsmust)
    report += apply_row(Asignaturas, propiedad_num_bloques_cero_bloques, ["NUM BLOQUES"])
    report += apply_row(Asignaturas, propiedad_num_sesiones_cero_sesiones, ["NUM SESIONES"])
    report += apply_row(Asignaturas, propiedad_VacantesMax_NumerosPermitidos, ["VAC MAX"])
    report += apply_row(Asignaturas, propiedad_VacantesMax_MaxCero, ["VAC MAX"])
    report += apply_row(Asignaturas, propiedad_req_horario_numerospermitidos, ["REQ HORARIO"])
    report += apply_row(Asignaturas, propiedad_req_horario_false, ["REQ HORARIO"])
    report += apply_row(Asignaturas, propiedad_req_sala_numerospermitidos, ["REQ SALA"])
    report += apply_row(Asignaturas, propiedad_req_sala_false, ["REQ SALA"])
    report += apply_row(Asignaturas, propiedad_req_docente_numerospermitidos, ["REQ DOCENTE"])
    report += apply_row(Asignaturas, propiedad_req_docente_false, ["REQ DOCENTE"])
    report += apply_row(Asignaturas, propiedad_online_numerospermitidos, ["ONLINE"])
    report += apply_row(Asignaturas, propiedad_online_InfoUno, ["ONLINE"])
    report += apply_row(Asignaturas, propiedad_SesionesAlineadas_NumerosPermitidos, ["SESIONES ALINEADAS"])
    report += apply_row(Asignaturas, propiedad_SesionesAlineadas_InfoUno, ["SESIONES ALINEADAS"])
    report += apply_row(Asignaturas, propiedad_usable_numerospermitidos, ["USABLE"])
    report += apply_row(Asignaturas, propiedad_usable_info_cero, ["USABLE"])


    #Opcionales
    report += apply_row(Asignaturas[Asignaturas['VAC MIN'].notna()], propiedad_VacantesMin_NumerosPermitidos, ["VAC MIN"])
    report += apply_row(Asignaturas[Asignaturas['VAC OPT'].notna()], propiedad_VacantesOpt_NumerosPermitidos, ["VAC OPT"])
    report += apply_row(Asignaturas[Asignaturas['VAC OPT'].notna()], propiedad_VacantesOpt_MaxCero, ["VAC OPT"])
    report += apply_row(Asignaturas[Asignaturas['VAC OPT'].notna()], propiedad_Vacantes_MaxOpt, ["VAC OPT", "VAC MAX"])
    report += apply_row(Asignaturas[(Asignaturas['VAC OPT'].notna()) & (Asignaturas['VAC MIN'].notna())], propiedad_Vacantes_OptMin, ["VAC OPT", "VAC MIN"])
    report += apply_row(Asignaturas[Asignaturas['VAC MIN'].notna()], propiedad_Vacantes_MaxMin, ["VAC MIN", "VAC MAX"])


    #Dependientes

    if isinstance(TSalas, pd.DataFrame):
        TSalaslist = TSalas["CODIGO"].values.tolist()
        LenSalas = len(TSalaslist)
        Columns = TSalaslist.copy()
        report += apply_row(Asignaturas, propiedad_PrioridadDeAula_NumerosPermitidos, Columns, tiposdesalas=TSalaslist, allow_list=list(gen_val_prio(LenSalas)))
        report += apply_row(Asignaturas, propiedad_PrioridadDeAula_NumerosNoConsecutivos, Columns, tiposdesalas=TSalaslist)
        report += apply_row(Asignaturas, propiedad_PrioridadDeAula_CeroPrioridades, Columns, tiposdesalas=TSalaslist)

    if isinstance(Franjas, dict):
        TFranjas = list(Franjas.keys())
        Columns = TFranjas.copy()
        report += apply_row(Asignaturas, propiedad_Franjas_NumerosPermitidos , Columns, franjas=TFranjas)
        report += apply_row(Asignaturas, propiedad_Franjas_CeroFranjas, Columns, franjas=TFranjas)



    #SAVE AND REPORT
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

    
