import json
from pathlib import Path
#from schöpfwerk_simulator import global_variablen as g

def spielstand_speichern(name, inventar, entscheidungen, dateiname):
    #Speichert aktuellen Spielstand
    try:
        
        spielstand = {
            "name": name,
            "inventar": inventar,
            "entscheidungen": entscheidungen,
            "dateiname": dateiname
        }
        old = Path(dateiname)
        dateiname = old.with_suffix(".json")
         

        
        with open(dateiname, "w", encoding="utf-8") as datei:
            json.dump(spielstand, datei, indent=4)

        #def read_json(dateiname):
         #   with open(dateiname, "r", encoding="utf-8") as datei:
          #      d = json.load(datei)
           # return d
    except ValueError:
        print("Error")

            



















