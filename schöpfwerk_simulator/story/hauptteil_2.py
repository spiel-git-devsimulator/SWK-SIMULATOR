from schöpfwerk_simulator.errors.error import zahlenkontrolle
from schöpfwerk_simulator.texte import texte, text_formatieren
from schöpfwerk_simulator.story.shop import dkfd, dkg, dkt
from schöpfwerk_simulator.story import minigame
from schöpfwerk_simulator.story.Story import storylast
from schöpfwerk_simulator.story.DukaufstDöner import dkfd
from schöpfwerk_simulator.story.shop import einkauf
from schöpfwerk_simulator.story.Story import storylast
from schöpfwerk_simulator.story.minigame import mgame
from schöpfwerk_simulator.story.ASCII_ART import spielzeit
from colorama import Fore, init
init(autoreset=True)
def tot():
    tot = Fore.RED+"Du bist tot. Ende" #hier wird der Text rot angezeigt.
    return tot

def game_yes_no():
    game = zahlenkontrolle("Möchtest du nochmals spielen? (1=Ja, 2=Nein): ")
    if game == 1:   
        mgame()
        storylast()
    elif game == 2:
        print("""Du hast das Minigame abgeschlossen!
        
        Zurück zur Story!
        
        """)
        storylast()
    else:
        print(Fore.RED+"Unknown ERROR.")

def hauptteil_2_start():
    print("""Du entscheidest dich den Typen zu schlagen. Du wirst offiziell ein Mitglied der SWKB und
        alle in der SWKB mögen dich Was möchtest du tun?? """)

    entscheidung = zahlenkontrolle("""
                                    1/Minigame spielen
                                    2/shop besuchen
                                    3/mit story weitermachen
                                
                                :  """)
    if entscheidung == 1:
        spielzeit()
        mgame()
        game_yes_no()
        
    elif entscheidung == 2:
        einkauf()
    elif entscheidung == 3:
        storylast()





