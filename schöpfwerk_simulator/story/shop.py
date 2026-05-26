from schöpfwerk_simulator.story.Zahlenkontrolle import zahlenkontrolle
from schöpfwerk_simulator.story.DukaufstDöner import dkfd
from schöpfwerk_simulator.story.DukaufstGetränk import dkg
from schöpfwerk_simulator.story.DukaufstTaschenmesser import dkt
from schöpfwerk_simulator import global_variablen as g
from schöpfwerk_simulator.story.Zahlenkontrolle import zahlenkontrolle_mit3

#def inventory():
#    myinventory 

def einkauf():

        shop = ["Taschenmesser","Getränk","Döner"]

        myinventory = ["10,50€","Kappe","J's","Jacke"]

        optionen = zahlenkontrolle_mit3("Was möchtest du im Shop kaufen? 1/Taschenmesser, 2/Getränk, 3/Döner: ")

        if optionen == 1:
            myinventory.append(shop[0])
            print("Du hast ein",shop[0],"für 10,50€ gekauft. Dieses Item wurde in dein Inventar hinzugefügt.")
            myinventory.pop(0)
            print(myinventory)
            g.player_inventar = myinventory
            dkt()
        elif optionen == 2:
            myinventory.append(shop[1])
            print("Du hast ein",shop[1]," für 1,50€ gekauft. Dieses Item wurde in dein Inventar hinzugefügt.")
            myinventory.pop(0)
            myinventory.append("9,00€")
            print(myinventory)
            g.player_inventar = myinventory
            dkg()
        elif optionen == 3:
            myinventory.append(shop[2])
            print("Du hast einen",shop[2],"gekauft. Dieses Item wurde in dein Inventar hinzugefügt.")
            myinventory.pop(0)
            myinventory.append("5,00€")
            print(myinventory)
            g.player_inventar = myinventory
            dkfd()
