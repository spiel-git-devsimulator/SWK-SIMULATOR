from schöpfwerk_simulator.errors.error import zahlenkontrolle
from schöpfwerk_simulator.texte import texte, text_formatieren
from schöpfwerk_simulator import global_variablen as g
from schöpfwerk_simulator.speichern import spielstand_speichern
from colorama import Fore, init
from schöpfwerk_simulator.story.ASCII_ART import polizeistation
from schöpfwerk_simulator.story.Zahlenkontrolle import zahlenkontrolle_mit3
init(autoreset=True)
def tot():
    tot = Fore.RED+"Du bist tot. Ende" #hier wird der Text rot angezeigt.
    return tot

def hauptteil_1_3_start():
    print(text_formatieren.text_formatierung(texte.start_1_3))
    true_false = zahlenkontrolle("Möchtest du die Wahrheit sagen (1=Ja, 2=Nein): ")
    if true_false == 1:
        print(text_formatieren.text_formatierung(texte.good_boy))
        drei_teilig = zahlenkontrolle_mit3("Nix tun=1, Kiberer=2, Gangbeitritt=3: ")
        if drei_teilig == 1:
            print(text_formatieren.text_formatierung(texte.tod_01))
            print(Fore.BLUE+"Deine Entscheidungen haben zu einem schlechtem Ende geführt. ")
            print(tot())
            ende = "Schlechtes Ende"
            g.player_entscheidungen["Ende"] = ende
            spielstand_speichern(
                g.player,
                g.player_inventar,
                g.player_entscheidungen,
                g.spielstand_name
            )
        elif drei_teilig == 2:
            polizeistation()
            print(text_formatieren.text_formatierung(texte.kiwara))
            print(Fore.YELLOW+"Geheimes Ende. ")
            ende = "Geheimes Ende"
            g.player_entscheidungen["Ende"] = ende
            spielstand_speichern(
                g.player,
                g.player_inventar,
                g.player_entscheidungen,
                g.spielstand_name
            )
        elif drei_teilig == 3:
            print(text_formatieren.text_formatierung(texte.loop_bad))
            print(Fore.RED+"Deine Entscheidungen haben zu einem schlechtem Ende geführt. ")
            print(tot())
            ende = "Schlechtes Ende"
            g.player_entscheidungen["Ende"] = ende
            spielstand_speichern(
                g.player,
                g.player_inventar,
                g.player_entscheidungen,
                g.spielstand_name
            )
            
    else:
        print(tot())
        ende = "Schlechtes Ende"
        g.player_entscheidungen["Ende"] = ende
        spielstand_speichern(
            g.player,
            g.player_inventar,
            g.player_entscheidungen,
            g.spielstand_name
        )









