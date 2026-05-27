from schöpfwerk_simulator.story.Zahlenkontrolle import zahlenkontrolle
from schöpfwerk_simulator import global_variablen as g
from schöpfwerk_simulator.speichern import spielstand_speichern
from colorama import Fore, init
from schöpfwerk_simulator.story.Kampfsystem import kampfsystem_besser
from schöpfwerk_simulator.story.ASCII_ART import SWKGebäude
from schöpfwerk_simulator.story.Zahlenkontrolle import zahlenkontrolle_aufteilen
from schöpfwerk_simulator.story.Zahlenkontrolle import zahlenkontrolle_mit3
init(autoreset=True)
def tot():
    tot = Fore.RED+"Du bist tot. Ende" #hier wird der Text rot angezeigt.
    return tot

def storylast():
    def SWSKOMMT():
        print("""Du bist nun ein SWKB Mitglied! Du triffst viele interessante Menschen und
            freundest dich mit vielen von ihnen an. Eines tages sitzt du im SWKB Hauptquartier,
            als du plötzlich eine Stimme hörst.Es ist der SWS Anführer. Er weiß, dass du sie
            verraten hast und fordert dich zu einem 1v1 heraus.""")
        
    SWSKOMMT()
    def kampf():

            kämpfenodernicht = zahlenkontrolle_mit3("""Kämpfst du gegen ihn oder nicht?
                                            1/Kämfen
                                            2/Nicht kämfen
                                            3/Nix tun
                                            :  """)

            if kämpfenodernicht == 2:
                print(tot())
                ende = "Schlechtes Ende"
                g.player_entscheidungen["Ende"] = ende
                spielstand_speichern(
                    g.player,
                    g.player_inventar,
                    g.player_entscheidungen,
                    g.spielstand_name
                )
            elif kämpfenodernicht ==3:
                print(tot())
                ende = "Schlechtes Ende"
                g.player_entscheidungen["Ende"] = ende
                spielstand_speichern(
                    g.player,
                    g.player_inventar,
                    g.player_entscheidungen,
                    g.spielstand_name
                )
            elif kämpfenodernicht == 1:
                def kampfsystem():
                    print("""Du kämpfst also gegen den Anfüherer!
                        Sehr mutig von dir. 
                        Mach genug Schaden um ihn zu besiegen!
                        Viel Glück!""")
                    kampfsystem_besser()
                    print("""Der Anführer liegt besiegt vor deinen Füßen. Er bittet dich um Gnade.
                        Du zeigst ihm Gnade. Er ist überrascht und auch dankbar. Du bist die einzige Person
                        im ganzen Schöpfwerk, welche Personen von beiden Seiten kennt und weiß wie beide
                        Gruppen organisiert sind.Alle respektieren dich. Der SWS und SWKB Anführer einigen sich auf eine Sache:
                        DU BIST DER EINZIGE, DER DAS SCHÖPFERK GERECHT ZWISCGEN DEN BEIDEN GRUPPEN AUFTEILEN KANN.
                        
                        SEI ABER VORSICHTIG
                        ES GIBT MEHR SWS MITGLIEDER ALS SWKB MITGLIEDER
                        Teile das Gebiet gerecht auf!
                        Es gibt 50 Stiegen (Gebäude)
                        Gib der SWKB eine geeignete Stiegenanzahl""")
                        
                    gerchtaufteilen = zahlenkontrolle_aufteilen("Gib ein, wieviele Stiegen du der SWKB geben willst: ")
                    if gerchtaufteilen <10 or gerchtaufteilen >20:
                        print("""Du hast das Gebiet nicht gerecht aufgeteilt.
                            Der Konflikt fängt wegen dir wieder an!""")
                        print("SCHLECHTES ENDE")
                    else:
                        SWKGebäude()
                        print("""Du hast das Gebiet gerecht aufgeteilt!
                            Du hast deine Mission erfüllt.
                            
                            GUTES ENDE""")
                        ende = "Gutes Ende"
                        g.player_entscheidungen["Ende"] = ende
                        spielstand_speichern(
                            g.player,
                            g.player_inventar,
                            g.player_entscheidungen,
                            g.spielstand_name
                        )

                        
                kampfsystem()
    kampf()





    
