def zahlenkontrolle(prompt):
    while True:
        try:
            a = int(input(prompt))
            if a == 1 or a == 2:
                return a
            else:
                print("Gib nur 1 oder 2 ein!")
        except ValueError:
            print("Gib eine Zahl ein und keinen Buchstaben!")


def zahlenkontrolle_mit3(prompt):
    while True:
        try:
            b = int(input(prompt))
            if b == 1 or b == 2 or b == 3:
                return b
            else:
                print("Gib nur 1, 2 oder 3 ein!")
        except ValueError:
            print("Gib eine Zahl ein und keinen Buchstaben!")
    
def zahlenkontrolle_aufteilen(prompt):
    while True:
        try:
            d = int(input(prompt))
            return d
        except ValueError:
            print("Gib eine Zahl ein und keinen Buchstaben!")