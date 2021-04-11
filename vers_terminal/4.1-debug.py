import random
import pdb

animaux = ['chien','chat','cheval','poule','tortue','canard','vache','mouton']
dico = []
for a in animaux:
    dico.append({
        "name":a,
        "pop":random.randint(0,5)
    })

pdb.set_trace()

"""
    tester :
    (Pdb) dico
    (Pdb) dico:[1:2]
""
