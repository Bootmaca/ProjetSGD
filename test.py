livre = "Ma première variable"
print(livre)
print(type(livre))
print("Affichage du premier caractère de la variable livre : ", livre[0])
myFirstTab = ["valeur1", "valeur2", "valeur3", "valeur4"]
print(myFirstTab[0])
myFirstTab.remove("valeur3")
myFirstTab.remove(myFirstTab[2]) # Suppression de la 3 valeur du tableau ("valeur4" car "valeur3" à été supprimé
print("voila le contenue de mon premier tableau : ")
print(myFirstTab)
print("Avec pour longueur : ", len(myFirstTab))