def zahlenkontrolle(prompt):
    while True:
        try:
            a = int(input(" "+ prompt))
            return a
        except ValueError:
            print("Gib eine Zahl ein und keinen Buchstaben! ")