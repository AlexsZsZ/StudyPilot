taches = []


print("===== StudyPilot =====")

def afficher_menu():
    print("Ajouter une tache")
    print("Afficher les taches")
    print("Terminer une tache")
    print("Quitter")
afficher_menu()

choix = int(input("Ton choix (1-4) : "))

action = "Ajouter une tâche"


if choix == 1:
    action = "Ajouter une tâche"
elif choix == 2:
    action = "Ajouter les tâches"
if choix == 3:
    action = "Terminer une Taches"
elif choix == 4:
    action = "Quitter"    
    

print(f"Vous avez choisi l'option {choix} qui est {action}")



