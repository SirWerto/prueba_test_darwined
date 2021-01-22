# -*- coding: ISO-8859-1 -*-
import pandas as pd
from utilities_darwined import report_duplicated, test_de_llaves, apply_row, to_report

########################   
### Check Properties ###
########################

def propiedad_MaxCrePeriodo_nonegativo(row):
    if row["MAX CREDITOS/PERIODO"] < 0:
        Tupla = ("curriculos", str(row["ClaveReporte"]), "MAX CREDITOS/PERIODO", "error", "Valor no permitido", "Valores permitidos números mayores que 0")
        return Tupla
    else:
        return None

def propiedad_MaxCreAno_nonegativo(row):
    if row["MAX CREDITOS/A�O"] < 0:
        Tupla = ("curriculos", str(row["ClaveReporte"]), "MAX CREDITOS/A�O", "error", "Valor no permitido", "Valores permitidos números mayores que 0")
        return Tupla
    else:
        return None

def propiedad_MaxCurPeriodo_nonegativo(row):
    if row["MAX CURSOS/PERIODO"] < 0:
        Tupla = ("curriculos", str(row["ClaveReporte"]), "MAX CURSOS/PERIODO", "error", "Valor no permitido", "Valores permitidos números mayores que 0")
        return Tupla
    else:
        return None

def propiedad_MaxCurAno_nonegativo(row):
    if row["MAX CURSOS/A�O"] < 0:
        Tupla = ("curriculos", str(row["ClaveReporte"]), "MAX CURSOS/A�O", "error", "Valor no permitido", "Valores permitidos números mayores que 0")
        return Tupla
    else:
        return None

def propiedad_MaxCrePeriodo_cero(row):
    if row["MAX CREDITOS/PERIODO"] == 0:
        Tupla = ("curriculos", str(row["ClaveReporte"]), "MAX CREDITOS/PERIODO", "aviso", "Se imparten un m�ximo de 0 creditos este periodo", "ENLACE A CEROCRED.MD")
        return Tupla
    else:
        return None

def propiedad_MaxCreAno_cero(row):
    if row["MAX CREDITOS/A�O"] == 0:
        Tupla = ("curriculos", str(row["ClaveReporte"]), "MAX CREDITOS/A�O", "aviso", "Se imparten un m�ximo de 0 creditos este a�o", "ENLACE A CEROCRED.MD")
        return Tupla
    else:
        return None

def propiedad_MaxCurPeriodo_cero(row):
    if row["MAX CURSOS/PERIODO"] == 0:
        Tupla = ("curriculos", str(row["ClaveReporte"]), "MAX CURSOS/PERIODO", "aviso", "Se imparten un m�ximo de 0 cursos este perido", "ENLACE A CEROCRED.MD")
        return Tupla
    else:
        return None

def propiedad_MaxCurAno_cero(row):
    if row["MAX CURSOS/A�O"] == 0:
        Tupla = ("curriculos", str(row["ClaveReporte"]), "MAX CURSOS/A�O", "aviso", "Se imparten un max�mo de 0 cursos este a�o", "ENLACE A CEROCRED.MD")
        return Tupla
    else:
        return None





############################    
### Private Functions ###
############################

def crear_clave(x):
    Clave = str(x["SEDE"]) + str(x["ESCUELA"])+ str(x["MODALIDAD"]) + str(x["JORNADA"]) + str(x["CARRERA"]) + str(x["CURRICULO"])
    return Clave

############################    
### Catalogue Validation ###
############################


def validacion_curriculos(Cat, path="Reporte/", to_csv=False):

    Curriculos = Cat["curr"]
    Sedes = Cat["sedes"]
    Escuelas = Cat["escuelas"]
    Modalidades = Cat["modalidades"]
    Jornadas = Cat["jornadas"]
    Carreras = Cat["carreras"]

    if Curriculos is None:
        return []


    Curriculos["ClaveReporte"] = Curriculos.apply(crear_clave, axis=1)

    report = []
    TuplaDup = ("curriculos", "Código", "error", "La clave está siendo usada en varias filas", "")
    report += report_duplicated(Curriculos, TuplaDup)



    report += apply_row(Curriculos, propiedad_MaxCrePeriodo_nonegativo, ["MAX CREDITOS/PERIODO"])
    report += apply_row(Curriculos, propiedad_MaxCrePeriodo_cero, ["MAX CREDITOS/PERIODO"])
    report += apply_row(Curriculos, propiedad_MaxCreAno_nonegativo, ["MAX CREDITOS/A�O"])
    report += apply_row(Curriculos, propiedad_MaxCreAno_cero, ["MAX CREDITOS/A�O"])
    report += apply_row(Curriculos, propiedad_MaxCurPeriodo_nonegativo, ["MAX CURSOS/PERIODO"])
    report += apply_row(Curriculos, propiedad_MaxCurPeriodo_cero, ["MAX CURSOS/PERIODO"])
    report += apply_row(Curriculos, propiedad_MaxCurAno_nonegativo, ["MAX CURSOS/A�O"])
    report += apply_row(Curriculos, propiedad_MaxCurAno_cero, ["MAX CURSOS/A�O"])

    keycolumns = []
    keylist = []
    if isinstance(Sedes, pd.DataFrame):
        ClavesSede = Sedes["CODIGO"].values.tolist()
        keycolumns.append("SEDE")
        keylist.append(ClavesSede)

    if isinstance(Escuelas, pd.DataFrame):
        ClavesEscuelas = Escuelas["CODIGO"].values.tolist()
        keycolumns.append("ESCUELA")
        keylist.append(ClavesEscuelas)

    if isinstance(Modalidadess, pd.DataFrame):
        ClavesModalidad = Modalidades["CODIGO"].values.tolist()
        keycolumns.append("MODALIDAD")
        keylist.append(ClavesModalidad)

    if isinstance(Jornadas, pd.DataFrame):
        ClavesJornadas = Jornadas["CODIGO"].values.tolist()
        keycolumns.append("JORNADA")
        keylist.append(ClavesJornadas)

    if isinstance(Carreras, pd.DataFrame):
        ClavesCarrera = Carreras["CODIGO"].values.tolist()
        keycolumns.append("CARRERA")
        keylist.append(ClavesCarrera)

    if isinstance(Tsalas, pd.DataFrame):
        ClavesSede = Tsalas["CODIGO"].values.tolist()
        keycolumns.append("TIPO")
        keylist.append(ClavesSede)

    report += test_de_llaves(Curriculos, "curriculos", keycolumns, keylist)

    

    #SAVE AND REPORT
    to_report(report, Curriculos, "curriculos", path, to_csv)
    return report


    
