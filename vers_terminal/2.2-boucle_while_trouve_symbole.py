
"""
Jeu :
    Proposez à l'utilisateur de trouver 
    le symbole chosit par le programme
    en moins de coups posssible.


"""
import random

# liste de 3 symboles
symboles =  ['@','#','$']
# programme choisit un symbole au hasard
r =  random.randint(0, len(symboles)-1)
program_symbole =  symboles[r]
# utilisateur recherche bon symbole
user_symbole =""
i=0;
while user_symbole != program_symbole:
    i+=1
    user_symbole =  input("quel symbole a choisit le programme ?")
    if user_symbole != program_symbole:
        print("Naaan !")

print("vous avez trouvé en "+ str(i) +" coup(s)")
