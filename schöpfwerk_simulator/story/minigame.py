import random
#from schöpfwerk_simulator.story.Zahlenkontrolle import zahlenkontrolle
from schöpfwerk_simulator.story.Zahlenkontrolle import zahlenkontrolle_minigame


def mgame():

    print("""Willkommen im Ratespiel !! 
        Dein ziel ist es eine Zahl zwischen 1 und 100 zu erraten!
        Viel Glück!!!""")

    zahl = random.randint(1,100)
    versuche = 0

    while True:
        
        Dein_Versuch = zahlenkontrolle_minigame("Versuche die Zahl zu erraten! : ")
        versuche +=1

        if Dein_Versuch < zahl:
            print("Deine Zahl ist zu klein")
        elif Dein_Versuch > zahl:
            print("Deine Zahl ist zu groß")
        if Dein_Versuch == zahl:
            print("Du hast die Zahl in",versuche," Versuchen erraten!")
            break

#mgame()