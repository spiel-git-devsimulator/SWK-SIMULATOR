import json
from pathlib import Path
#from schöpfwerk_simulator import global_variablen as g

def spielstand_speichern(name, inventar, entscheidungen, dateiname):
    #Speichert aktuellen Spielstand
    try:
        
        spielstand = {
            "name": name,
            "inventar": inventar,
            "entscheidungen": entscheidungen,   #speichert in Form von Dictionary
            "dateiname": dateiname
        }
        old = Path(dateiname)
        dateiname = old.with_suffix(".json")      #kontrolliert/ändert Dateiendung auf .json
                 
        with open(dateiname, "w", encoding="utf-8") as datei:  #macht ein json file
            json.dump(spielstand, datei, indent=4)
    except ValueError:
        print("Error")

def read_json(dateiname):
    with open(dateiname, "r", encoding="utf-8") as datei:   #json file lesen
        d = json.load(datei)
        print(d)
            



















