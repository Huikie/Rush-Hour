Wat is het verschil tussen een moeilijke rushhour-opgave en een evengrote makkelijk rushhour opgave (Ook aantonen waar de moeilijkheid niet aan ligt is waardevol):

Wij denken dat de complexiteit veroorzaakt wordt door een combinatie van het mogelijk aantal zetten per board en het minimaal aantal zetten dat nodig is om het winnende board te vinden. Wij denken dat de onderstaande formule een goeie indicatie geeft van de complexiteit van een bord. Waarbij een lage score een indicatie is van een relatief eenvoudig bord en een hoge score een indicatie is van een relatief complex bord.

>Minimaal aantal moves nodig voor winnend board ^ gemiddeld aantal mogelijke zetten per boards

Ons vermoeden wordt allereerst onderbouwd door onze breadth first berekeningen van bord 1, 2 en 3. Zo heeft bord 2 slechts 15 zetten nodig om te worden opgelost, maar duurt het vinden van deze oplossing langer dan bij bord 3, waar 21 zetten nodig zijn. Bij nadere inspectie valt dit te verklaren door het aantal mogelijke zetten in iedere branch. Hoewel bord 2 minder zetten nodig heeft, zijn er in iedere branch meer mogelijke zetten dan bij bord 3. Hierdoor is bord 2 in minder zetten op te lossen, maar complexer dan bord 3. Daarnaast is bord 1 complexer dan bord 2 en bord 3, die is logisch aangezien bord 3 opgelost kan worden in 33 en in iedere branch meer mogelijke zetten heeft dan bord 2 en 3.

Ons vermoeden wordt ondersteund door het artikel:
