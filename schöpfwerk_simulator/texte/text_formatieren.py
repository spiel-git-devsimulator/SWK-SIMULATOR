import shutil, textwrap #importe 


def text_formatierung(input): #erstellung einer Funktion
    breite = shutil.get_terminal_size().columns  # anfrage via shutil an 
    # pc wie breit das terminal ist (Spaltenanzahl)
    text = textwrap.fill(input, width=breite) #wird verwendet um zu schauen wann
    # der Text umgebrochen werden muss (neue Zeile).
    return text









