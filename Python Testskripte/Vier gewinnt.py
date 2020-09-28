
def ausgabe_Spielfeld(Zeilen):
    
    i=6
    while i >= 0:
        ausgabe = Zeilen[i][0] + Zeilen[i][1] + Zeilen[i][2] + Zeilen[i][3] + Zeilen[i][4] + Zeilen[i][5] + Zeilen[i][6]
        print (ausgabe)
        i=i-1



Symbol1 = "\u26AA"
Symbol2 = "\u26AB"

Z1=["","","","","","",""]
Z2=["","","","","","",""]
Z3=["","","","","","",""]
Z4=["","","","","","",""]
Z5=["","","","","","",""]
Z6=["","","","","","",""]
Z7=["","","","","","",""]
Zeilen = [Z1,Z2,Z3,Z4,Z5,Z6,Z7]

S1=["","","","","","",""]
S2=["","","","","","",""]
S3=["","","","","","",""]
S4=["","","","","","",""]
S5=["","","","","","",""]
S6=["","","","","","",""]
S7=["","","",""],"","",""
Spalten = [S1,S2,S3,S4,S5,S6,S7]

S_Stand =[0,0,0,0,0,0,0]

Programm_ENDE = False
Eingabecounter =0
while Programm_ENDE == False:
    Eingabecounter += 1
    if (Eingabecounter % 2) == 0:
        Symbol = Symbol1
    else:
        Symbol = Symbol2

    Eingabefehler = True 
    while Eingabefehler:
        Eingabe = input("Bitte Zahl zwischen 1-7")
        if Eingabe.isnumeric() == True:
            if int(Eingabe) in range (1,7):
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
    S_Stand[current_S] = S_Stand[current_S] + 1
    print(S_Stand)
    current_Z = S_Stand[current_S] - 1
    Spalten[current_S][current_Z] = Symbol
    Zeilen[current_Z][current_S] =Symbol
    #print(Spalten)
    #print(Zeilen)
    ausgabe_Spielfeld(Zeilen)




