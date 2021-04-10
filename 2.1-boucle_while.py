import random
r=0
cpt = 0
while r != 10 :
    cpt+=1
    r = random.randint(1,20)
    print('tour n°'+str(cpt) +' on a '+ str(r))
"""
Boucle Tant que 
    une valeur est différente de 10
    A chaque tour de boucle, afficher l'index de boucle et la valeur dans le terminal
"""
