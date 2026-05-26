from schöpfwerk_simulator.story.hauptteil import hauptteil1
from schöpfwerk_simulator.story.user import user
from schöpfwerk_simulator.story.Zahlenkontrolle import zahlenkontrolle
from schöpfwerk_simulator.texte import text_formatieren, texte
from schöpfwerk_simulator.speichern import spielstand_speichern
from schöpfwerk_simulator import global_variablen as g
from colorama import Fore, init
from schöpfwerk_simulator.story.ASCII_ART import SWKSchule
init(autoreset=True)
def tot():
    x = Fore.RED+"Du bist tot. Ende"
    return x

def prolog_start(name):
    print("Info: SWK = Schöpfwerk ")
    print(f"""{name},du stehst vor der Volkkschule Am Schöpfwerk und siehst
           wie ein Typ geschlagen wird.""")
    SWKSchule()
    # helfen = int(input(zahlenkontrolle("Willst du ihm helfen(1=JA/2=NEIN): ")))
    helfen = zahlenkontrolle("Willst du ihm helfen(1=JA/2=NEIN): ")
    if helfen == 1:
        print("Du entscheidest dich ihm zu helfen")
        gewalt = zahlenkontrolle("""Möchtest du seine Schläger schlagen, 
                                 oder möchtest du sie überzeugen ihn loszulassen?(1=Gewalt,2=Friedlich): """)
        if gewalt == 1:
            print("Es sind zu viele Schläger - du wirst zusammengeschlagen. ")
            print(tot())
            ende = "Schlechtes Ende"
            g.player_entscheidungen["Ende"] = ende
            spielstand_speichern(
                g.player,
                g.player_inventar,
                g.player_entscheidungen,
                g.spielstand_name
            )
        elif gewalt == 2:
            print("Du überzeugst sie friedlich und sie lassen ihn los")
            print("")
            hauptteil1()

    elif helfen == 2:
        print(f"Du hilfst ihm nicht. Du gehst nach Hause und stribst an einem {Fore.RED}Herzkasperl. ")
        print(tot())
        ende = "Schlechtes Ende"
        g.player_entscheidungen["Ende"] = ende
        spielstand_speichern(
            g.player,
            g.player_inventar,
            g.player_entscheidungen,
            g.spielstand_name
        )


