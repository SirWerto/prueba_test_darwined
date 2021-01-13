import sys
import pandas as pd
#from asignatura import validacion_asignatura


def try_to_read(Path):
    try:
        File = pd.read_excel(Path, engine="openpyxl")
    except:
        print("No se ha podido cargar el fichero " + str(Path))
    else:
        print(str(Path) + " fichero cargado correctamente")
        return File


def main():
    if len(sys.argv) != 3:
        exit("not enoght arguments")

    Files = sys.argv[1]
    BoolTest = sys.argv[2]

    Asignatura = try_to_read(Files["asignatura"])
    print(Asignatura)

    #Try to load all files

if __name__ == "__main__":
    main()

    
