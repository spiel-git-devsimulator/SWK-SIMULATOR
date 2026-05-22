from colorama import Fore, init
init(autoreset=True)
# hier kommen alle Texte hinein:
hauptteil1 = """Er bedankt sich und stellt sich als Dragan vor. 
Er erzählt dir, dass ein großer Konflikt zw. 2 Gruppen entstanden ist. (SWS, SWKB) .
Er bittet dich darum, Frieden ins SWK zu bringen. 
Du gehst zuerst ins SWS Quartier. Dort wirst du zusammengeschlagen. 
Du wirst zu ihrem Anführer gebracht. Du versuchst diesen von deiner Mission zu überzeugen. 
Er glaubt dir nicht.Er zeigt dir aber Gnade und beauftragt dich
den SWKB Anführer zu töten """

anführer_töten = """Du schaffst es nicht den Anführer zu töten, weil
das SWKB Quartier zu gut bewacht ist. Du kommst zur SWS zurück und der Anführer sagt,
 Du musst die SWKB ausspionieren musst 
"""
hauptteil_main_01 = """ Du gehst ins SWKB Quartier. Dort freundest du dich nach langer Zeit
mit einem Typen namens Ivan an. Als Zeichen eurer Freundschaft bietet er dir Rakija an.
(Er ist ziemlich bsoffn.)
"""
dead_hauptteil_01 = Fore.RED+"""Du wurdest gewarnt, dass er betrunken ist.
Die Flasche war mit Desinfektionsmittel gefüllt"""

bier = "Er bietet dir Bier an. "
bier_ja = """ Du trinkst es.
Dir schmeckt es (du Alkoholiker). Er bringt dich zum SWKB Anführer.
Dieser ist misstrauisch und will dich testen indem er dich beauftragt,
die SWS auszuspionieren.
"""
cooperate_yes = """
In den kommenden Wochen spionierst du sowohl die SWS und die SWKB aus.
Du nimmst auch an Schlägereien Teil und wirst auch ziemlich oft verletzt.
Du trägst aber immer eine Maske, sodass dich keiner erkennen kann. Eines tages
erfährst du, dass die SWKB einen Angriff auf die SWS plant.
"""
warn_yes = """
Du warnst die SWS. Die SWKB erfährt,
dass du ein Verräter bist und sie töten dich. """
warn_ok = """
Du verrätst sie nicht, der Angriff findet statt und ein
SWS-Mitglied bittet dich um Gnade. Du musst jetzt entscheiden was du mit ihm machen wirst.
Du hast 3 Möglichkeiten:
1. Nichts tun 2. Ihn schlagen 3. ihn laufen lassen.
"""
start_1_3 = """
Du schaust ihm zu, wie er wegläuft. Du überlegst ob es die richtige
Entscheidung war. Wenige Tage später wirst du von der SWS gefangen
genommen. Der Typ, den du nicht schlagen wolltest hat dich verraten.
Du wirst jetzt befragt. 
"""
good_boy = """
Sie nennen dich einen GOOD BOY. Nach einiger Zeit schaffst du es zu entkommen. 
Du stehst wieder vor der Volksschule. Du denkst darüber nach was bis jetzt alles passiert ist. Du stehst 
vor einer Entscheidung. Du hast 3 Optionen:
Du tust als ob nix passiert ist und gehst nach Hause, du Informierst die Kiberer
oder schließt dich der SWKB an. 
Was wählst du? 
"""
start_2 = """
Du schlägst ihn und wirst endgültig zum Mitglied der SWKB. 
(Im SWKB-Quartier schaltest du den Shop frei, dort kannst du Sachen kaufen). 
Es gibt jetzt kein Zurück mehr. 
"""
shop = """
Du darfst nur eine Sache auswählen.
"""
tod_01 ="""
Du wirst zu Hause gepackt, weil du ein Verräter bist.
"""

loop_bad = """
Du schließt dich der SWKB an und der Konflikt endet nie.
Du hast deine Mission nicht erfüllt.
"""
kiwara = """
Du sagst alles der Polizei. Du bist ein Verräter.
In den kommenden Tagen gehst du durchs SWK und hörst im SWS Quartier Schüsse
Du wirst zwar bissl geschlagen aber du hast in das Schöpfwerk Frieden gebracht.
"""
