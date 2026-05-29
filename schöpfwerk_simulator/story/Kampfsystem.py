from schöpfwerk_simulator.story.Zahlenkontrolle import zahlenkontrolle
import random
from schöpfwerk_simulator import global_variablen as g
from schöpfwerk_simulator.speichern import spielstand_speichern
from colorama import Fore, init
import sys
init(autoreset=True)
def tot():
    tot = Fore.RED+"Du bist tot. Ende" #hier wird der Text rot angezeigt.
    return tot


def kampfsystem_besser():

    hp_anfuhrer = 50
    dein_hp = 50

    while hp_anfuhrer > 0 and dein_hp > 0:

        entscheidung = zahlenkontrolle("Gib 1 ein um anzugreifen und 2 um dich zu heilen: ")

        if entscheidung == 1:

            angriff = random.randint(5, 10)
            schadenkassierer = random.randint(5, 10)

            hp_anfuhrer -= angriff
            dein_hp -= schadenkassierer

            if hp_anfuhrer < 0:    #damit keine Minuszahlen kommen
                hp_anfuhrer = 0     

            if dein_hp < 0:
                dein_hp = 0

            print("Dein Hp :", dein_hp, "/50")
            print("Anführer Hp :", hp_anfuhrer, "/50")
            print("Du hast", schadenkassierer,
                "Schaden bekommen und", angriff,
                "Schaden gemacht.")
        elif entscheidung == 2:
            heilen = 5
            #dein_hp=dein_hp+heilen
            dein_hp += heilen #Update von dein_hp 
            print("Dein Hp :", dein_hp, "/50")
            print("Anführer Hp :", hp_anfuhrer, "/50")
            print("""Du hast dich um""",heilen,"""Hp geheilt.
                  Du kannst dich erst ab der nächsten Attacke
                  wieder heilen.""")

    if hp_anfuhrer == 0:
        print("Du hast gewonnen!")


    elif dein_hp == 0:
        
        print("Du wurdest besiegt!")
        print(tot())
        ende = "Schlechtes Ende"
        g.player_entscheidungen["Ende"] = ende
        spielstand_speichern(
            g.player,
            g.player_inventar,
            g.player_entscheidungen,
            g.spielstand_name
        )
        #sys.exit()
        
    
