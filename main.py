import math, shutil, textwrap, random, json 
from colorama import Fore, init
from schöpfwerk_simulator.story.prolog import prolog_start
#from schöpfwerk_simulator.story.hauptteil import hauptteil1
#from schöpfwerk_simulator.texte import texte, text_formatieren
from schöpfwerk_simulator.story.user import user
from schöpfwerk_simulator.story.shop import einkauf
from schöpfwerk_simulator.speichern import spielstand_speichern, read_json
from schöpfwerk_simulator import global_variablen as g #importiert alle globalen variabeln
from schöpfwerk_simulator.story.ASCII_ART import SWKSIMULATOR
from pathlib import Path
from schöpfwerk_simulator.story.Zahlenkontrolle import zahlenkontrolle
import sys

while True:
    
    g.player = None
    g.player_inventar = []
    g.player_entscheidungen = {}

    SWKSIMULATOR()
    init(autoreset=True) #ändert nachdem ausführen von Fore+Farbe die Farbe wieder auf Standart
    def start():
        #Benutzerinput Kontrolle
        def tot():
            tot = Fore.RED+"Du bist tot. Ende" #hier wird der Text rot angezeigt.
            return tot
        
        #minigame()
        #einkauf()
        name = user()
        g.player = name
        #name = user() #Der Name wird als name gespeichert und dieser wird prolog_start mitgegeben
        prolog_start(name)
        #hauptteil1()
    while True:
        spielstand_name = input("Wie möchtest den Spielstand nennen: ").strip()
        if spielstand_name:
            break
        print("Du musst einen Spielstand eingeben.")
    g.spielstand_name = spielstand_name
    #print(spielstand_speichern())
    #ende = "Schlecht"
    #g.player_entscheidungen["Ende"] = ende

    #spielstand_speichern(
    #    g.player,
    #    g.player_inventar,
    #    g.player_entscheidungen,
    #    spielstand_name
    #    )
    old = Path(g.spielstand_name)
    dateiname = old.with_suffix(".json")
    start()

    ergebnisausgabe = zahlenkontrolle("""Möchtest du
                                    1) das letzte Ergebnis sehen?
                                    2) es nicht sehen?:  """)
    if ergebnisausgabe == 1:
        read_json(dateiname)
        again = zahlenkontrolle("Möchtest du nochmals spielen? (1=Ja, 2=Nein): ")
        if again ==2:
            break
    elif ergebnisausgabe == 2:
        again = zahlenkontrolle("Möchtest du nochmals spielen? (1=Ja, 2=Nein): ")
        if again ==2:
            break
    else: 
        sys.exit()
