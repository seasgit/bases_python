"""
Cet exercice permet de vérifier la popularité d'animaux par le programme
Il peut y avoir  : 
- un animal avec un niveau de popularité supérieur aux autres
- plusieurs animaux avec un même niveau de popularité supérieur aux autres
"""

import random
# Un tableau = données de base
animaux = ['chien','chat','cheval','poule','tortue','canard','vache','mouton']
# un tableau pour enregistrer des dictionnaires avec le nom et la popularité de chaque animal
dico = []
# niveau de popularité de départ
lePlusPopulaire =  -1
# tableau pour stocker plusieurs animaux avec un niveau de pop > autres
lesPlusPopulaires = []
# le programme crée dynamiquement le tableau des dico
for a in animaux:
    dico.append({
        "name":a,
        "pop":random.randint(0,5)
    })
# le programme évalue la popularité
for a in dico:
    if a['pop'] > lePlusPopulaire:
        lePlusPopulaire = a['pop']
        plusieurs = [a]
    elif a['pop'] == lePlusPopulaire:
        lesPlusPopulaires.append(a)

# trace du tableau dico --> print(dico)

# Evaluation et construction du message
out=""
if(len(lesPlusPopulaires)>1):
    out = "les animaux "
    for a in lesPlusPopulaires:
        out += a['name']+' - '
    out += "ont un score de "+ str(lePlusPopulaire)
else:
    out = plusieurs[0]['name'] + " avec un score de "+ str(lePlusPopulaire)
print("--------------")
print(out)