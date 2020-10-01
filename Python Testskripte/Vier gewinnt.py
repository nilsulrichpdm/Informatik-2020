
def ausgabe_Spielfeld(Zeilen):
    
    i=6
    while i >= 0:
        ausgabe = Zeilen[i][0] + Zeilen[i][1] + Zeilen[i][2] + Zeilen[i][3] + Zeilen[i][4] + Zeilen[i][5] + Zeilen[i][6]
        print (ausgabe)
        i=i-1


def prüfe_binaere_Zahl(Zahl,Maske):
    Ergebnis= 0
    counter=0
    while Zahl >= Maske:
        counter+=1
        print("ZAHL" + str(Zahl) + " binär:" + str(bin(Zahl)))
        if Zahl & Maske == Maske:
            Ergebnis = counter
            print("Ergbnis bei Stelle:" + str(Ergebnis))
            return Ergebnis
            
        Zahl = Zahl >> 1
    print("Ergbnis:" + str(Ergebnis))
    return Ergebnis





def main():

    Symbol1 = "\u26AA"
    Symbol2 = "\u2733"

    Z1=["\u26AB","\u26AB","\u26AB","\u26AB","\u26AB","\u26AB","\u26AB"]
    Z2=["\u26AB","\u26AB","\u26AB","\u26AB","\u26AB","\u26AB","\u26AB"]
    Z3=["\u26AB","\u26AB","\u26AB","\u26AB","\u26AB","\u26AB","\u26AB"]
    Z4=["\u26AB","\u26AB","\u26AB","\u26AB","\u26AB","\u26AB","\u26AB"]
    Z5=["\u26AB","\u26AB","\u26AB","\u26AB","\u26AB","\u26AB","\u26AB"]
    Z6=["\u26AB","\u26AB","\u26AB","\u26AB","\u26AB","\u26AB","\u26AB"]
    Z7=["\u26AB","\u26AB","\u26AB","\u26AB","\u26AB","\u26AB","\u26AB"]
    Zeilen = [Z1,Z2,Z3,Z4,Z5,Z6,Z7]

    S1=["\u26AB","\u26AB","\u26AB","\u26AB","\u26AB","\u26AB","\u26AB"]
    S2=["\u26AB","\u26AB","\u26AB","\u26AB","\u26AB","\u26AB","\u26AB"]
    S3=["\u26AB","\u26AB","\u26AB","\u26AB","\u26AB","\u26AB","\u26AB"]
    S4=["\u26AB","\u26AB","\u26AB","\u26AB","\u26AB","\u26AB","\u26AB"]
    S5=["\u26AB","\u26AB","\u26AB","\u26AB","\u26AB","\u26AB","\u26AB"]
    S6=["\u26AB","\u26AB","\u26AB","\u26AB","\u26AB","\u26AB","\u26AB"]
    S7=["\u26AB","\u26AB","\u26AB","\u26AB","\u26AB","\u26AB","\u26AB"]
    Spalten = [S1,S2,S3,S4,S5,S6,S7]

    S_Stand =[0,0,0,0,0,0,0]

    SP1_WAGERECHT =[0,0,0,0,0,0,0] 
    SP2_WAGERECHT = [0,0,0,0,0,0,0]

    SP1_SENKRECHT =[0,0,0,0,0,0,0] 
    SP2_SENKRECHT = [0,0,0,0,0,0,0]


    Programm_ENDE = False
    Eingabecounter =0


    while Programm_ENDE == False:
        Eingabecounter += 1
        if (Eingabecounter % 2) == 0:
            Symbol = Symbol1
            Spieler = "Spieler 1"
        else:
            Symbol = Symbol2
            Spieler = "Spieler 2"

        Eingabefehler = True 
        while Eingabefehler:
            Eingabe = input("Bitte Zahl zwischen 1-7")
            if Eingabe.isnumeric() == True:
                if int(Eingabe) in range (1,8):
                    if S_Stand[int(Eingabe)-1] < 7:
                        Eingabefehler = False #Eingabe ist Korrekt
                    else:
                        print ("Die Saplte [" + str(Eingabe) + "] ist voll")
                else:
                    print("Zahl ausserhalb 1..7")
            else:
                if Eingabe.upper() == "ENDE":
                    exit()
                else:
                    print("Bitte eine Zahl zwischen 1..7 oder Ende eingeben")
                

        
        
        
        current_S = int(Eingabe) -1
#       Berechner SP1/SP2 LISTE
#       Die Spielerliste besteht aus einer Dezimalzahl pro Zeile
#       Jede Dezimalzahl stellt binär die Belegung der Spalten pro Zeile dar
#       Es gibt 7 Spalten (1..7)
#       Ist die Spalte 7 belegt ist das erste BIT (2^0=1) = 1
#       IST die Spalte 6 belegt ist das zweite BIT (2^1=2) = 1
#       Ist die Spalte 5 belegt ist das dritte BIT (2^2=4) = 1
#       IST die Spalte 1 belegt ist das siebente BIT (2^7=128) = 1
#       Durch Addition erhält man die binäre Belegung der Spalten einer Zeile
#       z. B. 1 0 0 0 0 0 1 [7. und 1. Spalte] = 128 + 1 = 129
#       der Index der Liste läuft von links Index 0 = Spalte 1 entgegen der binären Codierung
#       Umrechnung von Spalte auf Index => Spalte (Eingabe) - 1
#       Umrechnung von Spalte auf Belegungs-Bit => 8 - Spalte (Eingabe) 


        if Symbol ==Symbol1:
            SP1_WAGERECHT[S_Stand[current_S]] = SP1_WAGERECHT[S_Stand[current_S]] + 2 ** (8-int(Eingabe))
            Programm_ENDE = prüfe_binaere_Zahl(SP1_WAGERECHT[S_Stand[current_S]],15) > 0

        else:
            SP2_WAGERECHT[S_Stand[current_S]] = SP2_WAGERECHT[S_Stand[current_S]] + 2 ** (8-int(Eingabe))
            Programm_ENDE = prüfe_binaere_Zahl(SP2_WAGERECHT[S_Stand[current_S]],15) > 0

        print("SP1:" + str(SP1_WAGERECHT))
        print("SP2:" + str(SP2_WAGERECHT))


        S_Stand[current_S] = S_Stand[current_S] + 1
        print("S_Stand: " + str(S_Stand))
        current_Z = S_Stand[current_S] - 1
        Spalten[current_S][current_Z] = Symbol
        Zeilen[current_Z][current_S] = Symbol
        
        ausgabe_Spielfeld(Zeilen)
    #Programmende
    print ("Spieler :" + Spieler + " hat gewonnen")
    

main()


