n = int(input("entrer le nombre de jours du mois ""\n"))
j = int(input("entrer le premier jour du mois : 1 pour lundi .... ""\n"))

Jours = [ "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam", "Dim" ]
print(" ".join(Jours))

print("  " *(j - 1), end="")
    
for jour in range (1, n+1):
    print(f"{jour:3}", end=" ")
    
    if (jour + j -1) % 7 == 0:
        print ()