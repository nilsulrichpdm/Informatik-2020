
def ausgabe_Spielfeld(Zeilen):
    
    i=3
    while i >= 0:
        ausgabe = Zeilen[i][0] + Zeilen[i][1] +Zeilen[i][2] +Zeilen[i][3]
        print (ausgabe)
        i=i-1



Symbol1 = "\u26AA"
Symbol2 = "\u26AB"

Z1=["","","",""]

Z2=["","","",""]
Z3=["","","",""]
Z4=["","","",""]
Zeilen = [Z1,Z2,Z3,Z4]

S1=["","","",""]
S2=["","","",""]
S3=["","","",""]
S4=["","","",""]
Spalten = [S1,S2,S3,S4]

S_Stand =[0,0,0,0]

Programm_ENDE = False
Eingabecounter =0
while Programm_ENDE == False:
    Eingabecounter += 1
    if (Eingabecounter % 2) == 0:
        Symbol = Symbol1
    else:
        Symbol = Symbol2

    Eingabe = input("Bitte Zahl zwischen 1-4")
    current_S = int(Eingabe) -1
    S_Stand[current_S] = S_Stand[current_S] + 1
    print(S_Stand)
    current_Z = S_Stand[current_S] - 1
    Spalten[current_S][current_Z] = Symbol
    Zeilen[current_Z][current_S] =Symbol
    #print(Spalten)
    #print(Zeilen)
    ausgabe_Spielfeld(Zeilen)




