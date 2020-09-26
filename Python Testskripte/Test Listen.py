
name = "nils"
print (name[0])           # Die 0 in eckigen Klammmern bezieht sich auf den ersten Buchstaben

print (name[0:3])         # Der Inhalt in den eckigen Klammmern bezieht sich auf den ersten bis dritten Buchstaben

print (name[-2:])         # Der Inhalt in der eckigen Klammer bezieht sich auf die letzten beiden Buchstaben

neueListe = [2,4,6,8,10]
print (neueListe)         # Druckt neue Liste 


wert = chr(178) 
gesamtListe = (name+ str(wert))
print  (gesamtListe)

print ((name[0])+str(wert))   #Druckt den Ersten Buchstaben von "name"+ den Wert aus "wert" 


lo  = "\u250F" 
lu  = "\u2517" 
ro  = "\u2513" 
ru  = "\u251B" 
lh  = "\u2503" 
lw  = "\u2501" 
fü  = "\u2588" 
ufü = "\u25A2" 
lz  = " "
listeEins   =[lo,lw,lw,lw,lw,lw,lw,lw,lw,ro]
listeZwei   =[lh,lz,lz,lz,lz,lz,lz,lz,lz,lh]
listeDrei   =[lh,lz,fü,lz,lz,lz,fü,fü,fü,lh]
listeVier   =[lh,fü,fü,fü,lz,lz,lz,fü,lz,lh]
listeFünf   =[lh,lz,lz,lz,fü,fü,lz,lz,lz,lh]
listeSechs  =[lh,lz,lz,lz,ufü,ufü,lz,lz,lz,lh]
listeSieben =[lh,lz,lz,lz,lz,lz,lz,lz,lz,lh]
listeAcht   =[lh,lz,lz,fü,fü,fü,fü,lz,lz,lh]
listeNeun   =[lh,lz,lz,lz,lz,lz,lz,lz,lz,lh]
listeZehn   =[lu,lw,lw,lw,lw,lw,lw,lw,lw,ru]

i=0

Zeile1  = ""
Zeile2  = ""
Zeile3  = ""
Zeile4  = ""
Zeile5  = ""
Zeile6  = ""
Zeile7  = ""
Zeile8  = ""
Zeile9  = ""
Zeile10 = ""

while i<10:
    Zeile1  = Zeile1 + (listeEins[i])
    Zeile2  = Zeile2 + (listeZwei[i])
    Zeile3  = Zeile3 + (listeDrei[i])
    Zeile4  = Zeile4 + (listeVier[i])
    Zeile5  = Zeile5 + (listeFünf[i])
    Zeile6  = Zeile6 + (listeSechs[i])
    Zeile7  = Zeile7 + (listeSieben[i])
    Zeile8  = Zeile8 + (listeAcht[i])
    Zeile9  = Zeile9 + (listeNeun[i])
    Zeile10 = Zeile10 + (listeZehn[i])

    i=i+1

print(Zeile1)
print(Zeile2)
print(Zeile3)
print(Zeile4)
print(Zeile5)
print(Zeile6)
print(Zeile7)
print(Zeile8)
print(Zeile9)
print(Zeile10)