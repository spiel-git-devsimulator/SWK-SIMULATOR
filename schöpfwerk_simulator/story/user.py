from colorama import Fore, init
init(autoreset=True)
def user():
    while True: 
        try: # probieren
            name = input("Gib deinen Namen ein: ") #man muss an input eingeben
            name = str(name) # jetzt wird name zu am String
            break 
        except ValueError: 
            print(Fore.RED+"Gib einen String ein!") # in roter schrift: Gib an String ein!
    return name