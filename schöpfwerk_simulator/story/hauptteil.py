from schöpfwerk_simulator.texte import texte, text_formatieren
from schöpfwerk_simulator.errors.error import zahlenkontrolle
from schöpfwerk_simulator.story import hauptteil_1_3, hauptteil_2
from schöpfwerk_simulator.story.hauptteil_1_3 import hauptteil_1_3_start
from schöpfwerk_simulator.story.hauptteil_2 import hauptteil_2_start
from schöpfwerk_simulator.speichern import spielstand_speichern
from schöpfwerk_simulator import global_variablen as g
from colorama import Fore, init
from schöpfwerk_simulator.story.ASCII_ART import geniessen

init(autoreset=True)
def tot():
    tot = Fore.RED+"Du bist tot. Ende" #hier wird der Text rot angezeigt.
    return tot
def hauptteil1():
    print(text_formatieren.text_formatierung(texte.hauptteil1))
    #
    anführer_dead = zahlenkontrolle("Möchtest du ihn töten (1=Ja, 2=Nein):")
    if anführer_dead == 1:
        print(tot())
        ende = "Schlechtes Ende"
        g.player_entscheidungen["Ende"] = ende
        spielstand_speichern(
            g.player,
            g.player_inventar,
            g.player_entscheidungen,
            g.spielstand_name
        )
    elif anführer_dead == 2: 
        print(text_formatieren.text_formatierung(texte.anführer_töten))
        print(text_formatieren.text_formatierung(texte.hauptteil_main_01))
        trinken = zahlenkontrolle("Möchtest du das Getränk mit ihm trinken? (1=Ja, 2=Nein) ")
        if trinken == 1:
            print(tot())
            print(text_formatieren.text_formatierung(texte.dead_hauptteil_01))
            ende = "Schlechtes Ende"
            g.player_entscheidungen["Ende"] = ende
            spielstand_speichern(
                g.player,
                g.player_inventar,
                g.player_entscheidungen,
                g.spielstand_name
            )

        elif trinken == 2: 
            print(text_formatieren.text_formatierung(texte.bier))
            bier = zahlenkontrolle("Möchtest du es trinken? (1=Ja, 2=Nein) ")
            geniessen()
            if bier == 1:
                print(text_formatieren.text_formatierung(texte.bier_ja))
                cooperate = zahlenkontrolle("Akzeptierst du die Kooperation mit ihm? (1=Ja, 2=Nein): ")
                if cooperate == 1:
                    print(text_formatieren.text_formatierung(texte.cooperate_yes))
                    warn = zahlenkontrolle("Möchtest du SWS warnen (1=Ja, 2=Nein): ")
                    if warn == 1:
                        print(text_formatieren.text_formatierung(texte.warn_yes))
                        print(tot())
                        ende = "Schlechtes Ende"
                        g.player_entscheidungen["Ende"] = ende
                        spielstand_speichern(
                            g.player,
                            g.player_inventar,
                            g.player_entscheidungen,
                            g.spielstand_name
                        )
                    elif warn == 2: 
                        print(text_formatieren.text_formatierung(texte.warn_ok))
                        aufteilung = zahlenkontrolle("Wie entscheidest du dich? (1=nichts tun, 2=ihn schlagen, 3=laufen lassen): ")
                        if aufteilung == 1 or aufteilung == 3:
                            hauptteil_1_3_start()
                        elif aufteilung == 2:
                            hauptteil_2_start()
                            #Hauptding
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

            



