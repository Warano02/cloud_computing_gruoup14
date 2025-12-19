def saisir_donnees(callback): #fonction pour gérer les entrées de l'utilisateur 
    while True:
        try:
            nb_jours = int(input("Entrez le nombre de jours du mois (28 à 31) : " "\n"))
            if not 28 <= nb_jours <= 31: # condition sur le nombre minimal et maximal de jours du mois 
                print("❌ \033[31m Le nombre de jours doit être entre 28 et 31.00m[\033")
                continue

            jour_debut = int(input("Entrez le jour de début (1=Lundi ... 7=Dimanche) : " "\n"))
            if not 1 <= jour_debut <= 7: #condition sur le nombre minimal et maximal pour être considéré comme 1er jour
                print("❌ \033[31m Le jour de début doit être compris entre 1 et 7. 00m[\033")
                continue

            callback(nb_jours, jour_debut)
            break

        except ValueError:
            print("❌ Veuillez entrer uniquement des nombres.")

def construire_calendrier(nb_jours, jour_debut): #fonction pour construire le calendrier
    jours_semaine = ["Lun", "Mar", "Mer", "Jeu", "Ven", "Sam", "Dim"]

    for jour in jours_semaine:
        print(f"{jour:>4}", end="") # affiche tous les jours de la semaine sur la mm ligne 
    print("\n" + "-" * 28) #affiche les tirets en bas des jours 

    for _ in range(jour_debut - 1): 
        print(" " * 4, end="")

    for jour in range(1, nb_jours + 1): # affiche les jours correspondants 
        print(f"{jour:>4}", end="")
        if (jour + jour_debut - 1) % 7 == 0: # retour à la ligne quand on atteint 7
            print()
    print()

saisir_donnees(construire_calendrier) #affiche le résultat sous forme de calendrier.
    