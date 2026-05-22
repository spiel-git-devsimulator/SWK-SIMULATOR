import turtle, math, shutil, textwrap, random, math, json 
from colorama import Fore, init
from schöpfwerk_simulator.story.prolog import prolog_start
#from schöpfwerk_simulator.story.hauptteil import hauptteil1
#from schöpfwerk_simulator.texte import texte, text_formatieren
from schöpfwerk_simulator.story.user import user
from schöpfwerk_simulator.story.shop import einkauf
from schöpfwerk_simulator.speichern import spielstand_speichern
from schöpfwerk_simulator import global_variablen as g #importiert alle globalen variabeln
from schöpfwerk_simulator.story.ASCII_ART import SWKSIMULATOR

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
 
spielstand_name = input("Wie möchtest den Spielstand nennen: ")
g.spielstand_name = spielstand_name
#print(spielstand_speichern())
#ende = "Schlecht"
#g.player_entscheidungen["Ende"] = ende

spielstand_speichern(
    g.player,
    g.player_inventar,
    g.player_entscheidungen,
    spielstand_name
    )

start()