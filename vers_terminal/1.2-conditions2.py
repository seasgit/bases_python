"""
Objectif : 
    variables  = concaténation de nombre et texte
    Tirage aléatoire
    Evaluations multiples
    Affichage dans le terminal

    
"""
import random
## heure
r = random.randint(0,23)
heure = "Il est "+str(r)+" heure(s)"
if r == 0:
    out = "Il est minuit !"
elif r == 12:
    out = "Il est midi !"
elif (r > 20) or (r>=0 and r<6) :
    out = "C'est la nuit. "+heure
elif r >=6 and r <=12:
    out = "C'est le matin "+heure
elif r>=13 and r<=18:
    out = "C'est l'après midi "+heure
else:
    out = "C'est le soir "+heure

print(out)


