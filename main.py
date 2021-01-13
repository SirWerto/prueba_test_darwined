import sys
import pandas as pd


def try_to_read(Path):
    try:
        File = pd.read_excel(Path, engine="openpyxl")
    except:
        print("No se ha podido cargar el fichero " + str(Path))
    else:
        print(str(Path) + " fichero cargado correctamente")
        return File


if __main__ == "__main__":
    if len(sys.argv) != 3:
        exit("not enoght arguments")

    Files = sys.argv[1]
    BoolTest = sys.argv[2]

    #Try to load all files

    
