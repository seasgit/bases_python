import random
## 1 avexc un random
r = random.randint(1,10)
## 2 avec un input
r = int(input('combien ?'))
if r < 5:
    print(str(r) +" est un Score insuffisant")
elif r >=6 and r <=7:
    print(str(r) +" est un Score correct")
else:
    print(str(r) +" est un bon Score")


"""
Tirage aléatoire d'un score entre 1 et 10
Evaluation du score et affichage message dans le terminal
"""