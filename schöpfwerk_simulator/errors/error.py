
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